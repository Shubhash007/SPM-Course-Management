import { createRouter, createWebHistory } from "vue-router";
import HomeView from "../views/HomeView.vue";
import CreateRole from "../views/CreateRole.vue";
import HRHome from "../views/HRHome.vue";
import ViewRoles from "../views/ViewRoles.vue";
import CreateSkill from "../views/CreateSkill.vue";
import StaffProfile from "../views/StaffProfile.vue";
import StaffStartLJ from "../views/StaffStartLJ.vue"
import StaffProfile from "../views/StaffProfile.vue";
import StaffHome from "../views/StaffHome.vue";
import EditLearningJourneys from "../views/EditLearningJourneys.vue";
import ViewStaff from "../views/ViewStaff.vue";
import RemoveCourse from "../views/RemoveCourse.vue";

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
    },
    {
      path: "/StaffProfile",
      component: StaffProfile,
    }
      path: "/StartLJ",
      component: StaffStartLJ,
      name: 'StartLJ'
    },
    {
      path: "/StaffProfile",
      component: StaffProfile,
    },
    {
      path: "/StaffHome",
      component: StaffHome,
    },
    {
      path: "/EditLearningJourneys",
      component: EditLearningJourneys,
    },
    {
      path: "/ViewStaff",
      component: ViewStaff,
    },
    {
      path: "/RemoveCourse",
      component: RemoveCourse,
    },
  ],
});

export default router;
