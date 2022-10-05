import { createRouter, createWebHistory } from "vue-router";
import HomeView from "../views/HomeView.vue";
import CreateRole from "../views/CreateRole.vue";
import HRHome from "../views/HRHome.vue";
import ViewRoles from "../views/ViewRoles.vue";
import CreateSkill from "../views/CreateSkill.vue";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      name: "home",
      component: HomeView,
    },
    {
      path: "/HRHome",
      component: HRHome,
    },
    {
      path: "/CreateRole",
      component: CreateRole,
    },
    {
      path: "/ViewRoles",
      component: ViewRoles,
    },
    {
      path: "/CreateSkill",
      component: CreateSkill,
    }

  ],
});

export default router;
