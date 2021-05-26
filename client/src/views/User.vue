<template lang="html">
  <body id="body">
      <div class="container">
        <main>
          <div class="main__container">

            <!-- Hello <username> -->
            <div class="main__title">
              <i class="fa fa-user-circle fa-2x text-navy" aria-hidden="true"></i>
              <div class="main__greeting">
                <h1 v-if="$store.state.isUserLoggedIn">Hello {{ $store.state.user.username }}</h1>
                <p>Welcome to your grid dashboard</p>
              </div>
            </div>

            <!-- Number of grids and create a new grid -->
            <div class="main__cards">
              <div class="card">
                <i
                  class="fa fa-table fa-2x text-lightblue"
                  aria-hidden="true"
                ></i>
                <div class="card_inner">
                  <p class="text-primary-p">Number of Grids</p>
                  <span class="font-bold text-title">{{ grids.length }}</span>
                </div>
              </div>

              <router-link v-if="$store.state.isUserLoggedIn"  :to="{ name: 'CreatePost'}">
                <div class="card2">
                  <i class="fa fa-plus fa-2x text-red" aria-hidden="true"></i>
                  <div class="card_inner">
                    <p class="text-primary-p">Create a new Grid</p>
                  </div>
                </div>
              </router-link>
            </div>

            <!-- Random picture and list of grids -->
            <div class="charts">
              <div class="charts__left">
                <div class="charts__left__title">
                  <div>
                    <h1>Random Picture of the day</h1>
                    <p>This picture is from unsplash</p>
                  </div>
                  <i class="fa fa-image" aria-hidden="true"></i>
                </div>
                <img src="https://source.unsplash.com/featured/daily?landscape" class = "rnd-img">
              </div>

              <div class="charts__right">
                <div class="charts__right__title">
                  <div>
                    <h1>Grids</h1>
                    <p>Tasks you are working on</p>
                  </div>
                  <i class="fa fa-table" aria-hidden="true"></i>
                </div>

                <div class="charts__right__cards">
                  <UserGridPreview class="grid__card" v-for="grid in grids" :key="grid.id" :grid="grid">
                    <h1> {{ grid.name }} </h1>
                  </UserGridPreview>
                </div>
              </div>
            </div>
          </div>
        </main>      
      </div>
  </body>
</template>

<script>
import UserGridPreview from "@/components/UserGridPreview";
import HabitsService from "@/services/HabitsService";

export default {
  name: "user",

  components: { UserGridPreview },

  data() {
    return {
      username: this.$route.params.username,
      grids: [],
    };
  },

  mounted() {
    this.fetchData();
  },

  watch: {
    $route() {
      this.username = this.$route.params.username;
      this.fetchData();
    },
  },

  methods: {
    fetchData() {
      HabitsService.user(this.username)
        .then((response) => {
          this.grids = response.data;
        })
        .catch((e) => {
          this.error = e.response.data.error;
        });
    },
  },
  computed: {
    description() {
      return this.grid.description.slice(0, 750) + "...";
    },
  },
};
</script>

<style scoped>

/*  styling scrollbars  */
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

body {
  box-sizing: border-box;
}

.text-primary-p {
  color: #535d70;
  font-size: 14px;
  font-weight: 700;
}

.font-bold {
  font-weight: 700;
}

.text-title {
  color: #2e4a66;
}

.text-lightblue {
  color: #469cac;
}

.text-red {
  color: #cc3d38;
}

.text-navy {
  color: #373f4d;
}

.container {
  display: grid;
  height: 100vh;
  width: 100%;
  grid-template-columns: 0.8fr 1fr 1fr 1fr;
  grid-template-areas:
    "main main main main";
}

main {
  background: linear-gradient(90deg, #BFC0C0, #4F5D75, #eea073);
  grid-area: main;
  overflow-y: auto;
}

.main__container {
  padding: 20px 35px;
}

.main__title {
  display: flex;
  align-items: center;
}

.main__title > i {
  max-height: 100px;
  object-fit: contain;
  margin-right: 30px;
}

.main__greeting > h1 {
  font-size: 45px;
  font-weight: 100;
  color: #20222e;
  margin-bottom: 5px;
}

.main__greeting > p {
  font-size: 19px;
  /* font-weight: 700; */
  color: #373f4d;
  line-height: 1.3;
}

.main__cards {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 30px;
  margin: 20px 0;
}

.card {
  display: flex;
  flex-direction: column;
  justify-content: space-around;
  height: 70px;
  padding: 25px;
  border-radius: 5px;
  background: #e2e1e1;
  box-shadow: 2px 2px 6px #525151, -2px -2px 6px #525151;
}

.card_inner {
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.card_inner > span {
  font-size: 25px;
}

.card2 {
  display: flex;
  flex-direction: column;
  justify-content: space-around;
  height: 70px;
  padding: 25px;
  border-radius: 5px;
  background: #e2e1e1;
  box-shadow: 2px 2px 6px #525151, -2px -2px 6px #525151;
}

.card2:hover {
  background: #bbbbbb;
  transition: all 0.1s ease-in-out;
}

.charts {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 30px;
  margin-top: 20px;
}

.charts__left {
  padding: 25px;
  border-radius: 5px;
  background: #e2e1e1;
  box-shadow: 2px 2px 6px #525151, -2px -2px 6px #525151;
}

.charts__left__title {
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.charts__left__title > div > h1 {
  font-size: 24px;
  color: #2e4a66;
  margin-bottom: 2.5px;
}

.charts__left__title > div > p {
  font-size: 14px;
  font-weight: 700;
  color: #535d70;
}

.charts__left__title > i {
  color: #ffffff;
  font-size: 20px;
  background: #313b4b;
  border-radius: 200px 0px 200px 200px;
  -moz-border-radius: 200px 0px 200px 200px;
  -webkit-border-radius: 200px 0px 200px 200px;
  border: 0px solid #000000;
  padding: 15px;
}

.rnd-img {
  width: 100%;
  height: 95%;
  object-fit: contain;
}

.charts__right {
  padding: 25px;
  border-radius: 5px;
  background: #e2e1e1;
  box-shadow: 2px 2px 6px #525151, -2px -2px 6px #525151;
}

.charts__right__title {
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.charts__right__title > div > h1 {
  font-size: 24px;
  color: #2e4a66;
  margin-bottom: 5px;
}

.charts__right__title > div > p {
  font-size: 14px;
  font-weight: 700;
  color: #535d70;
}

.charts__right__title > i {
  color: #ffffff;
  font-size: 20px;
  background: #39447a;
  border-radius: 200px 0px 200px 200px;
  -moz-border-radius: 200px 0px 200px 200px;
  -webkit-border-radius: 200px 0px 200px 200px;
  border: 0px solid #000000;
  padding: 15px;
}

.charts__right__cards {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 20px;
  margin-top: 20px;
}

.grid__card {
  /* background: linear-gradient(45deg, #eb9766, #4F5D75); */
  background: #e0c6b7;
  /* background: linear-gradient(45deg, #eb9766, #4F5D75); */
  color: #2e4a66;
  border: 1px solid #2e4a66;
  text-align: center;
  padding: 25px;
  border-radius: 5px;
  font-size: 14px;
}

.grid__card:hover {
  background: #b6a195;
  transition: all 0.1s ease-in-out;
}
</style>