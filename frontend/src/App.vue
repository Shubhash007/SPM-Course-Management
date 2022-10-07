<template>
  <Navbar></Navbar>
  <router-view></router-view>
  <Footer></Footer>
</template>

<script setup>
import { RouterLink, RouterView } from "vue-router";
import Navbar from "@/components/NavBar.vue";
import Footer from "./components/Footer.vue";
</script>
