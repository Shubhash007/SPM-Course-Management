<template>
  <nav class="navbar navbar-expand-lg">
    <div class="container-fluid">
      <a class="navbar-brand" href="#">
        <img id="LJMS-LOGO" src="../assets/LJMS_logo.jpg" alt="logo" width="60" height="50">
      </a>
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarSupportedContent">
        <ul class="navbar-nav me-auto mb-2 mb-lg-0">
          <li class="nav-item ms-5" v-if="userRole == 1">
            <router-link to="/admin" class="nav-link" aria-current="page">HOME</router-link>
          </li>
          <li class="nav-item ms-5" v-if="userRole == 2 || userRole == 4">
            <router-link to="/EditLearningJourneys" class="nav-link" aria-current="page">HOME</router-link>
          </li>
          <li class="nav-item ms-5" v-if="userRole == 3">
            <router-link to="/Manager" class="nav-link" aria-current="page">HOME</router-link>
          </li>
          <li class="nav-item ms-5" v-if="userRole == 2 || userRole == 4">
            <router-link to="StartLJ" class="nav-link" aria-current="page">START LEARNING JOURNEYS</router-link>
          </li>
          <li class="nav-item ms-5" v-if="userRole > 0">
            <router-link to="/Account" class="nav-link" aria-current="page">ACCOUNT</router-link>
          </li>
        </ul>
        <router-link to="/"><button type="button" class="btn btn-outline-primary navbar-button" id="navbar-signup" v-if="userRole > 0" @click.prevent="logout()">Log out</button></router-link>
      </div>
    </div>
  </nav>
</template>
<script>
  export default{
    data(){
      return{
        userRole: 0,
        pageStatus: true
      }
    },
    async created(){
      this.userRole = localStorage.getItem('userRole');
      console.log(this.userRole);
      if (this.userRole == 0){
        // window.location.reload();
      }
    },
    methods:{
      logout:function(){
        localStorage.clear();
        this.$router.push("/");
      }
    }
  }
</script>
