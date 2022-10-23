<template>
    <NavBar></NavBar>
    <div style="min-height: 80vh;">
        <div class="row g-3" style="margin: 20px 50px;">
            <div class="col-auto">
                <label for="search" class="visually-hidden">Search</label>
                <input type="text" @keyup="searchFunction" v-model="keyword" class="form-control search-textbox" id="search" placeholder="Search by...">
            </div>
        </div>
        <table class="table table-responsive" style="width: 75%; border-color: #2F2FFA; margin: 20px 60px;" border="#2F2FFA">
            <thead>
                <tr>
                <th scope="col">S/N</th>
                <th scope="col">Staff Name</th>
                <th scope="col">Job Role</th>
                </tr>
            </thead>
            <tbody id="tbody">
                <tr v-for="(employee, index) in employees">
                    <th scope="row" style="color: #2F2FFA">{{index+1}}</th>
                    <td>{{ employee.Staff_FName}} {{employee.Staff_LName}}</td>
                    <!-- <td><router-link :to="{name: 'StaffProfile', params: {slug: employee.StaffID}}">{{ employee.Staff }}</router-link></td> -->
                    <td>{{ employee.Dept}}</td> 
                </tr>
            </tbody>
        </table>
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
                // employees: [
                //     {
                //         Role: "Software Engineer",
                //         Staff: "Mary Lamb",
                //         StaffID: 130001
                //     },
                //     {
                //         Role: "Software Engineer",
                //         Staff: "Mary Cow",
                //         StaffID: 130002
                //     },
                //     {
                //         Role: "Consultant",
                //         Staff: "Bob Tan",
                //         StaffID: 140001
                //     },
                //     {
                //         Role: "Consultant",
                //         Staff: "Benjamin Toh",
                //         StaffID: 140002
                //     }
                // ],
                employees: [],
                category: "Category",
                keyword: "",
                hasSearch: false,
                returnData: []
            }
        }, methods:{


            onload: function(){
            axios.get('/staff/')
            .then(response => {
                // this.course = response.data.data;
                this.employees = response.data
                console.log(response.data)
                // console.log(this.employees[10].courses);
            })
            .catch(error => alert(error)) 
            },  



            searchFunction: function () {
                var input, filter, table, tbody, tr, tdName, tdRoles, i, txtValue;
                input = document.getElementById("search");
                filter = input.value.toUpperCase();
                table = document.getElementById("roles");
                tbody = document.getElementById("tbody");
                tr = tbody.getElementsByTagName("tr");

                for (i = 0; i < tr.length; i++) {
                    tdName = tr[i].getElementsByTagName("td")[0];
                    tdRoles = tr[i].getElementsByTagName("td")[1];
                    if (tdName && tdRoles) {
                    txtValue = [tdName.textContent, tdRoles.textContent];
                    console.log(txtValue)
                    if ((txtValue[0].toUpperCase().indexOf(filter) > -1) || (txtValue[1].toUpperCase().indexOf(filter) > -1)) {
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
        border-color: #2F2FFA;
    }
    
    #search::placeholder{
        color: #2F2FFA;
    }

    .search-textbox:focus{
        box-shadow: #F64C72;
    }

    .category-dropdown{
        border-color: #F64C72;
        color: #F64C72;
    }

    .category-dropdown:hover{
        border-color: #F64C72;
        color: black
    }

    .category-dropdown:focus{
        border-color: #F64C72;
        color: black;
        box-shadow: none;
    }
    
    .search-button{
        background-color: #F64C72;
        color: white;
    }

    .search-button:hover{
        background-color: #F64C72;
        color: black;
    }
    td{
        color: #2F2FFA;
    }

    a{
        color: #2F2FFA;
        text-decoration: none;
    }

    a:hover{
        color:#F64C72;
    }
</style>