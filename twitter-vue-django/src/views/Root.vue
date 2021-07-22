<template>
<div class="row container">
    <div class="col-3 responsive-section">
        <LeftBar />
    </div>
    <div class="col-1 responsive-section-alternetive">
        <LeftBar />
    </div>
    <div class="col-6 responsive-section">
        <div class="box" style="margin-bottom:10px;font-size:24px;font-weight:bold;">{{this.$store.state.pageHeader}}</div>
        <router-view />
    </div>
    <div class="col-10 responsive-section-alternetive">
        <div class="box" style="margin-bottom:10px;font-size:24px;font-weight:bold;">{{this.$store.state.pageHeader}}</div>
        <router-view />
    </div>
    <div class="col-3 responsive-right-bar"> 
        <img alt="Vue logo" src="../assets/logo.png">
    </div>
</div>
</template>

<script>
import LeftBar from '@/components/LeftBar'
import axios from 'axios'

export default {
  data(){
    return {
    }
  },
  components: {
    LeftBar,
  },
  methods: {
    setToken(){
      const formData = {
      username: 'admin',
      password: 'admin',
      }
    axios.post('/api/token/', formData)
    .then((result) => {

      this.$store.commit('setToken', result.data.access)

      localStorage.setItem('token', result.data.access)
      
      }).catch((err) => {
        console.log(err)
      });
    }
  },
  mounted(){
    this.setToken()
  }
}
</script>

<style lang="scss">
@media screen and (max-width: 1000px) {
  .responsive-right-bar{
    display: none;
  }
}
@media screen and (max-width: 1000px) {
  .responsive-section{
    display: none;
  }
}
@media screen and (min-width: 1000px){
  .responsive-section-alternetive{
    display:none;
  }
}
body{
  background-color: #15202b;
  color: white;
  min-height: 1100px;
}
</style>
