<script setup lang="ts">
import { ref, Ref } from "vue"
import axios from "axios"
import VideoType from "./models/VideoType"
import PrevVideoType from "./models/prevVideoType"
import Video from "./components/Video.vue"
import PrevVideo from "./components/prevVideo.vue"

const link: Ref<string> = ref("")
const videos: Ref<VideoType[]> = ref([])
const prevVideos: Ref<PrevVideoType[]> = ref([])

const handleSubmit = async (e: Event) => {
    e.preventDefault();
    const videoResponse = await axios.post("http://localhost:5000/api/download", {"link": link.value})
    const videoData = videoResponse.data[0]

    videos.value.unshift(videoData)
    link.value = ""

    while (videoData.status !== "AVAILABLE") {
        await checkStatus(videoData.id)
        await new Promise<void>(resolve => setTimeout(resolve, 10000));
    }
}

const checkStatus = async (id: string) => {
    const statusResponse = await axios.get(`http://localhost:5000/api/download/${id}`)

    if (statusResponse.data[0].status == "AVAILABLE") {
        videos.value.map((video) => {
            if (video.id == id) {
                video.status = "AVAILABLE"
            }
        })
    }
}

const deleteVideo = (id: string) => {
    videos.value = videos.value.filter(video => video.id !== id);
}

const refetchVideo = async (id: string, link: string) => {
    prevVideos.value = prevVideos.value.filter(prevVideo => prevVideo.id !== id)
    console.log(link)
    const videoResponse = await axios.post("http://localhost:5000/api/download", {"link": link})
    const videoData = videoResponse.data[0]

    videos.value.unshift(videoData)

    while (videoData.status !== "AVAILABLE") {
        await checkStatus(videoData.id)
        await new Promise<void>(resolve => setTimeout(resolve, 10000));
    }
}

const fetchData = async () => {
    const response = await axios.get("http://localhost:5000/api")
    const data = response.data[0]
    prevVideos.value = data

}

fetchData()
</script>

<template>
    <div id="app-container">
        <h1 id="header">Audioify</h1>
        <h3 id="subheader">convert a youtube video to mp3.</h3>

        <form @submit="handleSubmit">
            <input id="input-field" type="text" placeholder="https://www.youtube.com/watch?v=6hBDh3dRvLc" v-model="link">
            <button id="submit-button" type="submit">convert! ►</button>
        </form>

        <Video 
            v-for="video in videos"
            :video="video"
            :status="video.status"
            :key="video.id"
            @delete-video="deleteVideo"
        />

        <h1>Below are videos you've converted previously:</h1>

        <PrevVideo
            v-for="prevVideo in prevVideos"
            :prevVideo="prevVideo"
            @refetch-video="refetchVideo"
        />

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
    
    h1 {
        font-weight: 500;
        margin-top: 5%;
    }

</style>
