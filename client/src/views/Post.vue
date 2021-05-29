<template lang="html">
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
</head>
<body>
<div class="post">
    <div class="main-container">
      <div class="body container">
        <div class="content">
          <svg id="delete-button" @click="deletePost" fill="#000000" height="24" viewBox="0 0 24 24" width="24" xmlns="http://www.w3.org/2000/svg">
            <title>Delete Post</title>
            <path d="M6 19c0 1.1.9 2 2 2h8c1.1 0 2-.9 2-2V7H6v12zM19 4h-3.5l-1-1h-5l-1 1H5v2h14V4z"/>
            <path d="M0 0h24v24H0z" fill="none"/>
          </svg>
          <svg id="verify-delete-button" v-show="deleteVerify" @click="deleteVerify = false" fill="#000000" height="24" viewBox="0 0 24 24" width="24" xmlns="http://www.w3.org/2000/svg">
            <title>Cancel</title>
            <path d="M19 6.41L17.59 5 12 10.59 6.41 5 5 6.41 10.59 12 5 17.59 6.41 19 12 13.41 17.59 19 19 17.59 13.41 12z"/>
            <path d="M0 0h24v24H0z" fill="none"/>
          </svg>

          <p class="error">{{ error }}</p>
          <h1>{{ title }}</h1>

          <h3>by
            <router-link :to="{ name: 'User', params: { 'username': user.username } }">
              {{ user.username }}
            </router-link>
             on {{ created }}
          </h3>


<i class="post-id">ID {{ id }}</i>

</div>
</div>
</div>
</div>

 
</body>


    <SubvueInfo class="subvue-info" v-if="subvue" :subvue="subvue"></SubvueInfo>
    <!-- Only show it if data was fetched -->
    <div v-else></div>

    <CreateButton></CreateButton>
  
</template>

<script>

import PostsService from '@/services/PostsService'

export default {
    name: 'post',


    data() {
        return {
            error: null,
            id: this.$route.params.id,
            title: '',
            user: '',
            /* subvue: null, */
            created: '',
            content: '',
            /* comments: [], */
            /* upvotes: [], */
            /* downvotes: [], */
            deleteVerify: false,

            /* newCommentContent: '', */
            /* errorCreateComment: null */
        }
    },

    methods: {
        deletePost() {
            if (this.deleteVerify) {
                PostsService.delete(this.id)
                    .then(() => {
                        this.$router.push({ name: 'Home' })
                    })
                    .catch(e => {
                        this.error = e.response.data.error
                    })
            } else {
                this.deleteVerify = true
            }
        },
    },

    mounted() {
        PostsService.item(this.id)
            .then(response => {
                this.title = response.data.title
                this.user = response.data.user
                this.created = response.data.created
                this.content = response.data.content
                /*this.comments = response.data.comments
                this.upvotes = response.data.upvotes
                this.downvotes = response.data.downvotes
                this.subvue = response.data.subvue */
            })
            .catch(e => {
                this.error = e.response.data.error
            })
    }
}
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
  width:30%;
}
table, th, td {
  border: 1px solid black;
  border-collapse: collapse;
}
th, td {
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
  background-color: #2196F3;
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

