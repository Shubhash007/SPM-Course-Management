<template>
    <NavBar v-if="userRole == 1 || userRole == 3"></NavBar>
    <div style="min-height: 80vh;" v-if="userRole == 1 || userRole == 3">
        <div class="row g-3" style="margin: 20px 50px;">
            <div class="col-auto">
                <label for="search" class="visually-hidden">Search</label>
                <input type="text" @keyup="searchFunction" v-model="keyword" class="form-control search-textbox" id="search" placeholder="Search skill here...">
            </div>
        </div>
        <table class="table table-responsive" style="width: 75%; border-color: #d8648b; margin: 20px 60px;" border="#d8648b">
            <thead>
                <tr>
                <th scope="col">S/N</th>
                <th scope="col">Skill Name</th>
                <th scope="col">Courses</th>
                <th></th>
                <th></th>
                </tr>
            </thead>
            <tbody id="tbody">
                <tr v-for="(skill, index) in skills">
                    <th scope="row" style="color: #d8648b">{{index+1}}</th>
                    <td>{{ skill.Skill_Name}}</td> 
                    <td>
                    <ul v-for="course in skill.courses">
                        <li>{{course.split(",")[0]}}: {{course.split(",")[1] }}</li>
                    </ul>
                    </td>
                    <td><EditSkill :skillID="skill.Skill_ID" :skillName="skill.Skill_Name" :allSkills="skills"></EditSkill></td>
                    <td><button type="button" id="edit" class="btn" @click="deleteSkill(skill.Skill_ID)">
                        Delete Skill
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
    import EditSkill from '../../components/admin/editSkillModal.vue';
    import Error from '../../components/Error.vue';
</script>

<script>
    import axios from "axios";

    export default{
        data(){
            return{
                skills:[],
                keyword: "",
                hasSearch: false,
                returnData: [],
                userRole: 0,
                skillid: null
            }
        }, methods:{
            onload: function(){
                this.userRole = localStorage.getItem("userRole")
                axios.get('/skill/')
                .then(response => {
                    // this.course = response.data.data;
                    this.skills = response.data
                    console.log(this.skills)
                })
                .catch(error => alert(error)) 
            },    
            
            deleteSkill: async function(skillID) {
                await axios.delete('/skill/' + skillID + "/")
                .then(response => {
                // this.course = response.data.data;
                alert("Skill has been deleted")
                location.reload();
            })
            },


            searchFunction: function () {
                var input, filter, tbody, tr, tdName, i, txtValue;
                input = document.getElementById("search");
                filter = input.value.toUpperCase();
                tbody = document.getElementById("tbody");
                tr = tbody.getElementsByTagName("tr");

                for (i = 0; i < tr.length; i++) {
                    tdName = tr[i].getElementsByTagName("td")[0];
                
                    if (tdName) {
                    txtValue = tdName.textContent;
                    console.log(txtValue)
                    if ((txtValue.toUpperCase().indexOf(filter) > -1)) {
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
    #edit{
        margin: -0.5rem 0;
        scale: 0.7;
        border-color:#f5b9c6c7;
        background-color:#f5b9c6c7;
        color: white;
    }
    #search{
        border-color: #d8648b;
    }
    
    #search::placeholder{
        color: #d8648b;
    }

    .search-textbox:focus{
        box-shadow: #f5b9c6c7;
    }

    td{
        color: #d8648b;
    }

    ul {
    padding: 0;
    list-style-type: none;
    margin: 0;
    display: inline;
    }
</style>