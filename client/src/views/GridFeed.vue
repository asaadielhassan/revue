<template lang="html">
  <div class="feed container">
    <!-- <PostPreview v-for="post in posts" :key="post.id" :post="post">
      {{ post.title }}
    </PostPreview> -->

    <GridPreview v-for="grid in grids" :key="grid.id" :grid="grid">
      {{ grid.name }}
    </GridPreview>

    <!-- <div v-for = "grid in grids" :key="grid.id">
      <h1> {{ grid.name }} </h1>
      <div class = "body-area">
        <h3><slot></slot></h3>
        <span>created on {{ grid.start_Date }}</span>
        <span>&nbsp;by <span class="blue-highlight">u/{{ grid.user.username }}</span></span>
      </div>
    </div> -->

    <CreateButton></CreateButton>
  </div>
</template>

<script>
// import PostPreview from '@/components/PostPreview'
// import PostsService from '@/services/PostsService'
import HabitsService from '@/services/HabitsService'
import CreateButton from '@/components/CreateButton'
import GridPreview from '@/components/GridPreview'

export default {
  name: 'grid-feed',

  // components: { PostPreview, CreateButton },
  components: {GridPreview, CreateButton},

  data() {
    return {
      grids: null
    }
  },

  mounted() {
    HabitsService.index()
      .then(response => {
        this.grids = response.data
      })
      .catch(e => {
          this.error = e.response.data.error
        })
  }
}
</script>

<style lang="css">
  .welcome {
    text-align: center;
  }

</style>
