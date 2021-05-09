<template>
    <div class="grid-preview">
        <router-link :to="{name: 'Habit', params: { id: grid.id }}" class="image-area">
        </router-link>

        <router-link :to="{name:'Habit',params: { id: grid.id }}" class="body-area">
            <h3><slot></slot></h3>
            <p>

                <span>on {{ grid.start_Date }}</span>
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
    height: 150px;
    margin-bottom: 25px;
    display: block;
    color: black;
    display: grid;
    grid-template-columns: 3fr 1fr 15fr;
}


.body-area {
    color: black;
}

.blue-highlight {
    color: rgb(48, 99, 219);
}
</style>