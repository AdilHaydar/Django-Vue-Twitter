<template>
    <div class="explore">Explore</div>
</template>

<script>
export default {
    name: 'Explore',
    mounted(){
        this.$store.commit('setPageHeader', 'Explore')
    }
}
</script>