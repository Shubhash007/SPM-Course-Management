<template>
  <NavBar></NavBar>
  <div class="container" style="min-height: 82vh">
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
                  <DeleteLJ v-for="(item,index) in data.filtered_data" :num="index" :role="item.role" :skills="item.skills" />
                  {{getSkill}}
              </div>
          </div>
      </div>           
  </div>
</template>

<script setup>
import AddRoleToLJ from '@/components/AddRoleToLJ.vue'
import { ref,reactive } from 'vue';
import DeleteLJ from '../components/DeleteLJ.vue';
import axios from 'axios'
import NavBar from '../components/NavBar.vue';

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
      skills: {'Javascript': 
                  ["Intro to JS", "Vuejs Techniques"],

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

<script>


export default {
  data() {
    return {
      course: [],
      search : 130001
  }
},
  computed: {
    
    // a computed getter
    getSkill() {
        axios.get('/courseSkill')
        .then(response => {
            this.course = response.data.data;
            console.log(response.data)
            
        })
        .catch(error => alert(error)) 
    }

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
