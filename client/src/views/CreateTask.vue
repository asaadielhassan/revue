<template lang="html">
  <body>
    <div class="container">
      <!-- Title  -->
      <div class="title">Make a Grid</div>
      <div class="content">

        <form  @submit.prevent="create" enctype="multipart/form-data">

          <!-- Grid name, Number of days, and description -->
          <div class="user-details">
            <div class="input-box">
              <span class="details">Grid Name</span>
              <input v-model="name" type="text" placeholder="Enter the name of your grid" ref="name" required>
            </div>
            <div class="input-box">
              <span class="details">Number of days</span>
              <input v-model="days" type="number" placeholder="Enter the total days to complete this" required>
            </div>
            <div class="input-box-description">
              <span class="details">Description</span>
              <input v-model="description" name="name" placeholder="Enter the description for your grid" required>
            </div>            
          </div>

          <!-- Make the grid public or not -->
          <div class="public-details">
            <input type="radio" name="pub" id="dot-1" value="true" v-model = "checked">
            <input type="radio" name="pub" id="dot-2" value="false" v-model = "checked">
            <span class="public-title">Do you want to make your Grid public?</span>
            <div class="category">
              <label for="dot-1">
                <span class="dot one"></span>
                <span class="pub">Yes</span>
              </label>
              <label for="dot-2">
                <span class="dot two"></span>
                <span class="pub">No</span>
              </label>
            </div>
          </div>

          <div class="button">
            <input type="submit" value="Build My Grid!">
          </div>
        </form>

      </div>
    </div>
  </body>
</template>

<script>
import HabitsService from "@/services/HabitsService";

export default {
  name: "create-task",

  data() {
    return {
      name: "",
      days: null,
      description: "",
      checked: null,
      error: null,
    };
  },

  methods: {
    create() {
      var shit;
      if (this.checked == "true")
        shit = "true";
      else 
        shit = "false";
      var formData = new FormData();
      formData.append("name", this.name);
      formData.append("num_Days", this.days);
      formData.append("is_public", shit);
      formData.append("description", this.description);
      console.log(formData);

      HabitsService.create(formData)
        .then((response) => {
          this.$router.push({
            name: "Habit",
            params: { id: response.data.id },
          });
        })
        .catch((error) => {
          this.error = error.response.data.error;
        });
    },
  },

  mounted() {
    // Focus title
    this.$refs.name.focus();
  },
};
</script>

<style scoped>
/* @import url("https://fonts.googleapis.com/css2?family=Poppins:wght@200;300;400;500;600;700&display=swap"); */
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
form .public-details .public-title {
  font-size: 16px;
  font-weight: 500;
}
form .category {
  display: flex;
  width: 80%;
  margin: 14px 0;
  gap: 30px;
}
form .category label {
  display: flex;
  align-items: center;
  cursor: pointer;
}
form .category label .dot {
  height: 18px;
  width: 18px;
  border-radius: 50%;
  margin-right: 10px;
  background: #d9d9d9;
  border: 5px solid transparent;
  transition: all 0.1s ease;
}
#dot-1:checked ~ .category label .one,
#dot-2:checked ~ .category label .two{
  background: #eb9766;
  border-color: #d9d9d9;
}
form input[type="radio"] {
  display: none;
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
/* @media (max-width: 584px) {
  .container {
    max-width: 100%;
  }
  form .user-details .input-box {
    margin-bottom: 15px;
    width: 100%;
  }
  form .category {
    width: 100%;
  }
  .content form .user-details {
    max-height: 300px;
    overflow-y: scroll;
  }
  .user-details::-webkit-scrollbar {
    width: 5px;
  }
}
@media (max-width: 459px) {
  .container .content .category {
    flex-direction: column;
  }
} */
</style>
