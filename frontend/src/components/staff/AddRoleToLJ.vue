<template>
<div class="accordion-item">
    <h2 class="accordion-header" :id="'heading'+ num" >
        <button class="accordion-button" type="button" data-bs-toggle="collapse" :data-bs-target="'#collapse' + num" aria-expanded="true" :aria-controls="'collapseOne' + num" >
            {{role}}
            <div type ="hidden" style="display: none;visibility: hidden;" id="jobroleid">{{num}}</div>
        </button>
    </h2>
    <div :id="'collapse' + num" class="accordion-collapse collapse" :aria-labelledby="'heading'+ num" data-bs-parent="#accordionExample">
        <div class="accordion-body">
            <p class="fs-4 fst-italic">Skills</p>
            <ul class="list-group list-group-flush">
                <li class="list-group-item" v-if="Object.keys(allSkills).length != 0" v-for="skill in allSkills">{{skill.Skill_ID}}:{{skill.Skill_Name}}
                <div>
                    <ul v-for="c in skill.courses">
                        <li>
                            <input type="checkbox" :disabled="c.split(',')[4] == ' - Completed'" class="hi" :id='role+c' :value="c" @change="checkeditem(role+c)">
                            {{c.split(',')[0]}} : {{c.split(',')[1] }}{{c.split(',')[4]}}
                        </li>
                    </ul>
                </div>
                </li>
                <li class="list-group-item" v-else>No skills assigned to this course</li>


            </ul>
            <br>
            <button class="btn btn-md darkpink-button" @click="addcourse">Add Role to Learning Journey</button>
        </div>
    </div>
</div> 


</template>


<script setup>

import axios from "axios"
import { ref,reactive } from 'vue';
const props = defineProps({
    num: Number,
    role:String,
    skills:Object,
    coursesSelected: Object,
    roleTaken: Object
})


const data =reactive({
    skills_data:[],
    filtered_data:[],
    roleTaken: []
})

let courseSelected = []
const checkeditem = function(course_selected){
    
    var checked = document.getElementById(course_selected)
    let splitValue = checked.value.split(',')
    console.log(splitValue)
    let cid = splitValue[0]
    console.log(cid)
        if (checked.checked == true){
            console.log(checked)
            courseSelected.push(cid)
            
        }
        else{
            console.log('hi')
            courseSelected.splice(courseSelected.indexOf(cid), 1)
        }


        console.log(courseSelected)
        return(courseSelected)
    }

const addRole = function(){
    if (courseSelected.length == 0) {
        alert(`Unable to add Learning Journey. Learning Journey needs to have at least one course.`);
        window.location = "\StartLJ"
    }
}
console.log(courseSelected.length)

let Course_Registered
async function addcourse() {
 
    try {
        let id = localStorage.getItem("staff_id");
        console.log(id)
        console.log(props.num)
        Course_Registered = {"Course_Registered": courseSelected}
        console.log(courseSelected.length)
        
        if (courseSelected.length != 0) {
            const response = await axios.post('http://127.0.0.1:5000/req/'+id+'/'+props.num+'/',Course_Registered);
            alert(`Learning Journey Added`);
            window.location = "\StartLJ"
        }
        else{
            alert(`Unable to add Learning Journey. Learning Journey needs to have at least one course.`);
            window.location = "\StartLJ"
            
        }
        console.log(response)

    } 
    catch (error) {
        // alert(`DB is inaccesible at the moment due to ${error.message}`);
    }
}
</script>
<script>
    export default{
        data(){
            return{
                allSkills: {}
            }
        },
        methods:{
            filterCourses:function(){
                this.allSkills = this.props.skills;
                for (let eachSkill of this.allSkills){
                    let courses = eachSkill.courses;
                    for (let i=0; i<courses.length; i++){
                        console.log(courses[i]);
                        let courseCode = courses[i].split(',')[0];
                        axios.get("/registration/")
                        .then(response => {
                            let data = response.data;
                            for (let item of data){
                                if (item.Staff == localStorage.getItem("staff_id") && item.Completion_Status == "Completed" && item.Course == courseCode){
                                    courses[i] += ", - Completed";
                                }
                            }
                        })
                        .catch(error => {
                            console.log(error.message);
                        })
                    }
                }
            }
        },created(){
            this.filterCourses();
        }
    }
</script>
<style scoped>
    .darkpink-button{
        border-color: #d8648b;
        background-color: #d8648b;
        color: white;
    }

    .darkpink-button:hover{
        border-color: #d8648b;
        background-color: #d8648b;
        color: black;
    }
</style>