<template>
    <div id="app">
        <!-- <NavBar /> -->
        <header>
             <NewNav />
             
        </header>
       
        <main>
            <router-view />
        </main>
    </div>
</template>

<script>
// import NavBar from '@/components/NavBar'
import NewNav from '@/components/NewNav'

export default {
    name: 'app',
    components: { 
        // NavBar
        NewNav
    },

    created() {
        this.$store.dispatch('updateSubscribedSubvues')
    }
}
</script>


<style>
#app {
    font-family: "Avenir", Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
} 

 body {
    font-family: 'montserrat', sans-serif;
}

header {
    width: 100vw;
    background-color: rgb(235, 151, 102);
    /* background-color: steelblue; */
    padding: 5px;
    /* height: 40px; */
}
</style>
