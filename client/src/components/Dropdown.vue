<template>
  <div class="menu-item" @click="isOpen = !isOpen">
    <a href="#">
      <!-- {{ title }} -->
      Subvue
    </a>
    <svg viewBox="0 0 1030 638" width="10">
      <path
        d="M1017 68L541 626q-11 12-26 12t-26-12L13 68Q-3 49 6 24.5T39 0h952q24 0 33 24.5t-7 43.5z"
        fill="#FFF"
      ></path>
    </svg>
    <transition name="fade" appear>
      <div class="sub-menu" v-if="isOpen">
        <router-link
          v-for="subvue in $store.state.subscribedSubvues"
          :key="subvue.permalink" class = "menu-item"
          :to="{ name: 'Subvue', params: { name: subvue.permalink } }"
          >{{ subvue.name }}</router-link
        >
        <router-link class="menu-item" :to="{ name: 'CreateSubvue' }"
          >Create a Subvue</router-link
        >
      </div>
    </transition>
  </div>
</template>

<script>
export default {
  name: "dropdown",
  //   props: ['title', 'items'],
  data() {
    return {
      isOpen: false,
    };
  },
};
</script>

<style>
nav .menu-item svg {
  width: 10px;
  margin-left: 10px;
}
nav .menu-item .sub-menu {
  position: absolute;
  background-color: rgb(243, 175, 136);
  top: calc(100% + 8px);
  left: 50%;
  transform: translateX(-50%);
  width: max-content;
  border-radius: 0px 0px 16px 16px;
}
.fade-enter-active,
.fade-leave-active {
  transition: all 0.2s ease-out;
}
.fade-enter,
.fade-leave-to {
  opacity: 0;
}
</style>