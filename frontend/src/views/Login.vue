<template>
    <div style="padding-top: 150px;">
        <div class="d-flex align-items-center justify-content-center">
            <div class="col-auto">
                <label for="staffID" class="col-form-label" id="spacing">Staff ID</label>
            </div>
            <div class="col-auto">
                <input type="text" v-model="staffID" class="form-control" aria-describedby="roleNameLimit" maxlength="20">
            </div>
            <router-link to="/StaffHome"><button type="button" class="btn login-button" @click="authenticate()">Login</button></router-link>
        </div>
    </div>
</template>
<script>
    export default{
        data(){
            return{
                staffID: "",
            }
        },
        methods:{
            authenticate(){

            }
        }
    }
</script>
<style scoped>
    .login-button{
        color: white;
        background-color: #2F2FFA;
        margin: 10px;
    }

    .login-button:hover{
        color: black;
        background-color: #2F2FFA;
    }

    #spacing{
        padding-right: 42px;
    }

    .form-control{
        color: black;
        border-color: #2F2FFA;
        width: 300px;
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


</style>