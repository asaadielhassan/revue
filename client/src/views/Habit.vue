<template lang="html">
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
</head>
<body>
<div class="post">
    <div class="main-container">
      <div class="body container">
        <div class="content">
          <svg id="delete-button" @click="deleteHabit" fill="#000000" height="24" viewBox="0 0 24 24" width="24" xmlns="http://www.w3.org/2000/svg">
            <title>Delete Grid</title>
            <path d="M6 19c0 1.1.9 2 2 2h8c1.1 0 2-.9 2-2V7H6v12zM19 4h-3.5l-1-1h-5l-1 1H5v2h14V4z"/>
            <path d="M0 0h24v24H0z" fill="none"/>
          </svg>
          <svg id="verify-delete-button" v-show="deleteVerify" @click="deleteVerify = false" fill="#000000" height="24" viewBox="0 0 24 24" width="24" xmlns="http://www.w3.org/2000/svg">
            <title>Cancel</title>
            <path d="M19 6.41L17.59 5 12 10.59 6.41 5 5 6.41 10.59 12 5 17.59 6.41 19 12 13.41 17.59 19 19 17.59 13.41 12z"/>
            <path d="M0 0h24v24H0z" fill="none"/>
          </svg>

          <p class="error">{{ error }}</p>
          <h1>{{ name }}</h1>

          <h3>by
            <router-link :to="{ name: 'User', params: { 'username': user.username } }">
              {{ user.username }}
            </router-link>
             on {{ string_start }}
          </h3>


<br>
<h4>Click on each day's checkbox once you completed the goal. Good luck on your goal pursuit!</h4>
<br>

<table id="t01">

<tr>
    <th>M</th>
    <th>T</th> 
    <th>W</th>
    <th>T</th> 
    <th>F</th>
    <th>S</th> 
    <th>S</th>
</tr>
<tr>
<td>
<div class="box">
<label class="container">
<input type="checkbox" id = "0" tag = "checkbox" v-on:click="(updatebox1(0))">
<span class="checkmark"></span>
</label>
</div>
</td>
<td><div class="box">
<label class="container">
<input type="checkbox" id = "1" tag = "checkbox" v-on:click="(updatebox1(1))">
<span class="checkmark"></span>
</label>
</div></td>
<td>
<div class="box">
<label class="container">
<input type="checkbox" id = "2" tag = "checkbox" v-on:click="(updatebox1(2))">
<span class="checkmark"></span>
</label>
</div></td>
<td>
<div class="box">
<label class="container">
<input type="checkbox" id = "3" tag = "checkbox" v-on:click="(updatebox1(3))">
<span class="checkmark"></span>
</label>
</div></td>
<td>
<div class="box">
<label class="container">
<input type="checkbox" id = "4" tag = "checkbox" v-on:click="(updatebox1(4))">
<span class="checkmark"></span>
</label>
</div></td>
<td>
<div class="box">
<label class="container">
<input type="checkbox" id = "5" tag = "checkbox" v-on:click="(updatebox1(5))">
<span class="checkmark"></span>
</label>
</div></td>
<td>
<div class="box">
<label class="container">
<input type="checkbox" id = "6" tag = "checkbox" v-on:click="(updatebox1(6))">
<span class="checkmark"></span>
</label>
</div></td>
</tr>

<tr>
<td>
<div class="box">
<label class="container">
<input type="checkbox" id = "7" tag = "checkbox" v-on:click="(updatebox1(7))">
<span class="checkmark"></span>
</label>
</div>
</td>
<td><div class="box">
<label class="container">
<input type="checkbox" id = "8" tag = "checkbox" v-on:click="(updatebox1(8))">
<span class="checkmark"></span>
</label>
</div></td>
<td>
<div class="box">
<label class="container">
<input type="checkbox" id = "9" tag = "checkbox" v-on:click="(updatebox1(9))">
<span class="checkmark"></span>
</label>
</div></td>
<td>
<div class="box">
<label class="container">
<input type="checkbox" id = "10" tag = "checkbox" v-on:click="(updatebox1(10))">
<span class="checkmark"></span>
</label>
</div></td>
<td>
<div class="box">
<label class="container">
<input type="checkbox" id = "11" tag = "checkbox" v-on:click="(updatebox1(11))">
<span class="checkmark"></span>
</label>
</div></td>
<td>
<div class="box">
<label class="container">
<input type="checkbox" id = "12" tag = "checkbox" v-on:click="(updatebox1(12))">
<span class="checkmark"></span>
</label>
</div></td>
<td>
<div class="box">
<label class="container">
<input type="checkbox" id = "13" tag = "checkbox" v-on:click="(updatebox1(13))">
<span class="checkmark"></span>
</label>
</div></td>
    
