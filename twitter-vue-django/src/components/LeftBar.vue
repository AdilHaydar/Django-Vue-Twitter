<template>
<div class="wrapper">
    <div class="left-bar" align="center">
        <ul class="left-bar float-right">
            <li class="bar-item" @click="this.$router.push({name:'Home'})"><i class="fas fa-home"></i></li>
            <li class="bar-item" @click="this.$router.push({name:'Explore'})"><i class="fas fa-search"></i></li>
            <li class="bar-item" @click="this.$router.push({name:'Notification'})"><i class="fas fa-bell"></i></li>
            <li class="bar-item" @click="this.$router.push({name:'Settings'})"><i class="fas fa-wrench"></i></li>
            <li class="bar-item" @click="this.$router.push({name:'Profile'})"><i class="fas fa-user"></i></li>
        </ul>
    </div>

    <div class="left-bar-big">
        <ul class="left-bar float-left">
            <li class="bar-item" @click="this.$router.push({name:'Home'})">
                <span>
                    <i class="fas fa-home"></i><span class="ml-5">Anasayfa</span>
                </span>
            </li>
            <li class="bar-item" @click="this.$router.push({name:'Explore'})">
                <span>
                    <i class="fas fa-search"></i> <span class="ml-5">Keşfet</span>
                </span>
            </li>
            <li class="bar-item" @click="this.$router.push({name:'Notification'})">
                <span>
                    <i class="fas fa-bell"></i> <span class="ml-5">Bildirimler</span>
                </span>
            </li>
            <li class="bar-item" @click="this.$router.push({name:'Settings'})">
                <span>
                    <i class="fas fa-wrench"></i> <span class="ml-5">Ayarlar</span>
                </span>
            </li>
            <li class="bar-item" @click="this.$router.push({name:'Profile'})">
                <span>
                    <i class="fas fa-user"></i> <span class="ml-5">Profil</span>
                </span>
            </li>
        </ul>
    </div>
</div>
    

</template>

<script>
export default {
    name: 'LeftBar',
}
</script>

<style lang="scss">
.left-bar{
    position: fixed;
}
.bar-item{
    color: white;
    padding: 10px;
    border-radius: 10px;
    width: 100%;
    font-weight: bold;
    font-size: 20px;
    justify-items: center;
    align-items: center;
    transition: 0.1s all
}

.bar-item:hover{
    color: #44aafd;
    background-color: rgba(255,255,255,0.1);
    cursor: pointer;
    transition: 0.1s all
}

@media screen and (min-width: 1000px) {
    div.left-bar{
        display: none;
    }
}
@media screen and (max-width: 1000px){
    div.left-bar-big{display:none;} 
}
</style>
