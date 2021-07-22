<template>
    <div class="profile">Profil</div>
</template>

<script>
export default {
    name: 'Profile',
    mounted(){
        this.$store.commit('setPageHeader', 'Profile')
    }
}
</script>