<template>
    <NavBar v-if="userRole == 1 || userRole == 3"></NavBar>
    <div class="card w-75" style="min-height: 80vh;" v-if="userRole == 1 || userRole == 3">
        <div class="card-body">
            <!-- Create a Skill -->
            <h5 class="card-title">Assign Role(s) to Skill</h5>
            
            <!-- List of Roles -->
            <p class="card-text">
                <div v-for="n in existingRoleCounter" class="row g-3 py-3 align-items-center">
                    <div class="col-auto">
                        <label for="Role{{n}}" class="col-form-label" id="spacing">Skills</label>
                    </div>
                    <div class="col-auto">
                        <select @change="appendSkillID" size="10" v-model="selectedSkills" class="form-select select-skill" style="background-color: #d8648b; color:white;" >
                            <option v-for="skill in skillList" :value="skill.Skill_ID">{{skill.Skill_Name}}</option>
                        </select>
                        Selected Skill: {{selectedSkills}}
                    </div>
                </div>
                </p>
                    
            <!-- Attach Courses to Skills -->

            <p class="card-text">
                <div v-for="n in existingRoleCounter" class="row g-3 py-3 align-items-center">
                    <div class="col-auto">
                        <label for="Course{{n}}" class="col-form-label" id="spacing">Roles</label>
                    </div>
                    <div class="col-auto">
                        <select @change="appendJobID" multiple size="10" v-model="selectedRoles" class="form-select select-skill" style="background-color: #d8648b; color:white;" >
                            <option v-for="job in jobsList" :value="job.Job_Role_ID">{{job.Job_Role_Name}}</option>
                        </select>
                        Selected Roles: {{selectedRoles}}
                    </div>
                    </div>
                </p>


            <!-- <button @click="postSkill">Create</button> -->
            <button @click="assignCourse" type="button" class="btn next-button">Create</button>
            <!-- <router-link to="/ViewSkills" class="btn next-button">Create</router-link> -->
        </div>
    </div>
    <Error v-else></Error>
</template>
<script setup>
    import axios from 'axios'
    import NavBar from '../../components/NavBar.vue';
    import Error from '../../components/Error.vue';
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
                courseIDList: [],
                skillList: [],
                userRole: 0,
                selectedSkills:["Please select skill"]
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
            this.userRole = localStorage.getItem("userRole")
            await axios.get('http://localhost:5000/job_role/')
            .then(response => {
                this.course = response.data.data;
                this.jobsList = response.data
                console.log(this.jobsList)

            })
            .catch(error => alert(error)) 


            await axios.get('http://localhost:5000/skill/')
            .then(response => {
                this.skillNo = response.data.length + 2
                this.skillList = response.data
                console.log(response.data)

            })
            .catch(error => alert(error)) 


        },
        assignCourse: async function() {
            console.log(this.selectedRoles)
            var exist = false
            for (const [key, value] of Object.entries(this.selectedRoles)) {
                await axios.get('http://localhost:5000/job_role/' + value + '/')
                .then(response => {
                    console.log(response.data)
                    console.log(response.data["Skills"])
                    // response.data["Skills"]
                    for (let i = 0; i < response.data["Skills"].length; i++) {
                        console.log(response.data["Skills"][i]["Skill_ID"])
                        if (response.data["Skills"][i]["Skill_ID"] == this.selectedSkills){
                            exist = true
                        }
                        }



                })
                .catch(error => error) 
                }
                console.log(exist)
                if (exist == false) {
                    for (const [key, value] of Object.entries(this.selectedRoles)){
                        await axios.post('http://localhost:5000/skill_to_job_role/' + this.selectedSkills + "/" + value + "/", {
                        })
                        .then(response => {
                        console.log(response.data) 
                        alert("Job Role successfully assigned to Skill")
                        location.reload();
                    })
                    .catch(error => alert(error))
                    }
                    }
                else {
                    alert("Assignment already exists")
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
        background-color: #d8648b;
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
        background-color: #d8648b;
        color: white;
        width: 500px;
    }

    .form-control:active{
        border-color: #f5b9c6c7;
    }

    .form-control:hover{
        border-color: #f5b9c6c7;
    }

    .form-control:focus{
        border-color: #f5b9c6c7;
    }

    .next-button{
        background-color: #f5b9c6c7;
        color: white;
        width: 10%;
    }

    .next-button:hover{
        background-color: #f5b9c6c7;
        color: black;
    }

    /* Attach Skill to Role */
    .role-button{
        border-color: white;
        color: white;
    }

    .role-button:hover{
        border-color: #f5b9c6c7;
        color: #f5b9c6c7;
    }

    #spacing2{
        padding-right: 100px;
    }
    
    .select-skill:hover{
        border-color: #f5b9c6c7;
    }
</style>
