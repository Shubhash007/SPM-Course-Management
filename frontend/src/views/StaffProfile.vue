<template>
    <NavBar></NavBar>
    <div style="min-height: 80vh">
        <div class="card w-75">
            <div class="card-body">
    
                <!-- <h1 class="card-title">{{staffProfile.Staff_ID}}</h1> -->
                <h6 style="font-size: 20px">{{staffProfile.Staff_FName}} {{staffProfile.Staff_LName}}</h6>
                <br>
    
                <div class="row">
                    <div class="col-sm">
                    <h5 class="card-title">Staff Particulars</h5>
                    <p class="card-text">
                        <ul>
                            <li>Staff ID: {{staffProfile.Staff_ID}}</li>
                            <li>Department: {{staffProfile.Dept}}</li>
                        </ul>
                    </p>
                    </div>
                    
                    <div class="col-sm">
                    <h5 class="card-title">Skills Attained</h5>
                    <p class="card-text">
                        <ul>
                            <li v-for="skill in skillsList">{{skill.Skill_Name}}
                            </li>
                        </ul>
                    </p>
                    </div>


                    <div class="col-sm">
                    <h5 class="card-title">Current LJ Roles</h5>
                    <p class="card-text">
                        <ul>
                            <li v-for="role in currentRoles">{{role["Job_Role"]["Job_Role_Name"]}}
                            </li>
                        </ul>
                    </p>
                    </div>

                </div>



            </div>
        </div>
    </div>
</template>
<script>
import editRolesModal from '../components/admin/editRolesModal.vue';
import NavBar from '../components/NavBar.vue';
import axios from "axios";
export default {
    data() {
        return {
            employees:[],
            userRole: 0,
            staffProfile: [],
            skillsList: [],
            currentRoles: []
        };
    },
    methods: {
        // staffProfile:function(x){
        //   // console.log(x)
        //   sessionStorage.setItem("staffID", x);
        // },


        onload: async function(){
            this.userRole = localStorage.getItem("userRole")
            var staffID = sessionStorage.getItem('staffID')
            // console.log(staffID)
            // console.log(this.userRole)

            await axios.get('/staff/' + staffID + "/")
            .then(response => {
                this.staffProfile = response.data
                console.log(this.staffProfile)
            })
            .catch(error => alert(error)) 


            await axios.get('/skill_attained/' + staffID + "/")
            .then(response => {
                // console.log(response.data)
                for (let i = 0; i < response.data.length; i++){
                    this.skillsList = response.data[i]['Skills']
                }
                console.log(this.skillsList)
            })
            .catch(error => alert(error)) 

            await axios.get(' http://localhost:5000/req/' + staffID + "/")
            .then(response => {
                console.log(response.data)
                this.currentRoles = response.data
            })
            .catch(error => error)  








          
            },
    },


    mounted(){
      this.onload()
    },
    created() {
      this.onload()
    },
    // created(){
    //   this.userAuthentication()
    // },
    components: { NavBar }
};

</script>

<style scoped>
    .card{
        margin: 10px auto;
        border-color: white;
    }

    .card-body{
        background-color: #d8648b;
        color: white;
        padding: 70px;
        border-radius: 10px;
        border-top: 50px;
    }

    .card-title{
        padding: 10px 0px;
    }
    
    .col-auto{
        display: inline-block;
        margin-right: 15%;
    }

    .title-header{
        font-size: 1rem;
        color: #f5b9c6c7;
    }
    
    h5{
        color: #f5b9c6c7;
    }

    #spacing{
        padding-right: 42px;
    }
</style>
