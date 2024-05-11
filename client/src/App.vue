<script setup lang="ts">
import { ref, Ref } from "vue"
import axios from "axios";

const link: Ref<string> = ref("")
const videos: Ref<string[]> = ref([])

const handleSubmit = async (e: Event) => {
    e.preventDefault();
    const response = await axios.post("http://localhost:5000/api/download", {"link": link})
    const data = response.data[0]
    videos.value.push(data)
}
</script>

<template>
    <div id="app-container">
        <h1 id="header">Audioify</h1>
        <h3 id="subheader">convert a youtube video to mp3.</h3>

        <form @submit="handleSubmit">
            <input id="input-field" type="text" placeholder="https://www.youtube.com/watch?v=6hBDh3dRvLc" v-model="link">
            <button id="submit-button" type="submit">convert! ►</button>
        </form>

    </div>
</template>


<style scoped>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@100..900&family=Lobster&family=Roboto:wght@400;500;700&display=swap');

    #app-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        font-family: system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif
    }

    #header {
        font-weight: 400;
        font-size: 64px;
        margin: 0;
        margin-top: 10%;
    }

    #subheader {
        font-weight: 400;
        margin-bottom: 2%;
    }

    form {
        display: flex;
    }

    #input-field {
        height: 50px;
        width: 425px;
        font-size: 18px;
        background-color: #dcd2ad;
        border: solid;
        border-radius: 8px;
        padding-left: 10px;
        margin-right: 2%;
    }

    #input-field:focus {
        outline: none;
    }

    #submit-button {
        cursor: pointer;
        width: 70px;
        background-color: red;
        border: solid;
        border-radius: 8px;
        border-color: white;
        color: white;
    }
    
</style>
