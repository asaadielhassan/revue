<template lang="html">
  <div class="home container">
    <div class = "welcome">
      <h1 v-if="!$store.state.isUserLoggedIn"> Welcome to Productify </h1>
      <p v-if="!$store.state.isUserLoggedIn"> Add tasks, create beautiful grids, and see your productivity come to life with Productify! Make your grids public and share them with the world! Check out the grid feed to see what users have been creating. Start by creating an account here:</p>
      <router-link v-if="!$store.state.isUserLoggedIn" class="button" :to="{ name: 'SignUp', params: {} }">Sign Up</router-link>
    </div>
    <h1 v-if="$store.state.isUserLoggedIn">Hello, {{ $store.state.user.username }}</h1>
    <!-- <PostPreview v-for="post in posts" :key="post.id" :post="post">
      {{ post.title }}
    </PostPreview> -->

    <CreateButton></CreateButton>
  </div>
</template>

<script>
// import PostPreview from '@/components/PostPreview'
import PostsService from '@/services/PostsService'
import CreateButton from '@/components/CreateButton'

export default {
  name: 'home',

  // components: { PostPreview, CreateButton },
  components: {CreateButton},

  data() {
    return {
      posts: null
    }
  },

  mounted() {
    PostsService.index()
      .then(response => {
        this.posts = response.data
      })
  }
}
</script>

<style scoped lang="css">
  .welcome {
    margin-top: 60px;
    font-size: 1.7em;
    text-align: center;
  }
 
  p{
    font-size: 1.6em;
    margin: 65px;
    margin-bottom: 100px;
  }

  .button{
    padding: 30px;
    font-size: 1.5em;
    border: double 30px white;
    margin-top: 80px;
  }


</style>
