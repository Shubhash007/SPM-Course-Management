import "bootstrap/dist/css/bootstrap.min.css";
import { createApp } from "vue";
import { createPinia } from "pinia";

import App from "./App.vue";
import router from "./router";
import Vuex from "vuex";

import "./assets/main.css";
import "./assets/navbar.css";
import "./assets/hrhome.css";

const app = createApp(App);

app.use(createPinia());
app.use(router);
app.use(Vuex);

app.mount("#app");

import "bootstrap/dist/js/bootstrap.js";
