<template>
    <div class="modal fade" :id="'edit-button'+no+skillSelected" aria-hidden="true" aria-labelledby="first-modal" tabindex="-1">
        <div class="modal-dialog modal-dialog-centered">
            <div class="modal-content">
                <div class="modal-header">
                    <h1 class="modal-title fs-5" id="first-modal">Edit Courses</h1>
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                <div class="modal-body">
                    <div v-for="eachcourse in coursesSelected">
                        <input type="checkbox" name="courses[]" :value="eachcourse"> {{eachcourse}}
                    </div>
                </div>
                <div class="modal-footer">
                    <button class="btn pink-button" :data-bs-target="'#back-button'+no+skillSelected" data-bs-toggle="modal">Confirm</button>
                </div>
            </div>
        </div>
    </div>

    <div class="modal fade" :id="'back-button'+no+skillSelected" aria-hidden="true" aria-labelledby="exampleModalToggleLabel2" tabindex="-1">
        <div class="modal-dialog modal-dialog-centered">
            <div class="modal-content">
                <div class="modal-header">
                    <h1 class="modal-title fs-5" id="exampleModalToggleLabel2">Confirmation</h1>
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                <div class="modal-body">
                    You have successfully edited your courses. 
                </div>
                <div class="modal-footer">
                    <button class="btn pink-button" :data-bs-target="'#edit-button'+no+skillSelected" data-bs-toggle="modal">Back</button>
                </div>
            </div>
        </div>
    </div>
    <a class="btn btn-sm pink-button" data-bs-toggle="modal" :href="'#edit-button'+no+skillSelected" role="button">Edit</a>
</template>

<script setup>
    const props = defineProps({
        coursesSelected: Object,
        no: Number,
        skillSelected: String,
    })
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
    
    .pink-button{
    background-color: #F64C72;
    color: white;
    }

    .pink-button:hover{
        background-color: #F64C72;
        color: black;
    }
</style>