</tr>

<tr>
<td>
<div class="box">
<label class="container">
<input type="checkbox" id = "14" tag = "checkbox" v-on:click="(updatebox1(14))">
<span class="checkmark"></span>
</label>
</div>
</td>
<td><div class="box">
<label class="container">
<input type="checkbox" id = "15" tag = "checkbox" v-on:click="(updatebox1(15))">
<span class="checkmark"></span>
</label>
</div></td>
<td>
<div class="box">
<label class="container">
<input type="checkbox" id = "16" tag = "checkbox" v-on:click="(updatebox1(16))">
<span class="checkmark"></span>
</label>
</div></td>
<td>
<div class="box">
<label class="container">
<input type="checkbox" id = "17" tag = "checkbox" v-on:click="(updatebox1(17))">
<span class="checkmark"></span>
</label>
</div></td>
<td>
<div class="box">
<label class="container">
<input type="checkbox" id = "18" tag = "checkbox" v-on:click="(updatebox1(18))">
<span class="checkmark"></span>
</label>
</div></td>
<td>
<div class="box">
<label class="container">
<input type="checkbox" id = "19" tag = "checkbox" v-on:click="(updatebox1(19))">
<span class="checkmark"></span>
</label>
</div></td>
<td>
<div class="box">
<label class="container">
<input type="checkbox" id = "20" tag = "checkbox" v-on:click="(updatebox1(20))">
<span class="checkmark"></span>
</label>
</div></td>
    
</tr>

<tr>
<td>
<div class="box">
<label class="container">
<input type="checkbox" id = "21" tag = "checkbox" v-on:click="(updatebox1(21))">
<span class="checkmark"></span>
</label>
</div>
</td>
<td><div class="box">
<label class="container">
<input type="checkbox" id = "22" tag = "checkbox" v-on:click="(updatebox1(22))">
<span class="checkmark"></span>
</label>
</div></td>
<td>
<div class="box">
<label class="container">
<input type="checkbox" id = "23" tag = "checkbox" v-on:click="(updatebox1(23))">
<span class="checkmark"></span>
</label>
</div></td>
<td>
<div class="box">
<label class="container">
<input type="checkbox" id = "24" tag = "checkbox" v-on:click="(updatebox1(24))">
<span class="checkmark"></span>
</label>
</div></td>
<td>
<div class="box">
<label class="container">
<input type="checkbox" id = "25" tag = "checkbox" v-on:click="(updatebox1(25))">
<span class="checkmark"></span>
</label>
</div></td>
<td>
<div class="box">
<label class="container">
<input type="checkbox" id = "26" tag = "checkbox" v-on:click="(updatebox1(26))">
<span class="checkmark"></span>
</label>
</div></td>
<td>
<div class="box">
<label class="container">
<input type="checkbox" id = "27" tag = "checkbox" v-on:click="(updatebox1(27))">
<span class="checkmark"></span>
</label>
</div></td>
    
</tr>
  
</table>

<br>
<i class="post-id">ID: {{ id }}</i>

</div>
</div>
</div>
</div>

</body>


    <!-- <SubvueInfo class="subvue-info" v-if="subvue" :subvue="subvue"></SubvueInfo> -->
    <!-- Only show it if data was fetched -->
    <!-- <div v-else></div> -->

    <CreateButton></CreateButton>
  
</template>

