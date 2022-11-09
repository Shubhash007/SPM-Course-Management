<template>
    <NavBar></NavBar>
    <div class="container" style="min-height: 82vh">
        <div class="row text-dark fs-1 fw-bold p-2 text-center">
            <p>Start Learning Journey</p>
            <div class="text-muted fs-4">Click on role to see information</div>
        </div>

        <div class="row" style="margin: 20px 320px;">
            <div class="col-10">
                <label for="search" class="visually-hidden">Search</label>
                <input @change="update_filter" @keyup="update_filter"  v-model="search_term"  type="text" class="form-control search-textbox" id="search" placeholder="Search for Job Role...">
            </div>
            <div class="col-2">
                <button type="submit" class="btn search-button mb-3">Search</button>
            </div>
        </div>

        <div class="row">
            <div class="col-6 mx-auto">
                <div class="accordion" id="accordionExample">
                    <AddRoleToLJ v-for="(item,index) in data.remaining" :num="item.Job_Role_ID" :role="item.Job_Role_Name" :skills="item.Skills"  />
                </div>
            </div>
        </div>           
    </div>
</template>

<script setup>
import AddRoleToLJ from '@/components/staff/AddRoleToLJ.vue'
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

        console.log(res)
        return res

    } catch (error) {
        alert(`DB is inaccesible at the moment due to ${error.message}`);
    }
}

async function getJobs() {
    try{
        let id = localStorage.getItem("staff_id");
        console.log(id)
        const responseReq = await axios.get('http://127.0.0.1:5000/req/'+id+'/');
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
            data.filtered_data =data.remaining
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
        console.log(data.filtered_data)
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