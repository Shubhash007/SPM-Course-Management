<template>
  <div class="container">
      <div class="row text-dark fs-1 fw-bold p-2 text-center">
          <p>Learning Journeys</p>
      </div>

      <div class="row" style="margin: 20px 50px;">
          <div class="col-3"></div>
          <div class="col-3">
              <label for="search" class="visually-hidden">Search</label>
              <input @change="update_filter" @keyup="update_filter"  v-model="search_term"  type="text" class="form-control search-textbox" id="search" placeholder="Search for Job Role...">
          </div>
          <div class="col-3" >
              <button type="submit" class="btn search-button mb-3">Search</button>
          </div>
          <div class="col-3"></div>
      </div>

      <div class="row">
          <div class="col-6 mx-auto">
              <div class="accordion" id="accordionExample">
                  <DeleteLJ v-for="(item,index) in data.filtered_data" :num="index" :role="item.role" :skills="item.skills"  />
              </div>
          </div>
      </div>           
  </div>
</template>

<script setup>
import AddRoleToLJ from '@/components/AddRoleToLJ.vue'
import { ref,reactive } from 'vue';
import DeleteLJ from '../components/DeleteLJ.vue';

const search_term = ref('')
const data =reactive({
  skills_data:[
  {    
      role: "Software Engineer",
      skills: {'Python': 
                  ["Intro to Python", "Flask Techniques"]
                  ,
                'PHP':
                  ["Intro to PHP"]
              }
  },
  {
      role: "Developer",
      skills: {'Python': 
                  ["Intro to Python", "Flask Techniques"],

                'PHP':
                  ["Intro to PHP"]
              }
  }
],
  filtered_data:[]
})
data.filtered_data = data.skills_data

const update_filter = function(){
  let search = search_term.value.toLowerCase()
  if( search && search.length > 0){
      let res = data.skills_data.filter(info => info.role.toLowerCase().startsWith(search) )
      console.log(res)
      data.filtered_data = res
      console.log(data.filtered_data)
  }
  else{
      data.filtered_data = data.skills_data
  }
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
  
  .search-button{
      background-color: #F64C72;
      color: white;
  }

  .search-button:hover{
      background-color: #F64C72;
      color: black;
  }
</style>
