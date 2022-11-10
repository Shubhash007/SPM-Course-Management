<template>
    <NavBar :staffid="staffID" :userRole="userRole"></NavBar>
    <div style="padding-top: 150px; min-height: 85vh;">
        <div class="d-flex align-items-center justify-content-center">
            <div class="col-auto">
                <label for="staffID" class="col-form-label" id="spacing">Staff ID</label>
            </div>
            <div class="col-auto">
                <input type="text" v-model=staffID class="form-control" aria-describedby="roleNameLimit" maxlength="20">
            </div>
            <button type="button" class="btn login-button" @click.prevent="authenticate()">Login</button>
        </div>
    </div>
</template>
<script setup>
    import NavBar from '../components/NavBar.vue';
</script>
<script>
    import axios from "axios";
    export default{
        data(){
            return{
                staffID: "",
                userRole: 0
            }
        },
        computed:{
            authenticate:function(){
                let staffID = this.staffID;
                axios.get("/staff/" + staffID +'/')
                .then(response => {
                    let staffInfo = response.data; 
                    localStorage.setItem("userRole", staffInfo.User_Role);
                    localStorage.setItem("staff_id", staffInfo.Staff_ID)
                    this.userRole = localStorage.userRole;
                    this.staffID = localStorage.staff_id;
                    if (staffInfo.User_Role == 2 || staffInfo.User_Role == 4){
                        this.$router.push("/StartLJ");
                    }else if (staffInfo.User_Role == 1){
                        this.$router.push("/admin");
                    }else if (staffInfo.User_Role == 3){
                        this.$router.push("/Manager");
                    }
                })
                .catch(error=>{
                    console.log(error.message);
                })
            }
        }
    }
</script>
<style scoped>
    .login-button{
        color: white;
        background-color: #d8648b;
        margin: 10px;
    }

    .login-button:hover{
        color: black;
        background-color: #d8648b;
    }

    #spacing{
        padding-right: 42px;
    }

    .form-control{
        color: black;
        border-color: #d8648b;
        width: 300px;
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


</style>