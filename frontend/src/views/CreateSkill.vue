<template>
    <div class="card w-75">
        <div class="card-body">
            <!-- Create a Skill -->
            <h5 class="card-title">CREATE A SKILL</h5>
            <p class="card-text">
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
                        <label for="Role{{n}}" class="col-form-label" id="spacing2">Role #{{n}}</label>
                    </div>
                    <div class="col-auto">
                        <select class="form-select select-skill" style="background-color: #2F2FFA; color:white;">
                            <option selected>Select an existing role...</option>
                            <option value="1">One</option>
                            <option value="2">Two</option>
                            <option value="3">Three</option>
                        </select>
                    </div>
                    <div class="col-auto">
                        <button type="button" class="btn" style="color:white;" @click="AddExistingRole()">+</button>
                        <button type="button" class="btn" style="color:white;" @click="RemoveExistingRole()">-</button>
                    </div>
                </div>

                <div class="col-auto">
                    <button v-if="!hasNewRole" href="#" class="btn role-button" @click="AddNewRole()">Add New Role</button>
                    <h5 v-if="hasNewRole" class="card-title" style="display: inline">ADD NEW ROLE(S)</h5>
                    <button type="button" class="btn" style="color:white; margin-left:65%" @click="AddNewRole()">+</button>
                    <button type="button" class="btn" style="color:white;" @click="RemoveNewRole()">-</button>
                </div>

                <div v-for="i in newSkillCounter">
                    <div class="row g-3 py-3 align-items-center">
                        <div class="col-auto">
                            <label for="roleName" class="col-form-label" id="spacing">Role #{{i}} Name</label>
                        </div>
                        <div class="col-auto">
                            <input type="text" v-bind:id="roleName" class="form-control" aria-describedby="roleNameLimit" maxlength="20">
                        </div>
                        <div class="col-auto">
                            <span id="roleNameLimit" class="form-text" style="color:white;">
                            Must be 3-20 characters long.
                            </span>
                        </div>
                    </div>
                    <div class="row g-3 py-3 align-items-center">
                        <div class="col-auto">
                            <label for="roleDescription" class="col-form-label">Role #{{i}} Description</label>
                        </div>
                        <div class="col-auto">
                            <textarea v-bind:id="roleDescription" class="form-control" aria-describedby="roleDescLimit"></textarea>
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
                existingRoleCounter: 1,
                newSkillCounter: 0,
                hasNewRole: false
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
