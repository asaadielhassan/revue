<template lang = "html">
    <div class = "card">
        <h3> {{taskName}} :: {{taskLength}} {{taskTimescale}} task :: {{taskCompletion}}% complete  </h3>
    </div>
</template>

<script>
    export default {
        name: 'TaskPreview',

        props: {
            taskName: String ,
            taskLength: Number, 
            taskTimescale: String,
            taskColor: String, 
            taskCompletion: Number
        }

    }

</script>

<style scoped lang="css">
.card {
    display: block;
    min-height: 150px;
    margin-bottom: 100px;
    border-top: 7px #D0D7E1 dashed;
    background-color: #5B5756;
    color: #D0D7E1;
    padding: 35px;
    border-radius: 5%;
    width: 70%;
    margin-left: 20%;
    padding-bottom: 55px;
    text-align: center;

}
.card h3{
    font-size: 2em;
    margin-top: 20px;
    text-decoration: underline overline;
}
.card h5{
    font-size: 1.55em;
}
.card p{
    margin-top: 40px;
    font-size: 1.35em;
}
.portrait{
    height: 500px;
    border-radius: 35%;
    display: block;
    position: relative;
    margin:auto;

}
</style>
