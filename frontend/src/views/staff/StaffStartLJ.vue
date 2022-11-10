<template>
    <NavBar v-if="userRole == 2 || userRole == 4"></NavBar>
    <div class="container" style="min-height: 82vh" v-if="userRole == 2 || userRole == 4">
        <div class="row text-dark fs-1 fw-bold p-2 text-center">
            <p>Start Learning Journey</p>
            <div class="text-muted fs-4">Click on role to see information</div>
        </div>

        <div class="row">
            <div class="col-6 mx-auto">
                <div class="accordion" id="accordionExample">
                    <AddRoleToLJ v-for="(item,index) in data.remaining" :num="item.Job_Role_ID" :role="item.Job_Role_Name" :skills="item.Skills"  />
                </div>
            </div>
        </div>           
    </div>
    <Error v-else></Error>
</template>

<script setup>
import AddRoleToLJ from '@/components/staff/AddRoleToLJ.vue';
import Error from '@/components/Error.vue';
import { ref,reactive } from 'vue';
import axios from "axios"
import NavBar from '../../components/NavBar.vue';

const search_term = ref('')
const data =reactive({
    skills_data:[],
    filtered_data:[],
    taken: [],
    available: [],
    remaining:[]
})

async function get_data() {
    
    try {
        const response = await axios.get('http://127.0.0.1:5000/job_role/');
        let res = response.data
        data.skills_data = res
        data.filtered_data = res
        console.log(res)
        return res

    } catch (error) {
        alert(`DB is inaccesible at the moment due to ${error.message}`);
    }
}

// async function getJobs() {
//     try{
//         let id = localStorage.getItem("staff_id");
//         console.log(id)
//         const responseReq = await axios.get('http://127.0.0.1:5000/req/'+id+'/');
//         data.taken = responseReq.data
//         const response = await axios.get('http://127.0.0.1:5000/job_role/');
//         data.available = response.data
//         console.log(data.available)
//         console.log(data.taken)
//         var existing = []
//         for (let a = 0; a < data.available.length; a++){
//             for (let t in data.taken){
//                 if (data.taken[t].Job_Role.Job_Role_ID == data.available[a].Job_Role_ID) {
//                     console.log(data.taken[t].Job_Role.Job_Role_ID)
//                     existing.push(data.available[a].Job_Role_ID)
//                 }   
//             }
//         }
//         var dontExist = []
//         for (let a = 0; a < data.available.length; a++){
//             if (existing.includes(data.available[a].Job_Role_ID) == false){
//                 dontExist.push(data.available[a].Job_Role_ID)
//             }
//         }
//         console.log(dontExist)
//         for (let i in dontExist){
//                 if (dontExist[i] == data.available[dontExist[i]-1].Job_Role_ID){
//                     data.remaining.push(data.available[dontExist[i]-1])
//                 }
//                 console.log(dontExist[i],data.available[dontExist[i]-1].Job_Role_ID)
//         }
//             console.log(data.remaining)
//         }
        
    
//     catch{
//     }
// }
let id = localStorage.getItem("staff_id")
let flag = false;
const addRole = function(){
    axios.get('http://127.0.0.1:5000/req/'+ id+'/')
    .then(response => {
        console.log(response)
    })
    .catch(error => {
        flag = true;
        if (error.response) {
            console.log(error.response.data);
            console.log(error.response.status);
            console.log(error.response.headers);
        }
    });
}

addRole();
async function getJobs() {
    try{
        let id = localStorage.getItem("staff_id");
        console.log(id);
        console.log(flag);
        const responseReq = await axios.get('http://127.0.0.1:5000/req/'+id+'/');
        console.log(responseReq.status == 400);
        data.taken = responseReq.data
        const response = await axios.get('http://127.0.0.1:5000/job_role/');
        data.available = response.data
        console.log(data.available)
        console.log(data.taken)
        var existing = []
        for (let a = 0; a < data.available.length; a++){
            for (let t in data.taken){
                if (data.taken[t].Job_Role.Job_Role_ID == data.available[a].Job_Role_ID) {
                    console.log(data.taken[t].Job_Role.Job_Role_ID)
                    existing.push(data.available[a].Job_Role_ID)
                }   
            }
        }
        var dontExist = []
        for (let a = 0; a < data.available.length; a++){
            if (existing.includes(data.available[a].Job_Role_ID) == false){
                dontExist.push(data.available[a].Job_Role_ID)
            }
        }
        console.log(dontExist)
        for (let i in dontExist){
                if (dontExist[i] == data.available[dontExist[i]-1].Job_Role_ID){
                    data.remaining.push(data.available[dontExist[i]-1])
                }
                console.log(dontExist[i],data.available[dontExist[i]-1].Job_Role_ID)
        }
            console.log(data.remaining)
        }
        
    
    catch{
    }
}


get_data()
getJobs()


const update_filter = function(){
    let search = search_term.value.toLowerCase()
    if( search && search.length > 0){
        let res = data.skills_data.filter(info => info.Job_Role_Name.toLowerCase().startsWith(search) )
        console.log(res)
        data.remaining = res
    }
    else{
        data.remaining = data.skills_data
    }
}
</script>
<script>
    export default{
        data(){
            return{
                userRole: 0
            }
        }, created(){
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