<script>
// import PostsService from '@/services/PostsService'
import HabitsService from "@/services/HabitsService";

export default {
  name: "Habit",

  data() {
    return {
      error: null,
      id: this.$route.params.id,
      name: "",
      user: "",
      /* subvue: null, */
      start_Date: "",
      string_start: "",
      description: "",
      /* comments: [], */
      /* upvotes: [], */
      /* downvotes: [], */
      deleteVerify: false,
      habit_data: [],

      /* newCommentContent: '', */
      /* errorCreateComment: null */
    };
  },

  methods: {
    deleteHabit() {
      if (this.deleteVerify) {
        HabitsService.delete(this.id)
          .then(() => {
            this.$router.push({ name: "Home" });
          })
          .catch((e) => {
            this.error = e.response.data.error;
          });
      } else {
        this.deleteVerify = true;
      }
    },
    updatebox1(){
      console.log("Click");
      var temp = [];
      var checkboxes = document.querySelectorAll('input[type=checkbox]');
        var checkbox;
        for(checkbox of checkboxes){
          if(checkbox.checked == true){
            temp.push(["true", 0,0]);
          }
          else{
            temp.push(["false", 0,0]);
          }
        }
      var formData = new FormData();
      formData.append("habit_data", temp);
      console.log(formData);
      console.log(formData.get("habit_data"));
      HabitsService.update(this.id, formData)
        .then(() => {
        })
        .catch((error) => {
          this.error = error.response.data.error;
        });
    },
  },

  mounted() {

    HabitsService.item(this.id)
      .then((response) => {
        this.name = response.data.name;
        this.user = response.data.user;
        this.start_Date = response.data.start_Date;
        this.string_start = response.data.string_start;
        this.description = response.data.description;
        this.habit_data = response.data.habit_data;
        var checkboxes = document.querySelectorAll('input[type=checkbox]');
        var i = 0;
        var checkbox;
        for(checkbox of checkboxes){
        var x = this.habit_data[i][0];
          if(x == "true"){
           checkbox.checked = true;
         }
        i++;
        }
        /*this.comments = response.data.comments
                this.upvotes = response.data.upvotes
                this.downvotes = response.data.downvotes
                this.subvue = response.data.subvue */
      })
      .catch((e) => {
        this.error = e.response.data.error;
      });

  },
};
</script>

<style scoped lang="css">
.main-container {
  width: 80%;
  float: left;
}

* {
  box-sizing: border-box;
}

table {
  width: 30%;
}
table,
th,
td {
  border: 1px solid black;
  border-collapse: collapse;
}
th,
td {
  padding: 30px 30px 30px 30px;
  background-color: white;
}
#t01 tr:nth-child(even) {
  background-color: #eee;
}
#t01 tr:nth-child(odd) {
  background-color: #eee;
}

.box {
}

.row:after {
  content: "";
  display: table;
  clear: both;
}

.container {
  display: block;
  position: relative;
}

.container input {
  position: absolute;
  opacity: 0;
  cursor: pointer;
  height: 0;
  width: 0;
}

.checkmark {
  position: absolute;
  top: 0;
  left: 0;
  margin: -25px -12px -30px -18px;
  height: 50px;
  width: 50px;
  background-color: #eee;
  border: 1px solid black;
}

.box .container:hover input ~ .checkmark {
  background-color: #ccc;
}

.box .container input:checked ~ .checkmark {
  background-color: #2196f3;
}

.body {
  background: #eeeeee;
  position: relative;
  display: grid;
  grid-template-columns: 1fr 20fr;
}

#delete-button {
  position: absolute;
  right: 15px;
  top: 15px;
  cursor: pointer;
}

#delete-button:hover {
  fill: rgb(163, 7, 7);
}

#verify-delete-button {
  position: absolute;
  right: 40px;
  top: 15px;
  cursor: pointer;
}

#verify-delete-button:hover {
  fill: rgb(7, 163, 70);
}

h1 {
  margin: 0;
}

h3 {
  margin: 0;
  font-weight: 400;
}
</style>

