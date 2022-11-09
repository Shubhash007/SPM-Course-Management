<template>
    <div class="accordion-item">
        <h2 class="accordion-header" :id="'heading'+ num">
            <button class="accordion-button" type="button" data-bs-toggle="collapse" :data-bs-target="'#collapse' + num" aria-expanded="true" :aria-controls="'collapseOne' + num">
                {{role}}
            </button>
        </h2>

        <div :id="'collapse' + num" class="accordion-collapse collapse" :aria-labelledby="'heading'+ num" data-bs-parent="#accordionExample" >
            <div class="col-2">
                <editCoursesModal :coursesSelected="courses" :jobrole="jobrole" :no="num" :skillSelected="index"/>            </div>
                <div type ="hidden" style="display: none;visibility: hidden;" id="checks">{{courses}}</div>
                <div type ="hidden" style="display: none;visibility: hidden;" id="skill">{{skills}}</div>
                <AddCoursesModal  :CoursesSelected="skills" :jobrole="jobrole" :i="num" :SkillSelected="index" :jobroleid="jobroleid" :checkcourse="courses"/>
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

            <button type="button" class="btn btn-outline-danger btn-md">Delete Learning Journey</button>
        </div>
        
    </div>     
</template>
    
    
<script setup>
import { list } from 'postcss';
import editCoursesModal from './editCoursesModal.vue';
import AddCoursesModal from "../../components/addCourseModal.vue";



    const props = defineProps({
        num: Number,
        role: String,
        skills: Object,
        courses: String,
        jobrole:Object,
        regcourses: String,
        jobroleid:Number,

    })



    
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