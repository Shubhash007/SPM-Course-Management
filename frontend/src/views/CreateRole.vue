<template>
    <div class="card w-75">
        <div class="card-body">
            <!-- Create a Job Role -->
            <h5 class="card-title">CREATE A JOB ROLE</h5>
            <p class="card-text">
                <div class="row g-3 py-3 align-items-center">
                    <div class="col-auto">
                        <label for="jobRole" class="col-form-label" id="spacing">Job Role Name</label>
                    </div>
                    <div class="col-auto">
                        <input type="text" v-bind:id="jobRole" class="form-control" aria-describedby="roleNameLimit" maxlength="20">
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
            </p>
            
            <!-- Attach Skills to Role -->
            <h5 class="card-title">ATTACH SKILL(S)</h5>
            <p class="card-text">
                <div v-for="n in existingSkillCounter" class="row g-3 py-3 align-items-center">
                    <div class="col-auto">
                        <label for="Skill{{n}}" class="col-form-label" id="spacing2">Skill #{{n}}</label>
                    </div>
                    <div class="col-auto">
                        <select class="form-select select-skill" style="background-color: #2F2FFA; color:white;">
                            <option selected>Select an existing skill...</option>
                            <option value="1">One</option>
                            <option value="2">Two</option>
                            <option value="3">Three</option>
                        </select>
                    </div>
                    <div class="col-auto">
                        <button type="button" class="btn" style="color:white;" @click="AddExistingSkill()">+</button>
                        <button type="button" class="btn" style="color:white;" @click="RemoveExistingSkill()">-</button>
                    </div>
                </div>

                <div class="col-auto">
                    <button v-if="!hasNewSkill" href="#" class="btn skill-button" @click="AddNewSkill()">Add New Skill</button>
                    <h5 v-if="hasNewSkill" class="card-title" style="display: inline">ADD NEW SKILL(S)</h5>
                    <button type="button" class="btn" style="color:white; margin-left:65%" @click="AddNewSkill()">+</button>
                    <button type="button" class="btn" style="color:white;" @click="RemoveNewSkill()">-</button>
                </div>

                <div v-for="i in newSkillCounter">
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
                    <div class="row g-3 py-3 align-items-center">
                        <div class="col-auto">
                            <label for="jobDescription" class="col-form-label">Skill #{{i}} Description</label>
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
                </div>
            </p>

            <router-link to="/HRHome" class="btn next-button">Create</router-link>
        </div>
    </div>
</template>
<script>
    export default{
        data(){
            return{
                existingSkillCounter: 1,
                newSkillCounter: 0,
                hasNewSkill: false
            }
        }, 
        
        
        methods:{
            AddExistingSkill:function(){
                this.existingSkillCounter += 1;
            },
            RemoveExistingSkill:function(){
                if (this.existingRoleCounter != 1){
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
            }
        }
    }
</script>
<style scoped>
    /* Create Job Role */
    .card{
        margin: 10px auto;
    }

    .card-body{
        background-color: #2F2FFA;
        color: white;
        padding: 20px 35px;
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
    .skill-button{
        border-color: white;
        color: white;
    }

    .skill-button:hover{
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
