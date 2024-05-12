<script setup lang="ts">
import axios from "axios";
import prevVideoType from "../models/prevVideoType"

defineProps<{
    prevVideo: prevVideoType
}>()

const emits = defineEmits(['refetch-video']);

const handleRefetch = async (id: string, link: string) => {
    await axios.delete(`http://localhost:5000/api/download/${id}`)
    emits('refetch-video', id, link);
}
</script>

<template>
    <div class="vid-container">
        <img :src="prevVideo.thumbnail_link" width="240" height="180">
            <div class="vid-info">
                <p class="title">{{ prevVideo.title }}</p>
                <p>Upload Date: {{ new Date(prevVideo.date).toLocaleDateString() }}</p>
                <a :href="prevVideo.link">YouTube Link</a>
                <div class="audio-button">
                    <button class="refetch" @click="handleRefetch(prevVideo.id, prevVideo.link)">🔄 Refetch</button>
                </div>
            </div>
    </div>

</template>


<style scoped>
    .vid-container {
        display: flex;
        width: 800px;
        border: solid;
        border-radius: 20px;
        margin-top: 20px;
        overflow: hidden;
    }
    
    .vid-info {
        margin-left: 20px;
    }

    .title {
        font-weight: 500;
    }
    
    .status {
        font-weight: 500;
    }

    .refetch {
        color: white;
        cursor: pointer;
        background-color:rgb(0, 118, 0);
        border: none;
        border-width: 1px;
        border-radius: 4px;
        height: 25px;
        margin-top: 4%;
    }

    .audio-button {
        margin-top: 4%;
        display: flex;
        justify-content: space-between;
    }
    
</style>