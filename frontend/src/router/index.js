import { createRouter, createWebHistory } from "vue-router";
import HomeView from "../views/HomeView.vue";
import CreateRole from "../components/CreateRole.vue";
import HRHome from "../components/HRHome.vue";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      name: "home",
      component: HomeView,
    },
    {
      path: "/about",
      name: "about",
      component: () => import("../views/AboutView.vue"),
    },
    {
      path: "/HRHome",
      component: HRHome,
    },
    {
      path: "/CreateRole",
      component: CreateRole,
    }
  ],
});

export default router;
