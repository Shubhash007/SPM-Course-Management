import { createRouter, createWebHistory } from "vue-router";
import Login from "../views/Login.vue";
import CreateRole from "../views/admin/CreateRole.vue";
import HRHome from "../views/admin/HRHome.vue";
import ViewRoles from "../views/admin/ViewRoles.vue";
import CreateSkill from "../views/admin/CreateSkill.vue";
import StaffProfile from "../views/StaffProfile.vue";
import StaffStartLJ from "../views/staff/StaffStartLJ.vue"
import StaffHome from "../views/staff/StaffHome.vue";
import EditLearningJourneys from "../views/staff/EditLearningJourneys.vue";
import ViewStaff from "../views/manager/ViewStaff.vue";
import AddCourses from "../views/staff/AddCourses.vue";
import ViewSkills from "../views/admin/ViewSkills.vue";
import ManagerHome from "../views/manager/ManagerHome.vue";
import AssignCourse from "../views/admin/AssignCourse.vue";
import AssignRole from "../views/admin/AssignRole.vue";
import Account from "../views/Account.vue";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      component: Login,
      meta: { role: "" }
    },
    {
      path: "/admin",
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
      path: "/StaffProfile/:slug",
      name: 'StaffProfile',
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
      path: "/AddCourses",
      component: AddCourses,
    },
    {
      path: "/ViewSkills",
      component: ViewSkills,
    },
    {
      path: "/AssignCourse",
      component: AssignCourse,
    },
    {
      path: "/AssignRole",
      component: AssignRole,
    },
    {
      path: "/Manager",
      component: ManagerHome,
    },
    {
      path:'/Account',
      component: Account,
      
    }
  ],
});

export default router;