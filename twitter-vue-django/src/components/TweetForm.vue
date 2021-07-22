<template>
    <div class="tweet-form">
        <form method="POST" @submit.prevent="submitForm" id="tweet-form" enctype="multipart/form-data">
            <div class="columns">
                <div class="column is-1">
                    <figure class="image is-48x48">
                        <img class="is-rounded" src="../assets/logo.png" />
                    </figure>
                </div>
                    <div class="column is-11">
                        <textarea @keydown="textAreaAdjust($event)" name="tweet" id="tweet_id" class="tweet-input" rows="2" placeholder="Say Something" v-model="tweet"></textarea>
                        <div class="columns">
                            <img class="preview-image" v-if="file" :src="file" />
                        </div>
                        
                        
                        <label class="tweet-input-extra">
                            <i class="file_upload fas fa-photo-video" style="color:#44aafd"></i>
                            <input type="file" ref="file" id="file_id" @change="readFile($event)" accept=".jpg, .jpeg, .png, .mp4, .wmv, .avi"
                            />
                        </label>
                        <button class="button edited-button is-info float-right">Tweet</button>
                        
                    </div>   
            </div>
            
            
        </form>
    </div>
</template>

<script>
import axios from 'axios'

export default {
    name: 'TweetForm',
    data(){
        return {
            tweet: '',
            file: null,
            image: '',
        }
    },
    methods: {
        submitForm(){
            const data = {
                'content': this.tweet,
                'file' : this.image,
            }
            axios.post('/api/add-tweet/', 
            data,
            {
                method: 'POST',
                headers:{
                    'Content-Type': 'multipart/form-data'
                }
            })
            .then((result) => {
                console.log(result.data)
                this.tweet = ''
                //this.files = []
                this.$store.commit('removeFile')
            }).catch((err) => {
                console.log(err)
            });
        },
        textAreaAdjust(element){
            element.target.style.height = "3px";
            element.target.style.height = (25+element.target.scrollHeight)+"px";
        },
        readFile(event){
            this.image = this.$refs.file.files[0]
            let reader = new FileReader()
            reader.onload = (e) => {
                this.file = e.target.result
                this.$store.commit('setFile', this.file)
            }
            
            reader.readAsDataURL(event.target.files[0])
        },
    },
    mounted(){
        this.file = this.$store.state.file
    },
}
</script>

<style>
.tweet-input-extra{
    border-radius: 100%;
    padding: 10px;
}
.tweet-input-extra:hover{
    background-color: rgba(255,255,255,0.1);
}
.edited-button{
    border-radius: 30px !important;
    width: 100px;
}
.tweet-input{
    width: 100%;
    background-color: #15202A;
    color: white;
    border: none;
    resize: none;
    font-size: 18px;
    padding: 10px;
    overflow:hidden
}
.tweet-input:focus{
    outline: none;
}
::placeholder{
    color: lightgray;
}
.tweet-form{
    border-left: 1px solid #6A6A6A6A;
    border-right: 1px solid #6A6A6A6A;
    border-bottom: 1px solid #6A6A6A6A;
    margin-bottom: 10px;
    padding: 0 10px 10px 10px;
}
.preview-image{
    padding: 10px;
}
#file_id
{
display: none;
}
</style>