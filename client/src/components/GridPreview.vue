<template>
    <div class="grid-preview"
        @mouseover="hover = true"
        @mouseleave="hover = false"
    >

        <router-link :to="{name:'Habit',params: { id: grid.id }}" class="body-area">
            <div class="column">
            <h3><slot></slot></h3>
            <p>

                <span>Create on {{ grid.string_start }}</span>
                <span v-show="!hideUser">&nbsp;by <span class="blue-highlight">@{{ grid.user.username }}</span></span>
            </p>
            </div>
            <div class="column pullr">
                <p>{{ description }}</p>
            </div>
        </router-link>
    </div>
</template>

<script>
export default {
    name: 'grid-preview',

    props: {
        grid: {},
        hideUser: {
            default: false
        }
    },

    computed: {
        description() {
            return this.grid.description.slice(0, 150) + '...'
        }
    }
}
</script>

<style scoped>
p {
    margin: 5px 0;
}

.grid-preview {
    margin-left: 19%;
    text-align: center;
    height: 200px;
    margin-bottom: 25px;
    display: grid;
    grid-template-columns: 9fr 24fr 9fr;
}


.body-area {
    color: #3B4556;
    border: 7px solid #3B4556;
    border-left: 16px outset #eea073;
    padding: 15px 25px 15px 25px;
    margin-top: 35px;
    width: 650px;
    text-align: left;
    background-color: #FDF2EC;
}
.column {
    width: 50%;
    display: inline-block;
}
.pullr {
    display: inline-block;
    text-align: right;
    word-wrap: break-word;
}
h3 {
    font-size: 1.32em;
    text-transform: uppercase;
    text-decoration: underline;
}
.blue-highlight {
    color: rgb(48, 99, 219);
}
.grid-preview :hover {
  background: #eea073;
  transition: all 0.1s ease-in-out;
}
</style>