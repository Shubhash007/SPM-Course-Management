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
                        <ul>
                        <li v-for="values, keys in value">{{keys}}
                            <ol>
                                <li v-for="skill in values">
                                    {{skill}}
                                    <button type="submit" class="btn btn-sm delete-button" @click="deleteCourse">Delete</button>
                                </li>
                            </ol>
                            <br>
                        </li>
                    </ul>
                    </li>
                </ul>
                <button type="button" class="btn btn-outline-danger btn-md">Delete Learning Journey</button>
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