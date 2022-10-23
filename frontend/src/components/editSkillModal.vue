<template>
    <!-- Edit Button trigger Modal -->
    <button type="button" class="btn edit-button" data-bs-toggle="modal" :data-bs-target="'#'+skillName+skillID" @click.prevent="populate">
    Edit Skill
    </button>

    <!-- Modal -->
    <div class="modal fade" :id="skillName+skillID" tabindex="-1" aria-labelledby="edit-modal" aria-hidden="true">
        <div class="modal-dialog">
            <div class="modal-content">
                <div class="modal-header">
                    <h1 class="modal-title fs-5" id="edit-modal">Update Skill Details</h1>
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                <div class="modal-body">
                    <div class="mb-3">
                        <label for="skillName" class="form-label">Skill Name</label>
                        <input type="email" class="form-control" id="skillName" placeholder="name@example.com" :value="skillName">
                    </div>
                    <div class="mb-3">
                        <label for="exampleFormControlTextarea1" class="form-label">Skill Description</label>
                        <textarea class="form-control" id="exampleFormControlTextarea1" rows="3" :value="skillDescription"></textarea>
                    </div>
                </div>
                <div class="modal-footer">
                    <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                    <button type="button" class="btn btn-primary">Save changes</button>
                </div>
            </div>
        </div>
    </div>
</template>
<script setup>
    const props = defineProps({
        skillID: Number,
        skillName: String
    })    
</script>
<script>
    import axios from "axios";
    export default{
        data(){
            return{
                skillDescription: ""
            }
        },
        computed:{
            populate:function(){
                axios.get("/skill/" + this.props.skillID +'/')
                .then(response => {
                    let skillInfo = response.data;
                    this.skillDescription = skillInfo.Skill_Desc;
                })
                .catch(error=>{
                    console.log(error.message);
                })
            }
        }
    }
</script>
<style>
    .edit-button{
        margin: -0.5rem 0;
        scale: 0.7;
        border-color:#F64C72;
        background-color:#F64C72;
        color: white;
    }

    .btn:first-child:hover{
        border-color:#F64C72;
        background-color:#F64C72;
        color: black;
    }
</style>