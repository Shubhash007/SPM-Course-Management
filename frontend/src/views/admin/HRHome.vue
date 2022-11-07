<template>
  <NavBar></NavBar>
  <div style="min-height: 82vh">
    <!-- Create Role / Skill -->
    <div class="row p-5" id="row">
      <div class="col-sm-6">
        <div class="card">
          <div class="card-body">
            <h5 class="card-title">Create a New Role</h5>
            <p class="card-text">
              Input a new role into the system. You will not be able to create an
              existing role.
            </p>
            <router-link class="btn" id="card-button" to="/CreateRole"
              >Create Role</router-link
            >
          </div>
        </div>
      </div>



      <div class="col-sm-6">
        <div class="card">
          <div class="card-body">
            <h5 class="card-title">Create a New Skill</h5>
            <p class="card-text">
              Input a new skill into the system. You will not be able to create an
              existing skill.
            </p>
            <router-link class="btn" id="card-button" to="/CreateSkill"
              >Create Skill</router-link
            >
          </div>
        </div>
      </div>
  
      <!-- View Roles / Skills -->
      <div class="col-sm-6">
        <div class="card">
          <div class="card-body">
            <h5 class="card-title">View Roles</h5>
            <p class="card-text">
              View all roles to keep track of unfilled roles in the company
            </p>
            <router-link class="btn" id="card-button" to="/ViewRoles"
              >View Roles</router-link
            >
          </div>
        </div>
      </div>
  
          <!-- View Roles / Skills -->
          <div class="col-sm-6">
        <div class="card">
          <div class="card-body">
            <h5 class="card-title">View Skills</h5>
            <p class="card-text">
              View all skills to keep track of courses attached to it
            </p>
            <router-link class="btn" id="card-button" to="/ViewSkills"
              >View Skills</router-link
            >
          </div>
        </div>
      </div>



      
    </div>
  </div>
</template>
<script setup>
  import NavBar from '../../components/NavBar.vue';
</script>
<style scoped>
    #row{
        min-height: 80vh;
    }

    .card{
        border-color: #d8648b;
        color:black;
    }

    .card:hover{
        background-color: #d8648b;
        color:white;
    }

    #card-button{
        background-color: #f5b9c6c7;
        border-color: #f5b9c6c7;
        color: white;
    }

    #card-button:hover{
        background-color: #f5b9c6c7;
        color:black;
    }
</style>
