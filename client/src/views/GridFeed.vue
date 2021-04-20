<template lang="html">
  <div class="feed container">
    <PostPreview v-for="post in posts" :key="post.id" :post="post">
      {{ post.title }}
    </PostPreview>

    <CreateButton></CreateButton>
  </div>
</template>

<script>
// import PostPreview from '@/components/PostPreview'
import PostsService from '@/services/PostsService'
import CreateButton from '@/components/CreateButton'
import PostPreview from '@/components/PostPreview'

export default {
  name: 'grid-feed',

  // components: { PostPreview, CreateButton },
  components: {PostPreview, CreateButton},

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
  .welcome {
    text-align: center;
  }

</style>
