<template>
  <Navbar></Navbar>
  <div style="min-height: 82vh">
    <!-- Edit Learning Journeys -->
    <div class="row p-5" id="row">
      <div class="col-sm-6">
        <div class="card">
          <div class="card-body">
            <h5 class="card-title">Edit Learning Journey(s)</h5>
            <p class="card-text">Edit your existing Learning Journey(s).</p>
            <router-link class="btn" id="card-button" to="/EditLearningJourneys"
              >Edit</router-link
            >
          </div>
        </div>
      </div>
  
      <!-- Add Courses to LJ -->
      <div class="col-sm-6">
        <div class="card">
          <div class="card-body">
            <h5 class="card-title">Add courses</h5>
            <p class="card-text">
              Add courses to existing Learning Journey(s)
            </p>
            <router-link class="btn" id="card-button" to="/AddCourses"
              >Add  Courses</router-link
            >
          </div>
        </div>
      </div>
      
      <!-- View Staff -->
      <!-- <div class="col-sm-6">
        <div class="card">
          <div class="card-body">
            <h5 class="card-title">View Staff</h5>
            <p class="card-text">View staffs' skills and completed courses</p>
            <router-link class="btn" id="card-button" to="/ViewStaff">View Staff</router-link>
          </div>
        </div>
      </div> -->
    </div>
  </div>
</template>
<script setup>
  import Navbar from '../../components/NavBar.vue';
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

