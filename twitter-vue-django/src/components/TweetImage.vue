<template>
    <div class="tweetImage">
        <vue-easy-lightbox
    :visible="visible"
    :imgs="items"
    :index="index"
    @hide="handleHide" />
     <figure>
        <img :src="Images" @click="() => showImg(0)">
    </figure>
    </div>
    

    
</template>

<script>
import VueEasyLightbox from 'vue-easy-lightbox'

export default {
    name: 'TweetImage',
    components: { VueEasyLightbox },
    props: {
        Images: String
    },
    data(){
        return {
            items: [],
            index: null,
            visible: false,
        }
    },
    mounted(){
        this.items.push(this.Images)
    },
    methods: {
      showImg(index) {
        this.index = index
        this.visible = true
      },
      handleHide() {
        this.visible = false
      }
    }
    
}
</script>

<style>
.slider-image{
    width: 100%;
    max-height: 400px;
}
</style>