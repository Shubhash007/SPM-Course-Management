<template>
    <div class="card w-75">
        <div class="card-body">
            <!-- Create a Job Role -->
            <h5 class="card-title">CREATE A JOB ROLE</h5>
            <p class="card-text">
                <div class="row g-3 py-3 align-items-center" >
                    <div class="col-auto">
                        <label for="jobID" class="col-form-label" id="spacing1">Job ID</label>
                    </div>
                    <div class="col-auto">
                        <input type="number" v-model="jobID" class="form-control">
                    </div>
                    <div class="col-auto">
                    </div>
                </div>
                <div class="row g-3 py-3 align-items-center">
                    <div class="col-auto">
                        <label for="jobRole" class="col-form-label" id="spacing">Job Role Name</label>
                    </div>
                    <div class="col-auto">
                        <input type="text" v-model="jobRole" class="form-control" aria-describedby="roleNameLimit" maxlength="20">
                    </div>
                    <div class="col-auto">
                        <span id="roleNameLimit" class="form-text" style="color:white;">
                        Must be 3-20 characters long.
                        </span>
                    </div>
                </div>
                <div class="row g-3 py-3 align-items-center">
                    <div class="col-auto">
                        <label for="jobDescription" class="col-form-label">Job Role Description</label>
                    </div>
                    <div class="col-auto">
                        <textarea v-bind:id="jobDescription" class="form-control" aria-describedby="roleDescLimit"></textarea>
                    </div>
                    <div class="col-auto">
                        <span id="roleDescLimit" class="form-text" style="color:white;">
                        Must be 8-100 characters long.
                        </span>
                    </div>
                </div>
                <div class="row g-3 py-3 align-items-center">
                    <div class="col-auto">
                        <label for="dept" class="col-form-label" id="spacing2">Department</label>
                    </div>
                    <div class="col-auto">
                        <input type="text" v-model="dept" class="form-control">
                    </div>
                    <div class="col-auto">
                    </div>
                </div>
            </p>
            
            <!-- Attach Skills to Role -->
            <h5 class="card-title">ATTACH SKILL(S)</h5>
            <p class="card-text">
                <div v-for="n in existingSkillCounter" class="row g-3 py-3 align-items-center">
                    <div class="col-auto">
                        <label for="Skill{{n}}" class="col-form-label" id="spacing">Skills</label>
                    </div>
                    <div class="col-auto">
                        <select multiple size="10" v-model="selectedSkills" class="form-select select-skill" style="background-color: #2F2FFA; color:white;" >
                            <option v-for="skill in skillsList" :value="skill.Skill_Name">{{skill.Skill_Name}}</option>
                        </select>
                        Selected Skills: {{selectedSkills}}
                    </div>

                    <!-- <div class="col-auto">
                        <button type="button" class="btn" style="color:white;" @click="AddExistingSkill()">+</button>
                        <button type="button" class="btn" style="color:white;" @click="RemoveExistingSkill()">-</button>
                    </div> -->
                </div>

                <!-- <div class="col-auto">
                    <button v-if="!hasNewSkill" href="#" class="btn skill-button" @click="AddNewSkill()">Add New Skill</button>
                    <h5 v-if="hasNewSkill" class="card-title" style="display: inline">ADD NEW SKILL(S)</h5>
                    <button type="button" class="btn" style="color:white; margin-left:65%" @click="AddNewSkill()">+</button>
                    <button type="button" class="btn" style="color:white;" @click="RemoveNewSkill()">-</button>
                </div> -->

                <!-- <div v-for="i in newSkillCounter">
                    <div class="row g-3 py-3 align-items-center">
                        <div class="col-auto">
                            <label for="skillName" class="col-form-label" id="spacing">Skill #{{i}} Name</label>
                        </div>
                        <div class="col-auto">
                            <input type="text" v-bind:id="skillName" class="form-control" aria-describedby="skillNameLimit" maxlength="20">
                        </div>
                        <div class="col-auto">
                            <span id="skillNameLimit" class="form-text" style="color:white;">
                            Must be 3-20 characters long.
                            </span>
                        </div>
                    </div>
                </div> -->
            </p>
            <button @click="postJobRole">Create</button>
            <!-- <router-link to="/HRHome" class="btn next-button" @click="postJobRole">Create</router-link> -->
        </div>
    </div>
</template>
<script>

    import axios from 'axios'
    export default{
        data(){
            return{
                existingSkillCounter: 1,
                newSkillCounter: 0,
                hasNewSkill: false,
                skillsList: [],
                selectedSkills: ["Please select skills"]
            }
        },

        
        
        methods:{
            AddExistingSkill:function(){
                this.existingSkillCounter += 1;
            },
            RemoveExistingSkill:function(){
                if (this.existingSkillCounter != 1){
                    this.existingSkillCounter -= 1;
                }
            },
            AddNewSkill:function(){
                this.newSkillCounter += 1;
                this.hasNewSkill = true;
            },
            RemoveNewSkill:function(){
                this.newSkillCounter -= 1;
                if (this.newSkillCounter == 0){
                    this.hasNewSkill = false;
                }
            },

            onload:function(){
                axios.get('/skill')
            .then(response => {
                this.course = response.data.data;
                this.skillsList = response.data
                console.log(this.skillsList)

                
            })
            .catch(error => alert(error)) 
            }
        },


        created() {
            this.onload()
        },



        computed: {
    
    // a computed getter
        postJobRole() {
            var jobID = document.getElementsByTagName("input")[0].value
            axios.post('/job_role/' + jobID, {
                "Job_Role_ID": jobID,
                "Job_Role_Desc": document.getElementsByTagName("textarea")[0].value,
                "Job_Role_Name": document.getElementsByTagName("input")[1].value,
                "Dept": document.getElementsByTagName("input")[2].value,
                "Skills": this.selectedSkills
            })
            .then(response => {
                this.course = response.data.data;
                console.log(response.data)
                console.log(this.selectedSkills)
                
            })
            .catch(error => alert(error)) 
        }
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
        padding-right: 35px;
    }

    #spacing1{
        padding-right: 96px;
    }

    #spacing2{
        padding-right: 55px;
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
    .skill-button{
        border-color: white;
        color: white;
    }

    .skill-button:hover{
        border-color: #F64C72;
        color: #F64C72;
    }
    
    .select-skill:hover{
        border-color: #F64C72;
    }
</style>
