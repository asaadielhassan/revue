<template lang="html">
  <div class="feed container">
    <div class="title">
      <div class="textblock">
        <h1>The Public Feed</h1>
        <h5>Explore the world of Productify by viewing the public grids our community has been creating.</h5>
      </div>
    </div>
    <div class="styleme">
      <div class="grids">
        <GridPreview class="grid_card" v-for="grid in grids" :key="grid.id" :grid="grid">
            {{ grid.name }}
        </GridPreview>
      </div>
    </div>
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
      grids: null,
      hover: false
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

<style scoped lang="css">
::-webkit-scrollbar {
  width: 5px;
  height: 6px;
}

::-webkit-scrollbar-track {
  box-shadow: inset 0 0 5px #a5aaad;
  border-radius: 10px;
}

::-webkit-scrollbar-thumb {
  background: #3ea175;
  border-radius: 10px;
}

::-webkit-scrollbar-thumb:hover {
  background: #a5aaad;
}

* {
  margin: 0;
  padding: 0;
}
  .title {
    text-align: center;
    font-size: 2.2em;
    padding: 30px;
    color: #4F5D75;
    padding-top: 95px;
    padding-bottom: 115px;
    margin: 0;
    background-color: #BFC0C0;
    background-image: url('../assets/images/grid.png');
    background-size: 100%;

  }
  .title h5{
    width: 90%;
    font-size:.85em;
    margin: auto;
    margin-top: 20px;
  }
  .textblock{
    margin: auto;
    max-width: 45%;
    /*background-color: #4F5D75;
    background-color: rgba(79, 93, 117, .67);
    /*declared twice, once for backup and to show equvalency, then again to take theme color
    and apply an alpha scale to it*/
  }

.feed{
  background: #4F5D75;
  height: 100vh;
  grid-area: main;
  overflow-y: auto;
}

.styleme{
  border-left: 12px solid #eea073;
  border-right: 12px solid #eea073;
  height: 100vh;
}
.grids{
  margin: auto;
  background: linear-gradient(180deg, #BFC0C0 5%, #4F5D75 50%, 75%, #eea073 95%);
  width: 55%;
  align: center;
  padding-bottom: 50px;
  padding-top: 60px;
  height: 100vh;
}
.grid__card :hover {
  background: black;
  transition: all 0.1s ease-in-out;
}
</style>
