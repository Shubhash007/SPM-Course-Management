<template>
    <div class="accordion-item">
        <h2 class="accordion-header" :id="'heading'+ num">
            <button class="accordion-button" type="button" data-bs-toggle="collapse" :data-bs-target="'#collapse' + num" aria-expanded="true" :aria-controls="'collapseOne' + num">
                {{role}}
            </button>
        </h2>

        <div :id="'collapse' + num" class="accordion-collapse collapse" :aria-labelledby="'heading'+ num" data-bs-parent="#accordionExample">
            <div class="accordion-body" v-for="skill, index in (skills)">
                <ul class="list-group list-group-flush">
                    <li class="list-group-item" >
                        <div>
                            <div class="row">
                                <div class="col-10">
                                    {{skill.Skill_Name}}
                                </div>
                                <div class="col-2">
                                    <!-- need to amend this after new db is out -->
                                    <editCoursesModal :coursesSelected="courses" :jobrole="jobrole" :no="num" :skillSelected="index"/>
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
import editCoursesModal from '../components/editCoursesModal.vue';


    const props = defineProps({
        num: Number,
        role: String,
        skills: Object,
        courses: String,
        jobrole:Object
    })


    
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
    
    .pink-button{
    background-color: #F64C72;
    color: white;
    }

    .pink-button:hover{
        background-color: #F64C72;
        color: black;
    }
</style>