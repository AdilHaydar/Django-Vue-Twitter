<template>
  <div class="hello">
    <div class="box">
      <div class="columns">
        <div class="column is-1">
          <figure class="image is-48x48">
            <img class="is-rounded" src="../assets/logo.png" />
          </figure>
        </div>
          <div class="column is-11 ml-3">Undifined <span class="username">@{{tweet.user}}</span> 
           
          </div>
           
      </div>
      <div class="columns">
        <div class="column is-1"></div>
        <div class="columns is-11 ml-5 offset-3">{{tweet.content}}</div>
      </div>
      <!-- <div class="columns" v-if="tweet.files.length === 1">
        <div class="column is-1"></div>
        <div class="column is-11 ml-3">
          <figure class="image is-5by3" :key="'image-'+index" v-for="(image,index) in tweet.files"> MAX 4 IMAGE OLACAK VE https://bulma.io/documentation/elements/image/ BURADAN TWİTTER USULÜ max 4 parçalı fotolar konacak ekrana.2'li 4:3 4:3 3'lü 4:3 4:3 16:9 olacak şekilde sığdırılacak. 3'den fazla foto olunca 2 satır kullanılacak
            <img  :src="image.file" class="tweet-image">
          </figure>
        </div>
      </div> -->
      <TweetImage v-if="tweet.file" :Images="tweetFiles" :key="tweet.id"/>
      <div class="columns" style="margin-top:10px;">
        <div class="column is-2"></div>
        <div class="column is-3"><span class="activity-logo"><i class="far fa-comment"></i></span></div>
        <div class="column is-3"><span class="activity-logo"><i class="fas fa-retweet"></i></span></div>
        <div class="column is-2">
          <span class="activity-logo">
            <i class="far fa-heart"></i>
          </span>
          <span v-if="tweet.likes">
            {{tweet.likes}}
          </span>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import TweetImage from './TweetImage'

export default {
  name: 'TweetElement',
  components: { TweetImage },
  data(){
    return{
      tweetFiles: ''
    }
  },
  props: {
    tweet: Object
  },
  mounted(){
    // this.tweet.files.forEach((item) => {
    //   this.tweetFiles.push(item.file)
    // })
    this.tweetFiles = this.tweet.file
    console.log("Tweet File : (TweetElement.vue) => "+ this.tweet.file)

  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">
.box{
  background-color: #15202a;
  border: 1px solid #6A6A6A6A;
  border-radius: 5px;
  color: white;
}
.username{
  color: gray;
}
.activity-logo{
  padding: 10px;
}
.activity-logo:hover{
  background-color: rgba(255,255,255,0.1);
  border-radius: 100%;
  position: sticky;
}
.tweet-image{
  border: 1px solid #666;
  border-radius: 10px;
}
</style>
