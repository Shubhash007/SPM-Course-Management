<template>
    <NavBar></NavBar>
    <div style="min-height: 80vh;">
        <div class="row g-3" style="margin: 20px 50px;">
            <div class="col-auto">
                <label for="search" class="visually-hidden">Search</label>
                <input type="text" @keyup="searchFunction" v-model="keyword" class="form-control search-textbox" id="search" placeholder="Search skill here...">
            </div>
        </div>
        <table class="table table-responsive" style="width: 75%; border-color: #2F2FFA; margin: 20px 60px;" border="#2F2FFA">
            <thead>
                <tr>
                <th scope="col">S/N</th>
                <th scope="col">Skill Name</th>
                <th scope="col">Courses</th>
                <th></th>
                </tr>
            </thead>
            <tbody id="tbody">
                <tr v-for="(skill, index) in skills">
                    <th scope="row" style="color: #2F2FFA">{{index+1}}</th>
                    <td>{{ skill.Skill_Name}}</td> 
                    <td>{{ skill.courses.toString() }}</td>
                    <td><EditSkill :skillID="skill.Skill_ID" :skillName="skill.Skill_Name" :allSkills="skills"></EditSkill></td>
                </tr>
            </tbody>
        </table>
    </div>
</template>
<script setup>
    import NavBar from '../components/NavBar.vue';
    import EditSkill from '../components/editSkillModal.vue';
</script>
<script>
    import axios from "axios";

    export default{
        data(){
            return{
                skills:[],
                keyword: "",
                hasSearch: false,
                returnData: []
            }
        }, methods:{
            onload: function(){
                axios.get('/skill/')
            .then(response => {
                // this.course = response.data.data;
                this.skills = response.data
                console.log(this.skills)
            })
            .catch(error => alert(error)) 
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
    #search{
        border-color: #2F2FFA;
    }
    
    #search::placeholder{
        color: #2F2FFA;
    }

    .search-textbox:focus{
        box-shadow: #F64C72;
    }

    td{
        color: #2F2FFA;
    }
</style>