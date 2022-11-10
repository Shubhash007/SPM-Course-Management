<template>
    <NavBar v-if="userRole == 3"></NavBar>
    <div style="min-height: 82vh" v-if="userRole == 3">
        <div class="row p-5" id="row">
            <!--Create Role-->
            <div class="col-sm-6">
                <div class="card" id="card">
                <div class="card-body">
                    <h5 class="card-title">Create a New Role</h5>
                    <p class="card-text">
                    Input a new role into the system. You will not be able to create an
                    existing role.
                    </p>
                    <router-link class="btn" id="card-button" to="/CreateRole"
                    >Create Role</router-link
                    >
                </div>
                </div>
            </div>
        
            <!-- View Staff -->
            <div class="col-sm-6">
                <div class="card" id="card">
                    <div class="card-body">
                        <h5 class="card-title">View Staff</h5>
                        <p class="card-text">View staffs' profile</p>
                        <router-link class="btn" id="card-button" to="/ViewStaff">View Staff</router-link>
                    </div>
                </div>
            </div>

            <!-- View Roles -->
            <div class="col-sm-6">
                <div class="card" id="card">
                    <div class="card-body">
                        <h5 class="card-title">View Roles</h5>
                        <p class="card-text">
                            View all roles to keep track of roles in the company
                        </p>
                        <router-link class="btn" id="card-button" to="/ViewRoles"
                            >View Roles</router-link
                        >
                    </div>
                </div>
            </div>
    
            <!-- View Skills -->
            <div class="col-sm-6">
                <div class="card" id="card">
                    <div class="card-body">
                    <h5 class="card-title">View Skills</h5>
                    <p class="card-text">
                        View all skills to keep track of courses attached to it
                    </p>
                    <router-link class="btn" id="card-button" to="/ViewSkills"
                        >View Skills</router-link
                    >
                    </div>
                </div>
            </div>

            <!-- Assign existing role to existing skill -->
            <div class="col-sm-6">
                <div class="card" id="card">
                <div class="card-body">
                    <h5 class="card-title">Assign role</h5>
                    <p class="card-text">
                    Assign existing role to existing skill 
                    </p>
                    <router-link class="btn" id="card-button" to="/AssignRole"
                    >Assign Role</router-link
                    >
                </div>
                </div>
            </div>
        </div>
    </div>
    <Error v-else></Error>
</template>
<script setup>
    import NavBar from '../../components/NavBar.vue';
    import Error from '../../components/Error.vue';
</script>
<script>
    export default{
        data(){
        return{
            userRole: 0
        }
        },
        methods:{
        onload: async function(){
            this.userRole = localStorage.getItem('userRole');
        }
        },
        created(){
        this.onload();
        }
    }
</script>
<style scoped>
    #row{
        min-height: 80vh;
    }

    #card{
        border-color: #d8648b;
        color:black;
        margin-bottom: 20px;
    }

    #card:hover{
        background-color: #d8648b;
        color:white;
    }

    #card-button{
        background-color: #f5b9c6c7;
        border-color: #f5b9c6c7;
        color: white;
    }

    #card-button:hover{
        background-color: #f5b9c6c7;
        color:black;
    }
</style>
