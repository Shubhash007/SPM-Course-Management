<template>
    <div class="modal fade" :id="'edit-button'+staffID" aria-hidden="true" aria-labelledby="first-modal" tabindex="-1">
        <div class="modal-dialog modal-dialog-centered">
            <div class="modal-content">
                <div class="modal-header">
                    <h1 class="modal-title fs-5" id="first-modal">Edit Roles</h1>
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                <div class="modal-body">
                    <label for="search" class="visually-hidden">Search</label>
                    <input type="text" @keyup="searchFunction" v-model="keyword" class="form-control search-textbox" id="search" placeholder="Search for Role...">
                    <br>
                    <div id="divRoles">

                            <!-- <input type="checkbox" name="roles[]" :value="role.id" id="checkboxUntick"> {{role.Job_Role_Name}} -->

                        <p v-show="noRole">No such role</p>
                    </div>
                </div>
                <div class="modal-footer">
                    <button class="btn pink-button" :data-bs-target="'#back-button'" data-bs-toggle="modal">Confirm</button>
                </div>
            </div>
        </div>
    </div>

    <div class="modal fade" :id="'back-button'" aria-hidden="true" aria-labelledby="exampleModalToggleLabel2" tabindex="-1">
        <div class="modal-dialog modal-dialog-centered">
            <div class="modal-content">
                <div class="modal-header">
                    <h1 class="modal-title fs-5" id="exampleModalToggleLabel2">Confirmation</h1>
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                <div class="modal-body">
                    You have successfully the role. 
                </div>
                <div class="modal-footer">
                    <button class="btn pink-button" :data-bs-target="'#edit-button'+staffID" data-bs-toggle="modal">Back</button>
                </div>
            </div>
        </div>
    </div>
    <a class="btn btn-sm" data-bs-toggle="modal" :href="'#edit-button'+staffID" role="button"><font-awesome-icon icon="fa-solid fa-pen-to-square" style="padding: 10px 0px; margin-left: -50px; color: white;"/>
</a>
</template>

<script>
    import axios from 'axios';

    export default{
        data(){
            return{
                noRole: false,
                roles: [],
                existingRoles: [],
                selectedRoles: []
            }
        },
        created(){
            const reqOne = axios.get('http://127.0.0.1:5000/req/140002/')
            const reqTwo = axios.get('/job_role/')
            axios.all([reqOne, reqTwo])
            .then(axios.spread((...responses) => {
                const responseOne = responses[0].data
                const responseTwo = responses[1].data
                
                console.log(responseOne)

                responseOne.forEach(role =>
                this.existingRoles.push(role.Job_Role.Job_Role_Name))

                this.roles = responseTwo

                // console.log(this.existingRoles)
                this.ifChecked();
                console.log(this.roles)

            }
            ))
            .catch(error => alert(error)) 


        },

        methods:{
            ifChecked: function(){
                // console.log(this.roles)
                
                var jobList = ""
                this.roles.forEach(role => {
                    if(this.existingRoles.includes(role.Job_Role_Name)){
                        jobList += `<div> <input type='checkbox' name='roles[]' :value='role.id' checked> `  + role.Job_Role_Name + `</div>`
                        this.selectedRoles += role.Job_Role_id

                    }else{
                        jobList += `<div> <input type='checkbox' name='roles[]' :value='role.id'> `  + role.Job_Role_Name + `</div>`

                    }
                    // console.log(role.Job_Role_Name)
                    // console.log(this.existingRoles)
                    
                    console.log(this.existingRoles.includes(role.Job_Role_Name))

            })
            document.getElementById("divRoles").innerHTML = jobList
        },
        updateRoles: function(){
            //loop through checkbox values

        },
        // updateRequirementsDB: function(){
        //     axios.put("http://127.0.0.1:5000/req/" + this.props.staffID + "/", {
    //                     "id": this.skillname,
    //                     "Job_Role_id": this.role,
    //                     "Staff_id": this.staffID
    //                 })
    //                 .then(response => {
    //                     console.log(response.data);
    //                     console.log(this.skillname);
    //                 })
    //                 .catch(error =>{
    //                     console.log(error.message);
    //     })
        
    // },


            searchFunction: function () {
                var input, filter, divRoles, roleName, i, txtValue;
                input = document.getElementById("search");
                filter = input.value.toUpperCase();
                divRoles = document.getElementById("divRoles").getElementsByTagName("div");
                
                var hideCount = 0;
                for (i = 0; i < divRoles.length; i++) {
                    roleName = divRoles[i];

                    if (roleName) {
                    txtValue = roleName.getElementsByTagName("input")[0].value;
                    console.log(txtValue)
                    if ((txtValue.toUpperCase().indexOf(filter) > -1)) {
                        divRoles[i].style.display = "";
                    } else {
                        divRoles[i].style.display = "none";
                        hideCount += 1;
                    }
                    }
                }
                if (hideCount == divRoles.length){
                    this.noRole = true;
                }else{
                    this.noRole = false;
                }
            }



            }
        
        
        }
</script>

<script setup>
    const props = defineProps({
        roles: Object,
        staffID: Number
        // existingRoles: Object
    })    
</script>

<style scoped>
    *{
        color: black;
    }
    
    #search{
        border-color: #2F2FFA;
    }
    
    #search::placeholder{
        color: #2F2FFA;
    }

    .search-textbox:focus{
        box-shadow: #F64C72;
    }
    
    .pink-button{
    background-color: #F64C72;
    color: white;
    }

    .pink-button:hover{
        background-color: #F64C72;
        color: black;
    }
</style>