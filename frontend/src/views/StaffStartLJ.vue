<template>
    <div class="container">
        <div class="row text-dark fs-1 fw-bold p-2 text-center">
            <p>Start Learning Jorney</p>
            <div class="text-muted fs-4">Click on role to see information</div>
        </div>

        <div class="row">
            <div class="col-6 mx-auto">
                <p class="fs-3 text-white">Select Role</p>
                <div class="accordion" id="accordionExample">
                    <AddRoleToLJ v-for="(item,index) in skills_data" :num="index" :role="item.role" :skills="item.skills"  />
                </div>
            </div>
        </div>           
    </div>
</template>

<script setup>
import AddRoleToLJ from '@/components/AddRoleToLJ.vue'
import { ref,reactive } from 'vue';

const skills_data =reactive([
    {    
        role: "Developer",
        skills: ['A','B']
    },
    {
        role: "Sales",
        skills: ['C','D']
    },
    {
        role: "Ops",
        skills: ['E','F']
    }
])



</script>