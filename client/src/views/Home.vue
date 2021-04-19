<template lang="html">
  <div class="home container">
    <h1>Hello, {{ $store.state.user.username }}</h1>
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

<style lang="css">
</style>
