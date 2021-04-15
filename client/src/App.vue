<template>
    <div id="app">
        <NavBar />
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
    background-color: #222;
    padding: 15px;
}
</style>
