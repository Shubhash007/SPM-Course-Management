<template>
  <!-- Create Role / Skill -->
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

    <div class="col-sm-6">
      <div class="card">
        <div class="card-body">
          <h5 class="card-title">View Staff</h5>
          <p class="card-text">View staffs' skills and completed courses</p>
          <router-link class="btn" id="card-button" to="/ViewStaff"
            >View Staff</router-link
          >
        </div>
      </div>
    </div>
  </div>
</template>



<style scoped>
    #row{
        min-height: 80vh;
    }

    .card{
        border-color: #2F2FFA;
        color:black;
    }

    .card:hover{
        background-color: #ababb7;
        color:white;
    }

    #card-button{
        background-color: #F64C72;
        border-color: #F64C72;
        color: white;
    }

    #card-button:hover{
        background-color: #F64C72;
        color:black;
    }
</style>

