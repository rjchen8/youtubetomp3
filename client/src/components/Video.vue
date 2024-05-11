<script setup lang="ts">
import Video from "../model"

defineProps<{
    video: Video
    status: Boolean
}>()
</script>

<template>
    <div class="vid-container">
        <img :src="video.thumbnail_link" width="240" height="180">
            <div class="vid-info">
                <p class="title">{{ video.title }}</p>
                <p>Upload Date: {{ video.date }}</p>
                <a :href="video.link">YouTube Link</a>
                <p>
                    <span class="status" v-if="!status">STATUS: Converting</span>
                    <audio v-else controls>
                        <source :src="video.download_link" type="audio/mp3">
                    </audio>
                </p>
            </div>
    </div>

</template>


<style scoped>
    .vid-container {
        display: flex;
        width: 800px;
        height: 180px;
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
</style>