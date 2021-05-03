<template lang="html">
  <div class="create-post container">
    <h1>Make a Grid</h1>
    <form @submit.prevent="create" enctype="multipart/form-data">
      <p class="error">{{ error }}</p>
      <input v-model="name" type="text" placeholder="Grid Name" ref="title">
      <input v-model="days" type="number" placeholder="Number of days">
      <label for="pub1"> Should this grid be public?</label>
      <input v-model="pub1" style="display: inline" name="pub1" type="checkbox">
       
       
      <textarea v-model="description" name="name" placeholder="Description" rows="10" cols="80"></textarea>
      <input class="button" type="submit" value="Build My Grid!">
    </form>
  </div>
</template>

<script>
import HabitsService from '@/services/HabitsService'

export default {
    name: 'create-task',

    data() {
        return {
            name: '',
            days: 0,
            description: '',
            pub1: false,
            username: this.$route.params.username,
            error: null,
        }
    },
    watch: {
        $route() {
            this.username = this.$route.params.username
            this.fetchData()
        }
    },


    methods: {
   
        create() {

            // HabitsService.create({
            //     name: this.name,
            //     num_Days: this.days,
            //     description: this.description,
            //     is_public: this.pub1,
            // }
            var formData = new FormData();
            formData.append('name', this.name)
            formData.append('num_Days', this.days)
            formData.append('is_public', this.pub1)
            formData.append('description', this.description)
            console.log(formData)

            HabitsService.create(formData)
                .then(response => {
                     this.$router.push({
                         name: 'Habit',
                         params: {username: response.data.username}
                     })
                })
                .catch(error => {
                    this.error = error.response.data.error
                })
        },



        fileChanged(e) {
            this.image = e.target.files[0]

            // Show image preview
            var reader = new FileReader();
            reader.onload = (e) => {
                this.imagePreview = e.target.result;
            };
            reader.readAsDataURL(this.image);
        }
    },

    mounted() {
        // Focus title
        this.$refs.title.focus();
    }
}
</script>

<style scoped lang="css">

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
</style>
