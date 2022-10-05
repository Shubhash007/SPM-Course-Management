<template>
    <div class="container">
        <div class="row text-white fs-1 fw-bold p-2 text-center">
            <p>Start Learning Jorney</p>
        </div>

        <div class="row">
            <div class="col-6 mx-auto">
                <p class="fs-3 text-white">Select Role</p>
                <div class="accordion" id="accordionExample">
                    <!-- <div class="accordion-item">
                        <h2 class="accordion-header" id="headingOne">
                            <button class="accordion-button" type="button" data-bs-toggle="collapse" data-bs-target="#collapseOne" aria-expanded="true" aria-controls="collapseOne">
                                Accordion Item #1
                            </button>
                        </h2>
                        <div id="collapseOne" class="accordion-collapse collapse" aria-labelledby="headingOne" data-bs-parent="#accordionExample">
                            <div class="accordion-body">
                                <strong>This is the first item's accordion body.</strong> It is shown by default, until the collapse plugin adds the appropriate classes that we use to style each element. These classes control the overall appearance, as well as the showing and hiding via CSS transitions. You can modify any of this with custom CSS or overriding our default variables. It's also worth noting that just about any HTML can go within the <code>.accordion-body</code>, though the transition does limit overflow.
                                <br><button type="button" class="btn btn-outline-danger btn-md">Add Skill to Learning Jorney</button>
                            </div>
                        </div>
                    </div> 
                    <div class="accordion-item">
                        <h2 class="accordion-header" id="headingTwo">
                            <button class="accordion-button" type="button" data-bs-toggle="collapse" data-bs-target="#collapseTwo" aria-expanded="true" aria-controls="collapseOne">
                                Accordion Item #2
                            </button>
                        </h2>
                        <div id="collapseTwo" class="accordion-collapse collapse" aria-labelledby="headingTwo" data-bs-parent="#accordionExample">
                            <div class="accordion-body">
                                <strong>This is the first item's accordion body.</strong> It is shown by default, until the collapse plugin adds the appropriate classes that we use to style each element. These classes control the overall appearance, as well as the showing and hiding via CSS transitions. You can modify any of this with custom CSS or overriding our default variables. It's also worth noting that just about any HTML can go within the <code>.accordion-body</code>, though the transition does limit overflow.
                                <br><button type="button" class="btn btn-outline-danger btn-md">Add Skill to Learning Jorney</button>
                            </div>
                        </div>
                    </div>  -->
                    <AddSkillToLJVue num="One" role="Developer" :skills="['A','B']" />
                </div>
            </div>
        </div>           
    </div>

</template>

<script>
import AddSkillToLJVue from '../components/AddSkillToLJ.vue';
import { data } from 'browserslist';
    export default {
    components: { 
        AddSkillToLJVue, 
    },
    data(){
        return{

        }
    }
}
</script>