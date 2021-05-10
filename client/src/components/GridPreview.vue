<template>
    <div class="grid-preview">
        <router-link :to="{name: 'Habit', params: { id: grid.id }}" class="image-area">
        </router-link>

        <router-link :to="{name:'Habit',params: { id: grid.id }}" class="body-area">
            <h3><slot></slot></h3>
            <p>

                <span>on {{ grid.string_start }}</span>
                <span v-show="!hideUser">&nbsp;by <span class="blue-highlight">u/{{ grid.user.username }}</span></span>
            </p>
            <p>{{ description }}</p>
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
            return this.grid.description.slice(0, 750) + '...'
        }
    }
}
</script>

<style css = scoped>
p {
    margin: 5px 0;
}

.grid-preview {
    text-align: left;
    height: 150px;
    margin-bottom: 25px;
    display: block;
    display: grid;
    grid-template-columns: 5fr 1fr 15fr;
}


.body-area {
    color: #3B4556;
    width: 650px;
    border: 7px double #3B4556;
    border-left: 16px outset rgba(235, 151, 102, 100);
    padding: 15px 25px 15px 25px;
    margin-top: 35px;
    background-color: #FDF2EC;
}
h3 {
    font-size: 1.32em;
    text-transform: uppercase;
    text-decoration: underline;
}
.blue-highlight {
    color: rgb(48, 99, 219);
}
</style>