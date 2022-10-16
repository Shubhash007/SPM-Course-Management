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
                    <li class="list-group-item" v-for="courses, skill in skills">
                        <div>
                            <div class="row">
                                <div class="col-10">
                                    {{skill}}
                                </div>
                                <div class="col-2">
                                    <editCoursesModal :coursesSelected="courses" :no="num" :skillSelected="skill"/>
                                </div>
                                <div>
                                    <ol>
                                        <li v-for="course in courses">
                                            {{course}}
                                        </li>
                                    </ol>
                                </div>
                                </div>
                            </div>
                        <br>
                    </li>
                </ul>
                <button type="button" class="btn btn-outline-danger btn-md">Delete Learning Journey</button>
            </div>
        </div>
    </div>     
</template>
    
    
<script setup>
import editCoursesModal from '../components/editCoursesModal.vue';

    const props = defineProps({
        num: Number,
        role: String,
        skills: Object,
        courses: Object,
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