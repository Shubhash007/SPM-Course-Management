<template>
  <NavBar v-if="userRole % 2 == 0"></NavBar>
  <div class="container" style="min-height: 82vh" v-if="userRole % 2 == 0">
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
                  <DeleteLJ v-for="(item,index) in data.filtered_data" id='test' :num="index" :role="item['Job_Role']['Job_Role_Name']" :courses="item['Course_Registered']" :jobrole= "item['Job_Role']" :skills="item['Job_Role']['Skills']"/>
              </div>
          </div>
      </div>           
  </div>
  <Error v-else></Error>
</template>

<script setup>
import { ref,reactive } from 'vue';
import DeleteLJ from '../../components/staff/DeleteLJ.vue';
import NavBar from '../../components/NavBar.vue';
import Error from '../../components/Error.vue';
import axios from 'axios'

const search_term = ref('')
const data =reactive({
    skills_data:[],
    filtered_data:[],
})

async function get_data() {
    try {
        let id = localStorage.getItem("staff_id");
        console.log(id)
        const response = await axios.get('http://127.0.0.1:5000/req/'+id+'/');
        let res = response.data
        data.skills_data = res
        data.filtered_data = res
        console.log(res)
        // for (let item in res) {
        //   data.skills_data = res[item].Job_Role['Skills']
        // }
        
        // console.log(typeof(data.skills_data))
        
        return res
    } catch (error) {
        alert(`DB is inaccesible at the moment due to ${error.message}`);
    }
    
}
get_data()

const update_filter = function(){
    let search = search_term.value.toLowerCase()
    if( search && search.length > 0){
        let res = data.skills_data.filter(info => info.Job_Role.Job_Role_Name.toLowerCase().startsWith(search) )
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
    export default{
        data(){
        return{
            userRole: 0
        }
        },
        created(){
        this.userRole = localStorage.getItem("userRole");
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
