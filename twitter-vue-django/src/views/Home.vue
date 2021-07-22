<template>
  <div class="home">
    <TweetForm />
    <TweetElement v-for="tweet in tweets" :tweet="tweet" :key="'tweet-'+tweet.id"/>
    
  </div>
</template>

<script>
import TweetElement from '@/components/TweetElement.vue'
import TweetForm from '@/components/TweetForm'
import axios from 'axios'

export default {
  name: 'Home',
  data(){
    return {
      tweets: []
    }
  },
  methods: {
    async getTweets(){
      axios.get('/api/tweets/')
      .then((result) => {
        this.tweets = result.data
      }).catch((err) => {
        console.log(err)
      });
    },
  },
  
  components: {
    TweetElement, TweetForm
  },
  mounted(){
    this.$store.commit('setPageHeader', 'Home')
    this.getTweets()

  },
}
</script>

<style>
.box{
  background-color: #15202a !important;
  border: 1px solid #6A6A6A6A;
  border-radius: 0px;
  color: white !important;
}
</style>
