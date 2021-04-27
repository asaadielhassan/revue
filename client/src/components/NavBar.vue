<template lang="html">
  <nav>
    <router-link class="title" :to="{ name: 'Home', params: {} }">Productify</router-link>
    <router-link  :to="{ name: 'AboutUs' }">About</router-link>
    <router-link  :to="{ name: 'GridFeed' }">Grid Feed</router-link>
    
    <!--<div class="dropdown"  @click="isOpen = !isOpen">
      <button class="dropbtn">
        Grid Feed
        <svg viewBox="0 0 1030 638" width="10">
          <path
            d="M1017 68L541 626q-11 12-26 12t-26-12L13 68Q-3 49 6 24.5T39 0h952q24 0 33 24.5t-7 43.5z"
            fill="#FFF"
          ></path>
        </svg>
      </button>
      <transition name="fade" appear>
      <div class="dropdown-content"  v-if="isOpen">
        <router-link
          v-for="subvue in $store.state.subscribedSubvues"
          :key="subvue.permalink"
          :to="{ name: 'Subvue', params: {name: subvue.permalink} }"
          >{{ subvue.name }}</router-link>
        <router-link class="create-subvue" :to="{ name: 'CreateSubvue' }">Create a Subvue</router-link>
      </div>
      </transition>
      
    </div>-->

    <router-link v-if="!$store.state.isUserLoggedIn" style="float:right" :to="{ name: 'SignUp', params: {} }">Sign Up</router-link>
    <router-link v-if="!$store.state.isUserLoggedIn" style="float:right" :to="{ name: 'Login', params: {} }">Login</router-link>

    <a v-if="$store.state.isUserLoggedIn" style="float:right" @click="logout()">Logout</a>
    <!-- <router-link v-if="$store.state.isUserLoggedIn" style="float:right" :to="{ name: 'User', params: { username: $store.state.user.username } }">{{ $store.state.user.username }}</router-link> -->
    <router-link v-if="$store.state.isUserLoggedIn" style="float:right" :to="{ name: 'User', params: { username: $store.state.user.username } }">My Grids</router-link>  
  </nav>
</template>

<script>
export default {
  name: 'nav',
  data() {
    return {
      isOpen: false,
    };
  },

  methods: {
    logout() {
      this.$store.dispatch('setToken', null)
      this.$store.dispatch('setUser', null)
      this.$router.push({name: 'Home'})
    }
  }
}
</script>

<style scoped lang="css">
nav {
  overflow: hidden; 
  background-color:  rgb(235, 151, 102);
  font-family: Arial;
}

nav a {
  float: left;
  font-size: 16px;
  color: white;
  text-align: center;
  padding: 14px 16px;
  text-decoration: none;
} 
nav .dropbtn svg {
  width: 10px;
  margin-left: 2px;
  margin-bottom: 3px;
}

 .title {
  font-weight: bold;
}
.about-us{
  /* background-color: rgb(23, 92, 93); */
  color: white !important;
}
.about-us:hover {
  background-color: rgb(7, 44, 45) !important;
}


.create-subvue {
  background-color: rgb(243, 175, 136);
  color: white !important;
}

.create-subvue:hover {
  background-color: rgb(194, 118, 56) !important;
}

.dropdown {
  float: left;
  overflow: hidden;
}

.dropdown .dropbtn {
  font-size: 16px;
  border: none;
  outline: none;
  color: white;
  padding: 14px 16px;
  background-color: inherit;
  font: inherit;
  margin: 0;
}

nav a:hover, .dropdown:hover .dropbtn {
  background-color: rgb(194, 118, 56);
   transition: all 0.2s ease-in-out;
}

.dropdown-content {
  display: none;
  position: absolute;
  background-color: rgb(243, 175, 136);
  min-width: 160px;
  box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
  z-index: 1;
}

.dropdown-content a {
  float: none;
  color: white;
  padding: 12px 16px;
  text-decoration: none;
  display: block;
  text-align: left;
}

.dropdown-content a:hover {
  background-color: rgb(194, 118, 56);
   transition: all 0.2s ease-in-out;
}

.dropdown:hover .dropdown-content {
  display: block;
}

.fade-enter-active,
.fade-leave-active {
  transition: all 0.2s ease-out;
}
.fade-enter,
.fade-leave-to {
  opacity: 0;
}
</style>
