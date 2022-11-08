<template>
    <NavBar v-if="userRole != 1"></NavBar>
    <div class="container" style="min-height: 82vh" v-if="userRole != 1">
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
                    <addCourse v-for="(item,index) in data.filtered_data" :num="index" :role="item.Job_Role_Name" :skills="item.Skills" :id="item.Job_Role_ID" />
                </div>
            </div>
        </div>           
    </div>
    <Error v-else></Error>
  </template>
  <script setup>
  import AddRoleToLJ from '@/components/staff/AddRoleToLJ.vue'
  import { ref,reactive } from 'vue';
  import addCourse from '../../components/staff/addCourse.vue';
  import NavBar from '../../components/NavBar.vue';
  import Error from '../../components/Error.vue';
  

  import axios from "axios";
  const search_term = ref('')
    const data =reactive({
    skills_data:[],
    filtered_data:[],
})



async function get_data() {
    try {
        const response = await axios.get('http://127.0.0.1:5000/job_role/');
        let res = response.data
        data.skills_data = res
        data.filtered_data = res;
        // return res
        // localStorage.setItem('JobRoleID',id);
        // data.IDlist = res
        console.log(res);
    } catch (error) {
        alert(`DB is inaccesible at the moment due to ${error.message}`);
    }
}

get_data()

const update_filter = function(){
    let search = search_term.value.toLowerCase()
    if( search && search.length > 0){
        let res = data.skills_data.filter(info => info.Job_Role_Name.toLowerCase().startsWith(search) )
        console.log(res)
        data.filtered_data = res
    //     console.log(data.filtered_data)
     }
    else{
        data.filtered_data = data.skills_data
    }
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
  
  .search-button{
      background-color: #f5b9c6c7;
      color: white;
  }

  .search-button:hover{
      background-color: #f5b9c6c7;
      color: black;
  }
</style>
