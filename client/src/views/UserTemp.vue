<template lang="html">
  <div class="user">

    <div class="container">
    <h2>{{ username }}'s Grids</h2>
      <div class="post-list">
        <GridPreview v-for="grid in grids" :key="grid.id" :grid="grid">
          {{ grid.name }}
        </GridPreview>
      </div>
    </div>

    <div class="info">
      <img :src="'https://www.gravatar.com/avatar/' + this.hashedEmail + '?s=200'" />
      <h1>{{ username }}</h1>
      <div class="len-posts button">{{ grids.length }} Grids</div>
    </div>

    <CreateButton></CreateButton>
  </div>
</template>

<script>
import GridPreview from '@/components/GridPreview'
import CreateButton from '@/components/CreateButton'
import UsersService from '@/services/UsersService'
import HabitsService from '@/services/HabitsService'

export default {
  name: 'user-temp',

  components: { CreateButton, GridPreview },

  data() {
    return {
      username: this.$route.params.username,
      grids: [],
      hashedEmail: ''
    }
  },

  mounted() {
    this.fetchData()
  },

  watch: {
    $route() {
      this.username = this.$route.params.username
      this.fetchData()
    }
  },

  methods: {
    fetchData() {
      UsersService.username(this.username)
        .then(response => {
          this.hashedEmail = response.data.hashedEmail
        })

      HabitsService.user(this.username)
        .then(response => {
          this.grids = response.data
        })
        .catch(e => {
          this.error = e.response.data.error
        })
    }
  }
}
</script>

<style css = scoped>
.container {
  width: 70%;
  float: right;
  text-align: left;
}

.info {
  width: 15%;
  float: left;
  padding-top: 20px;
  padding-left: 50px;
}

.info img {
  display: block;
  margin: 0 auto;
}

.button {
  background: blue;
  display: inline;
  padding: 10px 20px;
}

.post-preview:first-of-type {
  margin-top: 25px;
}

h2{
  font-size: 2.0em;
  margin-left: 200px;
  margin-top: 100px;
}

.post-preview {
    height: 150px;
    margin-bottom: 25px;
    display: block;
    color: black;
    display: grid;
    grid-template-columns: 3fr 1fr 15fr;
}

.body-area {
    color: black;
}

.blue-highlight {
    color: rgb(48, 99, 219);
}
</style>
