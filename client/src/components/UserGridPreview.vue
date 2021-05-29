<template>
  <router-link :to="{ name: 'Habit', params: { id: grid.id } }">
    <h3><slot></slot></h3>
    <p>{{ description }}</p>
  </router-link>
</template>

<script>
export default {
  name: "user-grid-preview",

  props: {
    grid: {},
    hideUser: {
      default: false,
    },
  },

  computed: {
    description() {
      return this.grid.description.slice(0, 750);
    },
  },
};
</script>

<style scoped>
</style>