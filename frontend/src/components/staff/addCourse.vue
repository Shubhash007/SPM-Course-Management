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
                    <li class="list-group-item" v-for="value, key in skills">{{key}}
                            <ol>
                                <li v-for="skill in value">
                                    {{skill}}
                                    <button type="submit" class="btn btn-sm delete-button" @click="addCourse">Add</button>
                                </li>
                            </ol>
                            <br>
                    </li>
                </ul>
            </div>
        </div>
    </div> 
    
    
    </template>
    
    
<script setup>
    const props = defineProps({
        num: Number,
        role:String,
        skills:Object
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
      
      .delete-button{
        background-color: #f5b9c6c7;
        color: white;
      }
    
      .delete-button:hover{
          background-color: #f5b9c6c7;
          color: black;
      }
    </style>