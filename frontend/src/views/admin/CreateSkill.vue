<template>
    <NavBar></NavBar>
    <div class="card w-75" style="min-height: 80vh;">
        <div class="card-body">
            <!-- Create a Skill -->
            <h5 class="card-title">CREATE A SKILL</h5>
            <p class="card-text">
                <!-- <div class="row g-3 py-3 align-items-center">
                    <div class="col-auto">
                        <label for="newSkillID" class="col-form-label" id="spacing">Skill ID</label>
                    </div>
                    <div class="col-auto">
                        <input type="text" v-bind:id="newSkill" class="form-control" aria-describedby="roleNameLimit" maxlength="20">
                    </div>
                    <div class="col-auto">
                        <span id="skillIDLimit" class="form-text" style="color:white;">
                        Must be 3-20 characters long.
                        </span>
                    </div>
                </div> -->

                <div class="row g-3 py-3 align-items-center">
                    <div class="col-auto">
                        <label for="newSkill" class="col-form-label" id="spacing">Skill Name</label>
                    </div>
                    <div class="col-auto">
                        <input type="text" v-bind:id="newSkill" class="form-control" aria-describedby="roleNameLimit" maxlength="20">
                    </div>
                    <div class="col-auto">
                        <span id="skillNameLimit" class="form-text" style="color:white;">
                        Must be 3-20 characters long.
                        </span>
                    </div>
                </div>

                <div class="row g-3 py-3 align-items-center">
                    <div class="col-auto">
                        <label for="skillDescription" class="col-form-label">Skill Description</label>
                    </div>
                    <div class="col-auto">
                        <textarea v-bind:id="skillDescription" class="form-control" aria-describedby="skillDescLimit"></textarea>
                    </div>
                    <div class="col-auto">
                        <span id="skillDescLimit" class="form-text" style="color:white;">
                        Must be 8-100 characters long.
                        </span>
                    </div>
                </div>
            </p>
            
            <!-- Attach Role to Skills -->

            <h5 class="card-title">ATTACH TO ROLE(S)</h5>
            <p class="card-text">
                <div v-for="n in existingRoleCounter" class="row g-3 py-3 align-items-center">
                    <div class="col-auto">
                        <label for="Role{{n}}" class="col-form-label" id="spacing">Roles</label>
                    </div>
                    <div class="col-auto">
                        <select @change="appendJobID" multiple size="10" v-model="selectedRoles" class="form-select select-skill" style="background-color: #2F2FFA; color:white;" >
                            <option v-for="job in jobsList" :value="job.Job_Role_Name">{{job.Job_Role_Name}}</option>
                        </select>
                        Selected Roles: {{selectedRoles}}
                    </div>
                </div>
                </p>
            

            <!-- Attach Courses to Skills -->

            <h5 class="card-title">ATTACH TO COURSES(S)</h5>
            <p class="card-text">
                <div v-for="n in existingRoleCounter" class="row g-3 py-3 align-items-center">
                    <div class="col-auto">
                        <label for="Course{{n}}" class="col-form-label" id="spacing">Courses</label>
                    </div>
                    <div class="col-auto">
                        <select @change="appendCourseID" multiple size="10" v-model="selectedCourses" class="form-select select-skill" style="background-color: #2F2FFA; color:white;" >
                            <option v-for="course in coursesList" :value="course.Course_Name">{{course.Course_Name}}</option>
                        </select>
                        Selected Courses: {{selectedCourses}}
                    </div>
                </div>
                </p>


            <button @click="postSkill">Create</button>
            <!-- <router-link to="/ViewSkills" class="btn next-button">Create</router-link> -->
        </div>
    </div>
</template>
<script setup>
    import axios from 'axios'
    import NavBar from '../../components/NavBar.vue';
