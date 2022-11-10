<template>
    <!-- Edit Role Button that triggers Modal -->
    <button type="button" class="btn edit-button" data-bs-toggle="modal" :data-bs-target="'#role'+roleId" @click.prevent="populate()">Edit Role</button>

    <!-- EditRoleDetails Modal -->
    <div class="modal fade" :id="role+roleId" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" aria-labelledby="staticBackdropLabel" aria-hidden="true">
    <div class="modal-dialog">
        <div class="modal-content">
        <div class="modal-header">
            <h1 class="modal-title fs-5" id="staticBackdropLabel" style="margin-top: 0px; color:#d8648b;">Edit Role</h1>
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
        </div>
        <div class="modal-body">
            <div class="mb-3">
                <label for="roleName" class="form-label">Role Name</label>
                <input type="text" class="form-control" id="roleName" placeholder="Enter Role Name"  v-model="roleName">
                <p v-show="hasErrors" class="error-message">{{ errorMessage }}</p>
            </div>
            <div class="mb-3">
                <label for="deptName" class="form-label">Department Name</label>
                <input type="text" class="form-control" id="deptName" placeholder="Enter Department Name"  v-model="departmentName">
            </div>
            <div class="mb-3">
                <label for="exampleFormControlTextarea1" class="form-label">Role Description</label>
                <textarea class="form-control" id="exampleFormControlTextarea1" rows="3" v-model="roleDescription"></textarea>
            </div>
        </div>
        <div class="modal-footer">
            <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
            <button type="button" class="btn btn-primary save-changes" @click="editRoles()">Save changes</button>
        </div>
        </div>
    </div>
    </div>
</template>
<script setup>
    const props = defineProps({
        roleId: Number,
        currentRoleName: String
    })    
</script>
<script>
    import axios from "axios";
    export default{
        data(){
            return{
                roleName: "",
                roleDescription: "",
                departmentName: "",
                hasErrors: false,
                errorMessage: "",
                role: "role",
                allRoles: []
            }
        },
        methods:{
            editRoles:function(){
                var duplicateCount = 0;
                for (let role of this.allRoles){
                    if (role.Job_Role_Name == this.roleName && this.roleName != this.props.currentRoleName){
                        duplicateCount += 1;
                    }
                }
                console.log(duplicateCount);
                if (this.roleName.length > 3 && this.roleName.length < 20 && duplicateCount == 0){
                    this.hasErrors = false;
                    this.errorMessage = "";
                    axios.put("/job_role/" + this.props.roleId + "/", {
                        "Job_Role_Name": this.roleName,
                        "Job_Role_Desc": this.roleDescription,
                        "Dept": this.departmentName
                    })
                    .then(response => {
                        console.log(response.data);
                        console.log(this.roleName);
                    })
                    .catch(error =>{
                        console.log(error.message);
                    }) 
                }else if (duplicateCount > 0){
                    this.hasErrors = true;
                    this.errorMessage = "Edited role name already exists";
                }else{
                    this.hasErrors = true;
                    this.errorMessage = "Edited role name has to be more than 3 and less than 20 characters";
                }
                location.reload();
            },
            populate:function(){
                axios.get("/job_role/" + this.props.roleId + "/")
                .then(response => {
                    let roleInfo = response.data;
                    this.roleName = roleInfo.Job_Role_Name;
                    this.roleDescription = roleInfo.Job_Role_Desc;
                    this.departmentName = roleInfo.Dept;
                })
                .catch(error=>{
                    console.log(error.message);
                })

                axios.get("/job_role/")
                .then(response => {
                    this.allRoles = response.data;
                    console.log(this.allRoles);
                })
                .catch(error => {
                    console.log(error.message);
                })
            }
        }
    }
</script>
<style scoped> 
    .edit-button{
        margin: -0.5rem -4rem;
        scale: 0.7;
        border-color:#f5b9c6c7;
        background-color:#f5b9c6c7;
        color: white;
    }

    .btn:first-child:hover , :not(.btn-check)+.btn:hover{
        border-color:#f5b9c6c7;
        background-color:#f5b9c6c7;
        color: black;
    }

    .error-message{
        color: red;
        font-size: small;
    }

    .save-changes{
        background-color: #f5b9c6c7;
        border-color: #f5b9c6c7;
        color: white;
    }

    #close-button:hover{
        background-color: black;
        border-color: black;
        color: white;
    }

    .modal-open {
        position: fixed;
        overflow: scroll;
        width: 100%;
        padding-right: 0!important;
    }
</style>