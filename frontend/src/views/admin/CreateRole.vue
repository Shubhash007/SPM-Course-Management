<template>
    <NavBar v-if="userRole == 1"></NavBar>
    <div class="card w-75" v-if="userRole == 1">
        <div class="card-body">
            <!-- Create a Job Role -->
            <h5 class="card-title">CREATE A JOB ROLE</h5>
            <span>* indicates required field</span>
            <br><br>
            <p class="card-text">
                <div class="row g-3 py-3 align-items-center">
                    <div class="col-auto">
                        <label for="jobRole" class="col-form-label" id="spacing">Job Role Name*</label>
                    </div>
                    <div class="col-auto">
                        <input  type="text" v-model="jobRole" class="form-control" aria-describedby="roleNameLimit" minlength="3" maxlength="20">
                    </div>
                    <div class="col-auto">
                        <span id="roleNameLimit" class="form-text" style="color:white;">
                        Must be 3-20 characters long.
                        </span>
                    </div>
                </div>
                <div class="row g-3 py-3 align-items-center">
                    <div class="col-auto">
                        <label for="jobDescription" class="col-form-label">Job Role Description*</label>
                    </div>
                    <div class="col-auto">
                        <textarea v-bind:id="jobDescription" class="form-control" aria-describedby="roleDescLimit" minlength="8" maxlength="100"></textarea>
                    </div>
                    <div class="col-auto">
                        <span id="roleDescLimit" class="form-text" style="color:white;">
                        Must be 8-100 characters long.
                        </span>
                    </div>
                </div>
                <div class="row g-3 py-3 align-items-center">
                    <div class="col-auto">
                        <label for="dept" class="col-form-label" id="spacing2">Department*</label>
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
                        <label for="Skill{{n}}" class="col-form-label" id="spacing">Skills*</label>
                    </div>
                    <div class="col-auto">
                        <span>*To add more than 1 skill, press control button on keyboard and click on the skill you want to add</span><br>
                        <select @change="appendSkillID" multiple size="10" v-model="selectedSkills" class="form-select select-skill" style="background-color: #d8648b; color:white;" >
                            <option v-for="skill in skillsList" :value="skill.Skill_ID">{{skill.Skill_Name}}</option>
                        </select>
                        Selected Skills: {{selectedSkills}}
                    </div>
                </div>
            </p>
            <!-- <button @click="postJobRole">Create</button> -->
            <button @click="postJobRole" type="button" class="btn next-button">Create</button>
            <!-- <router-link to="/HRHome" class="btn next-button" @click="postJobRole">Create</router-link> -->
        </div>
    </div>
    <Error v-else></Error>
</template>
<script setup>
    import NavBar from '../../components/NavBar.vue';
    import Error from '../../components/Error.vue';
</script>
<script>
    import axios from 'axios'
    export default{
        data(){
            return{
                existingSkillCounter: 1,
                newSkillCounter: 0,
                hasNewSkill: false,
                skillsList: [],
                selectedSkills: ["Please select skills"],
                skillIDList: [],
                roleNo: 0,
                userRole: 0,
                roleList: []
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

            appendSkillID:function(){
            this.skillIDList = []

            for (let i = 0; i < this.selectedSkills.length; i++) {

                for (let j = 0; j < this.skillsList.length; j++) {
                    // console.log(this.skillsList[j])
                if (this.skillsList[j].Skill_Name == this.selectedSkills[i]) {
                    this.skillIDList.push(this.skillsList[j].Skill_ID)
                }
            }
            }
            console.log(this.skillIDList)
            },
        
            onload: async function(){
                this.userRole = localStorage.getItem("userRole")
                await axios.get('/skill/')
            .then(response => {
                // this.course = response.data.data;
                this.skillsList = response.data
                console.log(this.skillsList)
            })
            .catch(error => alert(error)) 


            await axios.get('/job_role/')
            .then(response => {
                this.roleNo = response.data.length + 1
                this.roleList = response.data
                console.log(response.data)
            })
            .catch(error => alert(error)) 


            },
            postJobRole: async function() {
                var exist = false
                var Job_Role_ID = this.roleNo
                var Job_Role_Desc = document.getElementsByTagName("textarea")[0].value
                var Job_Role_Name = document.getElementsByTagName("input")[0].value
                var Dept = document.getElementsByTagName("input")[1].value
                var Skills = this.selectedSkills

                if (Job_Role_Name.length < 3 ||  Job_Role_Name.length > 20 || Dept.length == 0 || Job_Role_Desc.length < 8 || Job_Role_Desc.length > 100) {
                    alert("Please provide valid inputs!")
                    window.location.reload()
                }
                else {


                    var jobRoleName = document.getElementsByTagName("input")[0].value
                for (let i = 0; i < this.roleList.length; i++) {
                    if (this.roleList[i].Job_Role_Name == jobRoleName) {
                        var exist = true
                        }
                    }
            if (exist == false) {
            await axios.post('http://localhost:5000/job_role/', {
                Job_Role_ID: this.roleNo,
                Job_Role_Desc: document.getElementsByTagName("textarea")[0].value,
                Job_Role_Name: document.getElementsByTagName("input")[0].value,
                Dept: document.getElementsByTagName("input")[1].value,
                Skills: this.selectedSkills
            })

            

            .then(response => {
                this.course = response.data.data;
                console.log(response.data)
                console.log(this.selectedSkills)
                alert("Job Role successfully created")
                window.location.reload();
                
            })
            .catch(error => {
                alert(error)
                window.location.reload();
            }) 


            var jobID = this.roleNo
            for (let j = 0; j < this.skillIDList.length; j++) {
                let skillID = this.skillIDList[j]
                await axios.post('/skill_to_job_role/' + skillID + "/" + jobID + "/", {
                // "Job_Role_ID": jobID,
                // "Skill_ID": skillID
                })
                
                .then(response => {
                            console.log(response.data)
                            // alert("Skill successfully assigned to Job Role")
                // console.log(document.getElementsByTagName("input")[0].value)

                })
                .catch(error => alert(error))

            }
                }
                else {
                    alert("Role already exists")
                    window.location.reload();
                }







                }


        }

            
        },
        created() {
            this.onload()
        },
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
        padding-right: 35px;
    }

    #spacing1{
        padding-right: 96px;
    }

    #spacing2{
        padding-right: 55px;
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
    .skill-button{
        border-color: white;
        color: white;
    }

    .skill-button:hover{
        border-color: #f5b9c6c7;
        color: #f5b9c6c7;
    }
    
    .select-skill:hover{
        border-color: #f5b9c6c7;
    }
</style>
