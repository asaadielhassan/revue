<template lang="html">
  <body>
    <div class="container">
      <!-- Title  -->
      <div class="title">Sign Up</div>
      <p class="error" :class="{ 'deprecated-error' : deprecatedError }">{{ error }}</p>
      <div class="content">

        <form  @submit.prevent="signUp">

          <!-- username and password -->
          <div class="user-details">
            <div class="input-box">
              <span class="details">Username</span>
              <input v-model="username" type="text" placeholder="Enter your username" ref="username" required>
            </div>
            <div class="input-box">
              <span class="details">Email</span>
              <input v-model="email" type="email" placeholder="Enter your email address" required>
            </div> 
            <div class="input-box">
              <span class="details">Password</span>
              <input v-model="password" type="password" placeholder="Enter your password" required>
            </div> 
            <div class="input-box">
              <span class="details">Repeat Password</span>
              <input v-model="passwordRepeat" type="password" placeholder="Enter your password again" required>
            </div>     
            <p v-if="!passwordsMatch" class="error">Passwords do not match!</p>      
          </div>

          <div class="button">
            <input type="submit" value="Login">
          </div>
        </form>

      </div>
    </div>
  </body>
</template>

<script>
import AuthenticationService from "@/services/AuthenticationService";

export default {
  name: "signup",

  data() {
    return {
      error: "",
      deprecatedError: false,
      username: "",
      password: "",
      passwordRepeat: "",
      email: "",
    };
  },

  methods: {
    signUp() {
      if (this.passwordsMatch) {
        this.deprecatedError = false;
        AuthenticationService.signup({
          username: this.username,
          password: this.password,
          email: this.email,
        })
          .then((response) => {
            this.$store.dispatch("setToken", response.data.token);
            this.$store.dispatch("setUser", response.data.user);
            this.$router.push({ name: "Home" });
          })
          .catch((e) => {
            this.error = e.response.data.error;
          });
      }
    },
  },

  computed: {
    passwordsMatch() {
      return this.password == this.passwordRepeat;
    },
  },

  watch: {
    username() {
      this.deprecatedError = true;
    },

    password() {
      this.deprecatedError = true;
    },

    passwordRepeat() {
      this.deprecatedError = true;
    },

    email() {
      this.deprecatedError = true;
    },
  },

  mounted() {
    this.$refs.username.focus();
  },
};
</script>

<style scoped>
  * {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    /* font-family: "Poppins", sans-serif; */
  }
  body {
    height: 100vh;
    display: flex;
    justify-content: center;
    align-items: center;
    padding: 10px;
    background: linear-gradient(90deg, #bfc0c0, #4f5d75, #eea073);
    /* background: #eb9766; */
  }
  .container {
    position: fixed;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    max-width: 700px;
    width: 100%;
    background-color: #fff;
    padding: 25px 30px;
    border-radius: 5px;
    box-shadow: 0 5px 10px rgba(0, 0, 0, 0.15);
  }
  .container .title {
    font-size: 45px;
    font-weight: 500;
    position: relative;
    color: #20222e;
  }
  .container .title::before {
    content: "";
    position: absolute;
    left: 0;
    bottom: 0;
    height: 3px;
    width: 30px;
    border-radius: 5px;
    background: linear-gradient(135deg, #eb9766, #4f5d75);
  }
  .content form .user-details {
    display: flex;
    flex-wrap: wrap;
    justify-content: space-between;
    margin: 20px 0 12px 0;
  }
  form .user-details .input-box {
    margin-bottom: 15px;
    width: calc(100% / 2 - 20px);
  }
  form .input-box span.details {
    display: block;
    font-weight: 500;
    margin-bottom: 5px;
    color: #20222e;
  }
  .user-details .input-box input {
    height: 45px;
    width: 100%;
    outline: none;
    font-size: 16px;
    border-radius: 5px;
    padding-left: 15px;
    border: 1px solid #ccc;
    border-bottom-width: 2px;
    transition: all 0.3s ease;
  }

  form .user-details .input-box-description {
    margin-bottom: 15px;
    width: 100%;
  }
  form .input-box-description span.details {
    display: block;
    font-weight: 500;
    margin-bottom: 5px;
  }

  .user-details .input-box-description input {
    height: 45px;
    width: 100%;
    outline: none;
    font-size: 16px;
    border-radius: 5px;
    padding-left: 15px;
    border: 1px solid #ccc;
    border-bottom-width: 2px;
    transition: all 0.3s ease;
  }
  .user-details .input-box input:focus,
  .user-details .input-box input:valid {
    border-color: #eb9766;
  }

  .user-details .input-box-description input:focus,
  .user-details .input-box-description input:valid {
    border-color: #eb9766;
  }

  form .button {
    height: 45px;
    margin: 35px 0;
    box-shadow: 3px 8px 22px rgba(94, 28, 68, 0.15);
  }
  form .button input {
    height: 100%;
    width: 100%;
    border-radius: 5px;
    border: none;
    color: #fff;
    font-size: 18px;
    font-weight: 100;
    letter-spacing: 1px;
    cursor: pointer;
    background: linear-gradient(45deg, #eb9766, #4f5d75);
  }
  form .button input:hover {
    background: linear-gradient(45deg, #a76b48, #333b4b);
    transition: all 0.1s ease-in-out;
  }
</style>
