<template>
    <div class="accordion-item">
        <h2 class="accordion-header" :id="'heading'+ num">
            <div type ="hidden" style="display: none;visibility: hidden;">{{roleid}}</div>
            <button class="accordion-button" :id="num" type="button" @click="getID(roleid)" data-bs-toggle="collapse" :data-bs-target="'#collapse' + num" aria-expanded="true" :aria-controls="'collapseOne' + num">
                {{role}}
            </button>
        </h2>

        <div :id="'collapse' + num" class="accordion-collapse collapse" :aria-labelledby="'heading'+ num" data-bs-parent="#accordionExample">
            <div class="col-2">
                <editCoursesModal :coursesSelected="courses" :jobrole="jobrole" :no="num" :skillSelected="index" :roleid="roleid"/>            
                <AddCoursesModal  :CoursesSelected="courses" :Jobrole="jobrole" :i="num" :SkillSelected="index"/>
            </div>
            <div class="accordion-body" v-for="skill, index in (skills)">
                <ul class="list-group list-group-flush">
                    <li class="list-group-item" >
                        <div>
                            <div class="row">
                                <div class="col-10">
                                    {{skill.Skill_Name}}
                                </div>
                                <div>
                                    <ul>
                                        <li>
                                            {{skill.Skill_Desc}}
                                        </li>
                                    </ul>
                                </div>
                            </div>
                        </div>
                        <br>
                    </li>
                </ul>
            </div>

            <button type="button" class="btn btn-outline-danger btn-md" @click="deleteLJ()">Delete Learning Journey</button>
        </div>
        
    </div>     
</template>
    
    
<script setup>
import { list } from 'postcss';
import editCoursesModal from './editCoursesModal.vue';
import AddCoursesModal from "./addCourseModal.vue";
import axios from "axios"

    const props = defineProps({
        num: Number,
        role: String,
        skills: Object,
        courses: String,
        jobrole:Object,
        regcourses: String,
        jobroleid:Number,
        roleid:String,
    })
    let roleID 
    const getID = function(tryyy) {
            roleID = tryyy
            console.log(roleID)
    }

    const deleteLJ = function() { 
        let id = localStorage.getItem("staff_id");
        console.log(id)
        console.log(roleID)
        axios.delete('http://127.0.0.1:5000/req/'+id+'/'+roleID+'/')
    
        alert(props.role + ` Role Successfully Removed from Learning Journey`);
        window.location = "\EditLearningJourneys"
    
        console.log(response)
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
    
    .pink-button{
    background-color: #f5b9c6c7;
    color: white;
    }

    .pink-button:hover{
        background-color: #f5b9c6c7;
        color: black;
    }
</style>