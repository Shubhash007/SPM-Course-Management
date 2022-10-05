<template>
<div class="accordion-item">
    <h2 class="accordion-header" :id="'heading'+ num">
        <button class="accordion-button" type="button" data-bs-toggle="collapse" :data-bs-target="'#collapse' + num" aria-expanded="true" :aria-controls="'collapseOne' + num">
            {{role}}
        </button>
    </h2>
    <div :id="'collapse' + num" class="accordion-collapse collapse" :aria-labelledby="'heading'+ num" data-bs-parent="#accordionExample">
        <div class="accordion-body">
            <ul class="list-group list-group-flush">
                <li class="list-group-item" v-for="skill in skills">{{skill}}</li>
            </ul>
            <br><button type="button" class="btn btn-outline-danger btn-md">Add Role to Learning Jorney</button>
        </div>
    </div>
</div> 


</template>


<script>
    name: AddSkillToLJ
    export default {
        props : ['num','role','skills']
    }


</script>