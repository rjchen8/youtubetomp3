<script setup lang="ts">
import axios from "axios";
import Video from "../models/VideoType"

defineProps<{
    video: Video
    status: string
}>()

const emits = defineEmits(['delete-video']);

const handleDelete = async (id: string) => {
    await axios.delete(`http://localhost:5000/api/download/${id}`)
    emits('delete-video', id);
}
</script>

<template>
    <div class="vid-container">
        <img :src="video.thumbnail_link" width="240" height="180">
            <div class="vid-info">
                <p class="title">{{ video.title }}</p>
                <p>Upload Date: {{ new Date(video.date).toLocaleDateString() }}</p>
                <a :href="video.link">YouTube Link</a>
                <div class="audio-button">
                    <span class="status" v-if="status!=='AVAILABLE'">STATUS: Converting</span>
                    <audio v-else controls class="audio">
                        <source :src="video.download_link" type="audio/mp3">
                    </audio>
                    <button class="delete" @click="handleDelete(video.id)">🗑️ Delete</button>
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

    .delete {
        color: white;
        cursor: pointer;
        background-color: #DC4C64;
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