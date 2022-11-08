<template>
    <div class="accordion-item">
            <h2 class="accordion-header" :id="'heading'+ num">
            <button class="accordion-button" type="button" data-bs-toggle="collapse" :data-bs-target="'#collapse' + num" aria-expanded="true" :aria-controls="'collapseOne' + num">
                {{role}}
            </button>

            
        </h2>
        <div :id="'collapse' + num" class="accordion-collapse collapse" :aria-labelledby="'heading'+ num" data-bs-parent="#accordionExample">
            <div class="accordion-body">
                <ul class="list-group list-group-flush">
                    <li class="list-group-item" v-for="value, index in skills">
                        <AddCoursesModal  :CoursesSelected="value.courses" :JobRole="value.jobrole" :i="num" :SkillSelected="index" :jobroleid="id"/>
                            <ul>
                                <li>
                                    {{value.Skill_Name}}
                                    <ul class="list-group-item" v-for="item,index in value.courses">
                                        <li>
                                            {{item.split(',')[1]}} 
                                            <div type ="hidden" style="display: none;visibility: hidden;" :id="courseroleid">{{item.split(',')[0]}}</div>
                                        </li>
                                    </ul>
                                    
                                </li>
                            </ul>
                            <br>
                    </li>
                </ul>
            </div>
        </div>
    </div> 
    
    
    </template>
    
    
<script setup>

import axios from "axios";
import AddCoursesModal from "./addCourseModal.vue";

    const props = defineProps({
        num: Number,
        role:String,
        skills:Object,
        id:Number,
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
      
      .delete-button{
        background-color: #F64C72;
        color: white;
      }
    
      .delete-button:hover{
          background-color: #F64C72;
          color: black;
      }
    </style>