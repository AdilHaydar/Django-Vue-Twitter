import { createStore } from 'vuex'

export default createStore({
  state: {
    pageHeader: '',
    token: '',
    isAuthenticated: false,
    file: '',
  },
  mutations: {
    initializeStore(state){
      if (localStorage.getItem('token')){
        state.token = localStorage.getItem('token')
        state.isAuthenticated = true
      }
      else {
        state.token = ''
        state.isAuthenticated = false
      }
    },
    setPageHeader(state, val){
      state.pageHeader = val
    },
    setToken(state, val){
      state.token = val
      state.isAuthenticated = true
    },
    removeToken(state){
      state.token = ''
      state.isAuthenticated = false
    },
    setFile(state, val){
      state.file = val
    },
    removeFile(state){
      state.file = ''
    }
  },
  actions: {
  },
  modules: {
  }
})
