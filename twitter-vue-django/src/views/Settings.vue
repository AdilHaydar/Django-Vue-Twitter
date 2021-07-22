<template>
    <div class="settings">Settings</div>
</template>

<script>
export default {
    name: 'Settings',
    mounted(){
        this.$store.commit('setPageHeader', 'Settings')
    }
}
</script>