 <template lang="html">
  <!-- <div class="home container"> -->
    <!-- <div class = "welcome">
      <h1 v-if="!$store.state.isUserLoggedIn"> Welcome to Productify </h1>
      <p v-if="!$store.state.isUserLoggedIn"> Add tasks, create beautiful grids, and see your productivity come to life with Productify! Make your grids public and share them with the world! Check out the grid feed to see what users have been creating. Start by creating an account here:</p>
      <router-link v-if="!$store.state.isUserLoggedIn" class="button" :to="{ name: 'SignUp', params: {} }">Sign Up</router-link>
    </div> -->
    <!-- <h1 v-if="$store.state.isUserLoggedIn">Hello, {{ $store.state.user.username }}</h1> -->
    <!-- <PostPreview v-for="post in posts" :key="post.id" :post="post">
      {{ post.title }}
    </PostPreview> -->

    <!-- <CreateButton></CreateButton> -->
  <!-- </div> -->
  <div class = "container">

    <!-- random image from unsplash that changes daily     -->
    <div class = "img-container">
      <img v-if="$store.state.isUserLoggedIn" src="https://source.unsplash.com/featured/daily?motivation,quotes" class = "rnd-img">
    </div>

    <!-- to do image before logging in  -->
      <img v-if="!$store.state.isUserLoggedIn" src = "../assets/images/todo.png" class = "feature-img">

    <div class = "content">
      <!-- before logging in  -->
      
      
      <h1  v-if="!$store.state.isUserLoggedIn"> Welcome to Productify </h1>

      <!-- after loggin in  -->
      <h1 v-if="$store.state.isUserLoggedIn">Hello, {{ $store.state.user.username }}</h1>

      <!-- description of productivity  -->
      
      <p> 
        Add tasks, create beautiful grids, and see your productivity come to life with Productify! <br>
        Make your grids public and share them with the world! <br>
        Check out the grid feed to see what users have been creating. <br> <br>
      </p>

      <!-- create an account button  -->
      <p v-if="!$store.state.isUserLoggedIn" >
        Start by creating an account here:
      </p>
      <router-link v-if="!$store.state.isUserLoggedIn" class = "btn" :to="{ name: 'SignUp', params: {} }">Create New Account</router-link>
      
      <p v-if="!$store.state.isUserLoggedIn" >
        Already have an account?
      </p>

      <router-link v-if="!$store.state.isUserLoggedIn" class = "btn" :to="{ name: 'Login', params: {} }">Log in</router-link>       

      <router-link v-if="$store.state.isUserLoggedIn" class = "btn" :to="{ name: 'CreatePost'}">Create A New Grid</router-link>
      <router-link v-if="$store.state.isUserLoggedIn" class = "btn2" :to="{ name: 'User', params: { username: $store.state.user.username } }">View My Current Grids</router-link>  
    </div> 
  </div>

</template>

<script>
// import PostPreview from '@/components/PostPreview'
import PostsService from '@/services/PostsService'
// import CreateButton from '@/components/CreateButton'

export default {
  name: 'home',

  // components: { PostPreview, CreateButton },
  // components: {CreateButton},

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

<style scoped>
  * {
    margin: 0;
    padding: 0;
  }

  .container {
    height: 100vh;
    width: 100%;
    background-image: url('../assets/images/custom.png');
    background-position: center;
    background-size: cover;
    padding-left: 5%;
    padding-right: 10%;
    box-sizing: border-box;
    position: relative;
  }

  .content h1 {
    font-size: 60px;
    font-weight: 100;
    margin-top: 24px;
    margin-bottom: 15px;
    color: #2D3142;

  }

  .content p {
    font-size: 20px;
    color: #4F5D75;
    line-height: 1.3;
    
  }

  .content{
    margin-left: 5%;
    margin-top: 19%;
  }

  .content .btn{
    display: inline-block;
    background: linear-gradient(45deg, #eb9766, #4F5D75);
    border-radius: 6px;
    padding: 15px 25px;
    box-sizing: border-box;
    text-decoration: none;
    color: #fff;
    box-shadow: 3px 8px 22px rgba(94, 28, 68, 0.15);
    margin-top: 5px;
    margin-bottom: 30px;
  }

  .content .btn:hover{
    background: linear-gradient(45deg, #a76b48, #333b4b);
    transition: all 0.2s ease-in-out;
  }

  .content .btn2{
    display: inline-block;
    background: linear-gradient(45deg, #eb9766, #4F5D75);
    border-radius: 6px;
    padding: 15px 25px;
    box-sizing: border-box;
    text-decoration: none;
    color: #fff;
    box-shadow: 3px 8px 22px rgba(94, 28, 68, 0.15);
    margin-top: 40px;
    margin-left: 5%;
  }

  .content .btn2:hover{
    background: linear-gradient(45deg, #a76b48, #333b4b);
    transition: all 0.2s ease-in-out;
  }

  .feature-img {
    height: 90%;
    position: absolute;
    margin-top: 50px;
    right: 200px;
  }

  .img-container {
    width: 575px;
    height: 575px;
    margin-top: 150px;
    float: right;
  }

  .rnd-img {
    width: 100%;
    height: 100%;
    object-fit: contain;
  }


  
  


  /* .welcome {
    margin-top: 60px;
    font-size: 1.7em;
    text-align: center;
  } */
 
  /* p{
    font-size: 1.0em;
    margin: 65px;
    margin-bottom: 100px;
  } */

  /* .button{ */
    /* padding: 10px; */
    /* font-size: 1.0em; */
    /* border: double 30px white; */
    /* margin-top: 80px; */
  /* } */


</style>
