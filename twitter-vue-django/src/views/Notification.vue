<template>
    <div class="notify">Notification</div>
</template>

<script>
export default {
    name: 'Notification',
    mounted(){
        this.$store.commit('setPageHeader', 'Notification')
    }
}
</script>