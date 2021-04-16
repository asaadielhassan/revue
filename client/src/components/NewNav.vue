<template>
  <nav>
    <router-link class="title" :to="{ name: 'Home', params: {} }"
      >Productify</router-link
    >
    <router-link class="menu-item" :to="{ name: 'AboutUs' }">About</router-link>

    <!-- <div class="menu-item"><a href="#">Contact</a></div> -->
    <Dropdown title="Dropdown" :items="services" />

    <router-link
      class="sign-up"
      v-if="!$store.state.isUserLoggedIn"
      style="float: right"
      :to="{ name: 'SignUp', params: {} }"
      >Sign Up</router-link
    >

    <router-link
      class="menu-item"
      v-if="!$store.state.isUserLoggedIn"
      style="float: right"
      :to="{ name: 'Login', params: {} }"
      >Login</router-link
    >

    <router-link
      class="sign-up"
      v-if="$store.state.isUserLoggedIn"
      style="float: right"
      :to="{ name: 'User', params: { username: $store.state.user.username } }"
      >{{ $store.state.user.username }}</router-link
    >

    <a
      class="menu-item"
      v-if="$store.state.isUserLoggedIn"
      style="float: right"
      @click="logout()"
      >Logout</a
    >
  </nav>
</template>

<script>
import Dropdown from "./Dropdown";
export default {
  name: "navbar",
  components: {
    Dropdown,
  },
  //   data() {
  //     return {
  //       services: [
  //         {
  //           title: "Web",
  //           link: "#",
  //         },
  //         {
  //           title: "Design",
  //           link: "#",
  //         },
  //         {
  //           title: "Videos",
  //           link: "#",
  //         },
  //       ],
  //     };
  //   },
  methods: {
    logout() {
      this.$store.dispatch("setToken", null);
      this.$store.dispatch("setUser", null);
      this.$router.push({ name: "Home" });
    },
  },
};
</script>

<style>
nav {
  display: flex;
  align-items: center;
  justify-content: center;
  /* text-align: center; */
}

nav .menu-item {
  color: #fff;
  padding: 14px 25px;
  position: relative;
  text-align: center;
  border-bottom: 3px solid transparent;
  display: flex;
  transition: 0.4s;
  font-size: 18px;
}

nav .menu-item.active,
nav .menu-item:hover {
  background-color: rgb(194, 118, 56);
  border-bottom-color: #303030;
}

nav .menu-item a {
  color: inherit;
  text-decoration: none;
}

nav .title {
  color: #fff;
  font-family: Arial;
  padding: 10px 20px;
  position: relative;
  text-align: center;
  border-bottom: 3px solid transparent;
  display: flex;
  transition: 0.4s;
  /* font-weight: bold; */
  font-size: 25px;
  
}


nav .title.active,
nav .title:hover {
  background-color: rgb(194, 118, 56);
  border-bottom-color: #303030;
}

nav .title a {
  color: inherit;
  text-decoration: none;
}

nav .sign-up {
  color: #fff;
  padding: 15.5px 20px;
  position: relative;
  text-align: center;
  border-bottom: 3px solid transparent;
  display: flex;
  transition: 0.4s;
  margin-left: 1325px;
  font-size: 18px;
}

nav .sign-up.active,
nav .sign-up:hover {
  background-color: rgb(194, 118, 56);
  border-bottom-color:#303030;
}

nav .sign-up a {
  color: inherit;
  text-decoration: none;
}
</style>
