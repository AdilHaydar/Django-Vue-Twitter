import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import axios from 'axios'

axios.defaults.baseURL = 'http://127.0.0.1:8000'
axios.defaults.headers.common["Authorization"] = "Token " + localStorage.getItem('token')

require("./assets/main.scss")

createApp(App).use(store).use(router).mount('#app')
