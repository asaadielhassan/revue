<template lang="html">
  <div class="create-task container">
    <h1>Create Task</h1>
    <form @submit.prevent="create" enctype="multipart/form-data">
      <p class="error">{{ error }}</p>
      <input v-model="title" type="text" placeholder="Title" ref="title">
      <input v-model="subvue" type="text" placeholder="Subvue">
      <div v-if="imagePreview" id="image-preview" :style="'background-image: url(' + imagePreview + ')'"></div>
      <div id="image-upload">
        <p>
          <span v-if="!image">Drag your image here to begin<br> or click to browse</span>
          <span v-else>
            {{ image.name }}
          </span>
        </p>
        <input type="file" @change="fileChanged" accept="image/*">
      </div>
      <textarea v-model="content" name="name" placeholder="Content" rows="25" cols="80"></textarea>
      <input class="button" type="submit" value="Create post">
    </form>
  </div>
</template>


<script>
    import TaskPreview from '@/components/TaskPreview'

    export default {
        name: 'TaskScheduler',

        components: {TaskPreview},

        data(){
            return{ 
                tasks: [],
                title: "Schedule A Task:"
                task: ["Workout Daily", 30, "day", "#ffffff", .1]
            }
        },

        mounted(){
            this.$refs.title.focus();
        }
    }

</script>

<style>
form {
    max-width: 1500px;
    width: 100%;
    margin: 0 auto;
}

input,
textarea {
    display: block;
    width: 100%;
    margin: 0;
    border: none;
    background: rgb(223, 224, 221);
    padding: 15px;
    margin: 20px 0;

    -webkit-box-sizing: border-box; /* Safari/Chrome, other WebKit */
    -moz-box-sizing: border-box; /* Firefox, other Gecko */
    box-sizing: border-box; /* Opera/IE 8+ */
}

#image-upload {
    outline: 2px dashed grey;
    outline-offset: -10px;
    background: rgb(223, 224, 221);
    color: dimgray;
    cursor: pointer;
    position: relative;
    height: 100px;
}

#image-upload:hover {
    background: rgb(191, 191, 191);
}

#image-upload input {
    opacity: 0; /* invisible but it's there! */
    width: 100%;
    height: 100%;
    cursor: pointer;
}

#image-upload p {
    text-align: center;
    position: absolute;
    position: absolute;
    top: 0;
    bottom: 0;
    left: 0;
    right: 0;
    width: 50%;
    height: 30%;
    margin: auto;
    width: 100%;
}

#image-preview {
    margin: 0 auto;
    max-width: 250px;
    width: 100%;
    height: 150px;
    background-repeat: no-repeat;
    background-size: cover;
    background-position: center;
}
#devs {
    position: relative;
    display: block;
    width: 86%;
    margin: auto;
    padding: 25px;
}
 
#title{
    font-size: 3em;
    margin-top: 25px;
    color: steelblue;
}


</style>




