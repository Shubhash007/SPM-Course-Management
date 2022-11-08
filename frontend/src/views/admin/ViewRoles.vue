<template>
    <NavBar v-if="userRole == 1 || userRole == 3"></NavBar>
    <div style="min-height: 80vh;" v-if="userRole == 1 || userRole == 3">
        <div class="row g-3" style="margin: 20px 50px;">
            <div class="col-auto">
                <label for="search" class="visually-hidden">Search</label>
                <input type="text" @keyup="searchFunction" v-model="keyword" class="form-control search-textbox" id="search" placeholder="Search by...">
            </div>
        </div>
        <table class="table table-responsive" style="width: 75%; border-color: #d8648b; margin: 20px 60px;" border="#d8648b">
            <thead>
                <tr>
                <th scope="col">S/N</th>
                <th scope="col">Role Name</th>
                <th></th>
                </tr>
            </thead>
            <tbody id="tbody">
                <tr v-for="(jobRoles, index) in jobRoles">
                    <th scope="row" style="color: #d8648b">{{index+1}}</th>
                    <td>{{ jobRoles.Job_Role_Name}}</td>
                    <!-- <td><router-link :to="{name: 'StaffProfile', params: {slug: employee.StaffID}}">{{ employee.Staff }}</router-link></td> -->
                    <!-- <td>{{ jobRoles.Skills.toString()}}</td>  -->
                    <td><button type="button" id="edit" class="btn" @click="deleteRole(jobRoles.Job_Role_ID)">
                        Delete Role
                        </button>
                    </td>
                </tr>
            </tbody>
        </table>
    </div>
    <Error v-else></Error>
</template>
<script setup>
    import NavBar from '../../components/NavBar.vue';
    import Error from '../../components/Error.vue';
</script>
<script>
    import axios from "axios";
    export default{
        data(){
            return{
                employees: [],
                category: "Category",
                keyword: "",
                hasSearch: false,
                returnData: [],
                jobRoles: [],
                userRole: 0
            }
        }, methods:{


            onload: function(){
            this.userRole = localStorage.getItem("userRole")
            axios.get('/staff/')
            .then(response => {
                // this.course = response.data.data;
                this.employees = response.data
                console.log(response.data)
                // console.log(this.employees[10].courses);
            })
            .catch(error => alert(error)) 
            axios.get('/job_role/')
            .then(response => {
                this.jobRoles = response.data
                console.log(response.data)
            })
            .catch(error => alert(error)) 
            },
            deleteRole: async function(jobID) {
                await axios.delete('/job_role/' + jobID + "/")
                .then(response => {
                // this.course = response.data.data;
                alert("Job Role has been deleted")
                location.reload();
            })
            },  
            searchFunction: function () {
                var input, filter, table, tbody, tr, tdName, tdRoles, i, txtValue;
                input = document.getElementById("search");
                filter = input.value.toUpperCase();
                tbody = document.getElementById("tbody");
                tr = tbody.getElementsByTagName("tr");

                for (i = 0; i < tr.length; i++) {
                    tdName = tr[i].getElementsByTagName("td")[0];
                    if (tdName) {
                    txtValue = [tdName.textContent];
                    console.log(txtValue)
                    if ((txtValue[0].toUpperCase().indexOf(filter) > -1)) {
                        tr[i].style.display = "";
                    } else {
                        tr[i].style.display = "none";
                    }
                    }
                }
            }

        },

        mounted(){
            this.onload()
        },
        created() {
            this.onload()
        },
        
    }
</script>
<style scoped>
    #search{
        border-color: #d8648b;
    }
    
    #search::placeholder{
        color: #d8648b;
    }

    .search-textbox:focus{
        box-shadow: #f5b9c6c7;
    }

    .category-dropdown{
        border-color: #f5b9c6c7;
        color: #f5b9c6c7;
    }

    .category-dropdown:hover{
        border-color: #f5b9c6c7;
        color: black
    }

    .category-dropdown:focus{
        border-color: #f5b9c6c7;
        color: black;
        box-shadow: none;
    }
    
    .search-button{
        background-color: #f5b9c6c7;
        color: white;
    }

    .search-button:hover{
        background-color: #f5b9c6c7;
        color: black;
    }
    td{
        color: #d8648b;
    }

    a{
        color: #d8648b;
        text-decoration: none;
    }

    a:hover{
        color:#f5b9c6c7;
    }

    #edit{
        margin: -0.5rem 0;
        scale: 0.7;
        border-color:#f5b9c6c7;
        background-color:#f5b9c6c7;
        color: white;
    }
</style>