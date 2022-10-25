<template>
    <!-- Edit Button trigger Modal -->
    <button type="button" class="btn edit-button" data-bs-toggle="modal" :data-bs-target="'#'+skillName+skillID" @click.prevent="populate()">
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
                        <input type="text" class="form-control" id="skillName" placeholder="Enter Skill Name"  v-model="skillname">
                        <p v-show="hasErrors" class="error-message">{{ errorMessage }}</p>
                    </div>
                    <div class="mb-3">
                        <label for="exampleFormControlTextarea1" class="form-label">Skill Description</label>
                        <textarea class="form-control" id="exampleFormControlTextarea1" rows="3" v-model="skillDescription"></textarea>
                    </div>
                </div>
                <div class="modal-footer">
                    <button type="button" class="btn btn-secondary" id="close-button" data-bs-dismiss="modal">Close</button>
                    <button type="button" class="btn save-changes" @click="editSkills()">Save changes</button>
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
                skillname: "",
                skillDescription: "",
                hasErrors: false,
                errorMessage: ""
            }
        },
        methods:{
            editSkills:function(){
                if (this.skillname.length > 3 && this.skillname.length < 20){
                    this.hasErrors = false;
                    this.errorMessage = "";
                    axios.patch("/skill/" + this.props.skillID + "/", {
                        "Skill_Name": this.skillname,
                        "Skill_Desc": this.skillDescription
                    })
                    .then(response => {
                        console.log(response.data);
                        console.log(this.skillname);
                    })
                    .catch(error =>{
                        console.log(error.message);
                    }) 
                }else{
                    this.hasErrors = true;
                    this.errorMessage = "Edited skill name has to be more than 3 and less than 20 characters";
                }
            },
            // editSkills:function(){
            //     axios.get("/skill/")
            //     .then(response => {
            //         console.log(response.data);
            //         let skills = response.data;
            //         let duplicateCount = 0;
            //         console.log(skills[0].Skill_Name);
            //         for (skill in skills){
            //             if (this.skillname == skills.skill.Skill_Name){
            //                 duplicateCount += 1;
            //             }
            //         }

            //         if (this.skillname.length > 3 && this.skillname.length < 20 && duplicateCount == 0){
            //             this.hasErrors = false;
            //             this.errorMessage = "";
            //             axios.patch("/skill/" + this.props.skillID + "/", {
            //                 "Skill_Name": this.skillname,
            //                 "Skill_Desc": this.skillDescription
            //             })
            //             .then(response => {
            //                 console.log(response.data);
            //                 console.log(this.skillname);
            //             })
            //             .catch(error =>{
            //                 console.log(error.message);
            //             }) 
            //         }else if (duplicateCount > 0){
            //             this.hasErrors = true;
            //             this.errorMessage = "Edited skill name already exists";
            //         }else{
            //             this.hasErrors = true;
            //             this.errorMessage = "Edited skill name has to be more than 3 and less than 20 characters";
            //         }
            //     })
            //     .catch(error=>{
            //         console.log(error.message);
            //     })
            // }, 
            populate:function(){
                axios.get("/skill/" + this.props.skillID +'/')
                .then(response => {
                    let skillInfo = response.data;
                    this.skillname = skillInfo.Skill_Name;
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

    .btn:first-child:hover , :not(.btn-check)+.btn:hover{
        border-color:#F64C72;
        background-color:#F64C72;
        color: black;
    }

    .error-message{
        color: red;
        font-size: small;
    }

    .save-changes{
        background-color: #F64C72;
        color: white;
    }

    #close-button:hover{
        background-color: black;
        border-color: black;
        color: white;
    }
</style>