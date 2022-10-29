<template>
<div class="accordion-item">
    <h2 class="accordion-header" :id="'heading'+ num">
        <button class="accordion-button" type="button" data-bs-toggle="collapse" :data-bs-target="'#collapse' + num" aria-expanded="true" :aria-controls="'collapseOne' + num">
            {{role}}
        </button>
    </h2>
    <div :id="'collapse' + num" class="accordion-collapse collapse" :aria-labelledby="'heading'+ num" data-bs-parent="#accordionExample">
        <div class="accordion-body">
            <p class="fs-4 fst-italic">Skills</p>
            <ul class="list-group list-group-flush">
                <li class="list-group-item" v-if="Object.keys(skills).length != 0" v-for="skill in skills">{{skill.Skill_ID}}:{{skill.Skill_Name}}</li>
                <li class="list-group-item" v-else>No skills assigned to this course</li>
            </ul>
            <br><button type="button" class="btn btn-outline-danger btn-md">Add Role to Learning Jorney</button>
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
console.log(props.num)
</script>