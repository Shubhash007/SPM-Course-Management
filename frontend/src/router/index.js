import { createRouter, createWebHistory } from "vue-router";
import Login from "../views/Login.vue";
import CreateRole from "../views/CreateRole.vue";
import HRHome from "../views/HRHome.vue";
import ViewRoles from "../views/ViewRoles.vue";
import CreateSkill from "../views/CreateSkill.vue";
import StaffProfile from "../views/StaffProfile.vue";
import StaffStartLJ from "../views/StaffStartLJ.vue"
import StaffHome from "../views/StaffHome.vue";
import EditLearningJourneys from "../views/EditLearningJourneys.vue";
import ViewStaff from "../views/ViewStaff.vue";
import RemoveCourse from "../views/RemoveCourse.vue";
import AddCourses from "../views/AddCourses.vue";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      component: Login,
      meta: { role: "" }
    },
    {
      path: "/HRHome",
      component: HRHome,
      meta: { role: "admin" }
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
    },
    {
      path: "/StartLJ",
      component: StaffStartLJ,
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
    {
      path: "/AddCourses",
      component: AddCourses,
    }
  ],
});

export default router;