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
                        <div v-for="role in roles">
                            <input type="checkbox" name="roles[]" :value="role" id="checkbox"> {{role}}
                        </div>
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
    export default{
        data(){
            return{
                noRole: false
            }
        },
        methods:{
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
    })    
</script>

<style scoped>
    *{
        color: black;
    }
    
    #search{
        border-color: #d8648b;
    }
    
    #search::placeholder{
        color: #d8648b;
    }

    .search-textbox:focus{
        box-shadow: #f5b9c6c7;
    }
    
    .pink-button{
    background-color: #f5b9c6c7;
    color: white;
    }

    .pink-button:hover{
        background-color: #f5b9c6c7;
        color: black;
    }
</style>