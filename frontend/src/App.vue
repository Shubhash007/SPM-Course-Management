<template>
  <router-view></router-view>
  <Footer></Footer>
</template>

<script setup>
import { RouterLink, RouterView } from "vue-router";
import Footer from "./components/Footer.vue";
</script>
