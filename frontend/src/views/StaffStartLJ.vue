<template>
    <div class="container">
        <div class="row text-dark fs-1 fw-bold p-2 text-center">
            <p>Start Learning Jorney</p>
            <div class="text-muted fs-4">Click on role to see information</div>
        </div>

        <div class="row" style="margin: 20px 50px;">
            <div class="col-3">
                <label for="search" class="visually-hidden">Search</label>
                <input @change="update_filter" @keyup="update_filter"  v-model="search_term"  type="text" class="form-control search-textbox" id="search" placeholder="Search for Job Role...">
            </div>
            <div class="col-3">
                <button type="submit" class="btn search-button mb-3">Search</button>
            </div>
        </div>

        <div class="row">
            <div class="col-6 mx-auto">
                <div class="accordion" id="accordionExample">
                    <AddRoleToLJ v-for="(item) in data.filtered_data" :num="item.Job_Role_ID" :role="item.Job_Role_Name" :skills="item.Skills"  />
                </div>
            </div>
        </div>           
    </div>
</template>

<script setup>
import AddRoleToLJ from '@/components/AddRoleToLJ.vue'
import { ref,reactive } from 'vue';
import axios from "axios"

const search_term = ref('')
const data =reactive({
    skills_data:[],
    filtered_data:[],
})

async function get_data() {
    try {
        const response = await axios.get('http://127.0.0.1:5000/job_role');
        let res = response.data
        data.skills_data = res
        data.filtered_data = res
        return res
        // for (item) in data {

        // }
        // console.log(data)
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