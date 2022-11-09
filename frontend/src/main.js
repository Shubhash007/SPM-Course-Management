import "bootstrap/dist/css/bootstrap.min.css";
import { createApp } from "vue";
import { createPinia } from "pinia";
import { library } from '@fortawesome/fontawesome-svg-core';
import { faPenToSquare } from '@fortawesome/free-solid-svg-icons';
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome';

library.add(faPenToSquare);

import App from "./App.vue";
import router from "./router";

import "./assets/main.css";
import "./assets/navbar.css";
import "./assets/hrhome.css";

const app = createApp(App);
app.component("font-awesome-icon", FontAwesomeIcon);

app.use(createPinia());
app.use(router);

app.mount("#app");

import "bootstrap/dist/js/bootstrap.js";