</script>
<script>
    export default{
        data(){
            return{
                existingRoleCounter: 1,
                newSkillCounter: 0,
                hasNewRole: false,
                jobsList: [],
                selectedRoles: ["Please select roles"],
                jobIDList: [],
                skillNo: 0,
                coursesList: [],
                selectedCourses: ["Please select courses"],
                courseIDList: [],
                skillList: []

            }
        }, methods:{
            AddExistingRole:function(){
                this.existingRoleCounter += 1;
            },
            RemoveExistingRole:function(){
                if (this.existingRoleCounter != 1){
                    this.existingRoleCounter -= 1;
                }
            },
            AddNewRole:function(){
                this.newSkillCounter += 1;
                this.hasNewRole = true;
            },
            RemoveNewRole:function(){
                this.newSkillCounter -= 1;
                if (this.newSkillCounter == 0){
                    this.hasNewRole = false;
                }
            },



            appendCourseID:function(){
            this.courseIDList = []

            for (let i = 0; i < this.selectedCourses.length; i++) {

                for (let j = 0; j < this.coursesList.length; j++) {
                if (this.coursesList[j].Course_Name == this.selectedCourses[i]) {
                    this.courseIDList.push(this.coursesList[j].Course_ID)
                }
            }
            }
            console.log(this.courseIDList)
        },


        appendJobID:function(){
            this.jobIDList = []

            for (let i = 0; i < this.selectedRoles.length; i++) {

                for (let j = 0; j < this.jobsList.length; j++) {
                if (this.jobsList[j].Job_Role_Name == this.selectedRoles[i]) {
                    this.jobIDList.push(this.jobsList[j].Job_Role_ID)
                }
            }
            }
            console.log(this.jobIDList)
        },

            onload:async function(){

            await axios.get('http://localhost:5000/job_role/')
            .then(response => {
                this.course = response.data.data;
                this.jobsList = response.data

            })
            .catch(error => alert(error)) 


            await axios.get('http://localhost:5000/skill/')
            .then(response => {
                this.skillNo = response.data.length + 2
                this.skillList = response.data
                console.log(response.data)

            })
            .catch(error => alert(error)) 


            await axios.get('http://localhost:5000/course/')
            .then(response => {
                this.coursesList = response.data
                console.log(this.coursesList)

            })
            .catch(error => alert(error)) 


        },
        postSkill: async function() {
            // console.log(document.getElementsByTagName("input")[0].value)


            var exist = false
                var skillName = document.getElementsByTagName("input")[0].value
                for (let i = 0; i < this.skillList.length; i++) {


                    if (this.skillList[i].Skill_Name == skillName) {
                        var exist = true
                        }


                    }
            
            if (exist == false) {

                await axios.post('http://localhost:5000/skill/', {
                Skill_ID: this.skillNo,
                Skill_Name: document.getElementsByTagName("input")[0].value,
                Skill_Desc: document.getElementsByTagName("textarea")[0].value



            })

            .then(response => {
                // console.log(document.getElementsByTagName("input")[0].value)
                console.log(response.data)
                alert("Skill successfully created")
                
                
            })
            .catch(error => alert(error))

            var skillID = this.skillNo
            for (let j = 0; j < this.jobIDList.length; j++) {
                let jobID = this.jobIDList[j]
                await axios.post('http://localhost:5000/skill_to_job_role/' + skillID + "/" + jobID + "/", {
                // "Job_Role_ID": jobID,
                // "Skill_ID": skillID
                })

                .then(response => {
                // console.log(document.getElementsByTagName("input")[0].value)
                    console.log(response.data)
                    alert("Job Role successfully assigned to Skill")
                })
                .catch(error => alert(error))

            }



            var skillID = this.skillNo
            for (let j = 0; j < this.courseIDList.length; j++) {
                let courseID = this.courseIDList[j]
                await axios.post('http://localhost:5000/skill_to_course/' + skillID + "/" + courseID + "/", {
                // "Job_Role_ID": jobID,
                // "Skill_ID": skillID
                })

                .then(response => {
                // console.log(document.getElementsByTagName("input")[0].value)
                    console.log(response.data)
                    alert("Course successfully assigned to Skill")
                })
                .catch(error => alert(error))

            }
            }
            else {
                alert("Skill already exists")
            }






        }

        },
        created() {
            this.onload()
        }
        
        ,
        computed: {
    
    // a computed getter





        
    }

    }
</script>
<style scoped>
    /* Create Job Role */
    .card{
        margin: 10px auto;
        border-color: white;
    }

    .card-body{
        background-color: #2F2FFA;
        color: white;
        padding: 20px 35px;
        border-radius: 10px;
    }

    .card-title{
        padding: 10px 0px;
    }

    #spacing{
        padding-right: 42px;
    }

    .form-control{
        background-color: #2F2FFA;
        color: white;
        width: 500px;
    }

    .form-control:active{
        border-color: #F64C72;
    }

    .form-control:hover{
        border-color: #F64C72;
    }

    .form-control:focus{
        border-color: #F64C72;
    }

    .next-button{
        background-color: #F64C72;
        color: white;
        width: 10%;
    }

    .next-button:hover{
        background-color: #F64C72;
        color: black;
    }

    /* Attach Skill to Role */
    .role-button{
        border-color: white;
        color: white;
    }

    .role-button:hover{
        border-color: #F64C72;
        color: #F64C72;
    }

    #spacing2{
        padding-right: 100px;
    }
    
    .select-skill:hover{
        border-color: #F64C72;
    }
</style>
