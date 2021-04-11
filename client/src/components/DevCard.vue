<template lang = "html">
    <div class = "card">
        <img class="portrait" :src="devImg"/>
        <h3> {{devName}} </h3>
        <h5> ::{{devTitle}}:: </h5>
        <p class="description">{{devIntro}}</p>
    </div>
</template>

<script>
    export default {
        name: 'DevCard',

        props: {
            devName: String ,
            devTitle: String, 
            devImg: String, 
            devIntro: String
        }

    }

</script>

<style scoped lang="css">
.card {
    display: block;
    min-height: 500px;
    margin-bottom: 100px;
    border-top: 7px #D0D7E1 dashed;
    background-color: #5B5756;
    color: #D0D7E1;
    padding: 35px;
    border-radius: 5%;
    padding-bottom: 55px;

}
.card h3{
    font-size: 2.5em;
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
