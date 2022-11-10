<template>
  <NavBar v-if="userRole % 2 == 0"></NavBar>
  <div class="container" style="min-height: 82vh" v-if="userRole % 2 == 0">
      <div class="row text-dark fs-1 fw-bold p-2 text-center">
          <p>My Learning Journeys</p>
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
          <div class="col-6 mx-auto mb-3">
              <div class="accordion" id="accordionExample">
                  <DeleteLJ v-for="(item,index) in data.filtered_data" id='test' :num="index" :role="item['Job_Role']['Job_Role_Name']" :roleid="item['Job_Role']['Job_Role_ID']" :courses="item['Course_Registered']" :jobrole= "item['Job_Role']" :skills="item['Job_Role']['Skills']" :jobroleid="item['id']"/>
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


// async function addRole(){
//     const response = await axios.get('http://127.0.0.1:5000/req/')
//     .then(response => {
//         console.log(response)
//         for (let each of response.data){
//             console.log(each.Staff)
//             stafflist.push(each.Staff)
//         }
//     })
//     .catch(error => {
//         flag = true;
//         if (error.response) {
//             console.log(error.response.data);
//             console.log(error.response.status);
//         }
//   });
// }

// addRole()
// console.log(stafflist)
let stafflist = []
async function get_data() {

    try {
        const staffid = await axios.get('http://127.0.0.1:5000/req/');
        console.log(staffid)
        for (let each in staffid.data){
            console.log(staffid.data[each].Staff)
            stafflist.push(staffid.data[each].Staff)
        }
        console.log(stafflist)
        let id = localStorage.getItem("staff_id");
        for (let sid of stafflist) {
            if (sid == id) {
                const response = await axios.get('http://127.0.0.1:5000/req/'+id+'/');
                let res = response.data
                data.skills_data = res
                data.filtered_data = res
                console.log(res)
            }
        }
        // if (stafflist.includes(id) == true) {
        //     console.log(id)
        //     const response = await axios.get('http://127.0.0.1:5000/req/'+id+'/');
        //     let res = response.data
        //     data.skills_data = res
        //     data.filtered_data = res
        //     console.log(res)
        // }
        // else {
        //     alert(`You do not have any existing learning journey. Please add a learning journey first.`);
            
        // }

        
        
    } catch (error) {
        alert(`You do not have any existing learning journey. Please add a learning journey first.`);
        
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
