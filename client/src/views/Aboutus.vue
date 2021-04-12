<template lang = "html">
    <div class="container">
        <h2 id = "title">{{title}}</h2>
        <div id = "devs">
            <DevCard 
                v-for = "([name, title, img, intro]) in devs" 
                :key = "name" 
                :devName = "name" 
                :devTitle = "title" 
                :devImg = "img" 
                :devIntro = "intro">
            </DevCard>
        </div>
    </div>
</template>

<script>
    import DevCard from '@/components/DevCard'

    export default {
        name: 'Aboutus',

        components: {DevCard},

        data(){
            return{
                // abhi_intro: "Self-motivated, creative, enthusiastic, passionate undergraduate student with an eagerness to progress, learn more in the field of Computer Science with proficient skill in C, C#, Java, Python, Ruby, Clojure, and CUDA C. A meticulous eye for perfection, with a strong desire to maintain the highest possible professional and ethical standards.",
                // ali_intro: "I am a double major in Computer Science and Psychology, graduating from Knox College in Fall of 2021. I'm currently inrolled in a UX Design program at the University of California at San Diego, hoping to start a career in UI/UX research, development, and design. I have 5 german shepards!",
                // drew_intro: "My name is Drew Friend, I am a intuitive programmer who is well versed in a variety of different languages, frameworks, and technologies.",
                // tris_intro: "I am an aspriring software developer and a Junior at Knox College, pursuing a Bachelors of Science in Computer Science. In addition to my studies, I have helped build multiple websites through squarespace and wordpress. In school I have built a few very simple projects using unity, and have accumulated a significant portion of code on GitHub. I also have more than five years of experience as a theatrical lighting technician, lighting board operator, and scenic carpenter.",
                devs: [
                    ["Abhishek", "SUPREME OVERLORD #1", "https://therealthaps.github.io/img/t.62ae5305.jpg", "Self-motivated, creative, enthusiastic, passionate undergraduate student with an eagerness to progress, learn more in the field of Computer Science with proficient skill in C, C#, Java, Python, Ruby, Clojure, and CUDA C. A meticulous eye for perfection, with a strong desire to maintain the highest possible professional and ethical standards."],
                    ["Ali", "SUPREME OVERLORD A", "https://asaadielhassan.github.io/hello-world/img/image.25ceb678.png", "I am a double major in Computer Science and Psychology, graduating from Knox College in Fall of 2021. I'm currently inrolled in a UX Design program at the University of California at San Diego, hoping to start a career in UI/UX research, development, and design. I have 5 german shepards!"],
                    ["Drew", "SUPREME OVERLORD 00", "https://avatars.githubusercontent.com/u/43389539?s=400&u=68c28d391e1a9f5b06c8457d9b0dd0daa6554e7c&v=4", "My name is Drew Friend, I am a intuitive programmer who is well versed in a variety of different languages, frameworks, and technologies."],
                    ["Tristan", "SUPREME OVERLORD I", "https://user-images.githubusercontent.com/71510797/112917605-a02b8e00-90c8-11eb-95c9-19a95e17e53a.jpg", "I am an aspriring software developer and a Junior at Knox College, pursuing a Bachelors of Science in Computer Science. In addition to my studies, I have helped build multiple websites through squarespace and wordpress. In school I have built a few very simple projects using unity, and have accumulated a significant portion of code on GitHub. I also have more than five years of experience as a theatrical lighting technician, lighting board operator, and scenic carpenter."],
                ],
                title: "Meet the Devs",
                
            }
        },

        mounted(){
            this.$refs.title.focus();
        }
    }

</script>

<style>
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