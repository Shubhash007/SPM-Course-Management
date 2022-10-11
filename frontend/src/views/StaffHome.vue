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

    <!-- View Roles / Skills -->
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

    <div class="col-sm-6">
      <div class="card">
        <div class="card-body">
          <h5 class="card-title">View Staff</h5>
          <p class="card-text">View staffs' skills and completed courses</p>
          <router-link class="btn" id="card-button" to="/ViewStaff">View Staff</router-link>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
</script>
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

