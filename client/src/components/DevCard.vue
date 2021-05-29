<template lang = "html">
    <div class = "card">
        <img class="portrait" :src="devImg"/>
        <h3> {{devName}} </h3>
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
    width: 40%;
    border-bottom: 1px #aa5635 solid;
    border-top: 4px #aa5635 solid;
    border-left: 2px #6e3b27 solid;
    border-right: 2px #6e3b27 solid;
    background-color: rgb(212, 161, 116);
    color: rgb(136, 75, 22);
    padding: 35px;
    padding-bottom: 55px;
    margin: auto;

}
.card h3{
    margin-top: 20px;
    font-size: 20px;
}
.card p{
    margin-top: 20px;
}
.portrait{
    width: 90%;
    display: block;
    position: relative;
    margin:auto;

}
</style>
