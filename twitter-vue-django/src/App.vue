<template>
<router-view />
</template>

<script>
import axios from 'axios'

export default {
  beforeCreate(){
    this.$store.commit('initializeStore')

    const token = this.$store.state.token
    if (token) {
      axios.defaults.headers.common['Authorization'] = "Bearer " + token
    } else {
      axios.defaults.headers.common['Authorization'] = ""
    }
  }
}
</script>

