<template>
    <div class="page-log-in">
        <div class="columns" style="color:white;">
            <div class="column is-4 is-offset-4">
                <h1 class="title" align="center" style="color:white;margin-top:25px;">Log in</h1>

                <form @submit.prevent="submitForm" class="box">
                    <div class="field">
                        <label>Username</label>
                        <div class="control">
                            <input type="text" class="input" v-model="username">
                        </div>
                    </div>

                    <div class="field">
                        <label>Password</label>
                        <div class="control">
                            <input type="password" class="input" v-model="password">
                        </div>
                    </div>

                    <div class="notification is-danger" v-if="errors.length">
                        <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
                    </div>

                    <div class="field">
                        <div class="control">
                            <button class="button is-info">Log in</button>
                        </div>
                    </div>

                    <hr>

                    Or <router-link to="/sign-up">click here</router-link> to sign up!
                </form>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'
export default {
    name: 'LogIn',
    data() {
        return {
            username: '',
            password: '',
            errors: []
        }
    },
    mounted() {
        document.title = 'Login'
    },
    methods: {
        async submitForm() {
            axios.defaults.headers.common["Authorization"] = ""
            localStorage.removeItem("token")
            const formData = {
                username: this.username,
                password: this.password
            }
            await axios
                .post("/api/token/", formData)
                .then(response => {
                    const token = response.data.access
                    this.$store.commit('setToken', token)
                    
                    axios.defaults.headers.common["Authorization"] = "Bearer " + token
                    localStorage.setItem("token", token)
                    const toPath = this.$route.query.to || '/'
                    this.$router.push(toPath)
                })
                .catch(error => {
                    if (error.response) {
                        console.log(error.response)
                        this.errors = []
                        for (const property in error.response.data) {
                            this.errors.push(`${property}: ${error.response.data[property]}`)
                        }
                    } else {
                        this.errors.push('Something went wrong. Please try again')
                        
                        console.log(JSON.stringify(error))
                    }
                })
        }
    }
}
</script>