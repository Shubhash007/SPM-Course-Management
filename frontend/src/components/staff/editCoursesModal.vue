<template>
    <div class="modal fade" :id="'edit-button'+no+skillSelected" aria-hidden="true" aria-labelledby="first-modal" tabindex="-1">
        <div class="modal-dialog modal-dialog-centered">
            <div class="modal-content">
                <div class="modal-header">
                    <h1 class="modal-title fs-5" id="first-modal">Drop Courses</h1>
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                <div class="modal-body">
                    <div v-for="eachcourse in coursesSelected">
                        <input type="checkbox" name="courses[]" @change="checkeditem(eachcourse)" :id='eachcourse' :value="eachcourse"> {{eachcourse}}
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
    import axios from 'axios'
    const props = defineProps({
        coursesSelected: Object,
        no: Number,
        skillSelected: String,
        deleting: String,
        jobrole: Object,
    })


    const checkeditem = function(course_selected){
        var checked = document.getElementById(course_selected)
        get_data(course_selected)
    }
    
    let regcourse
    async function get_data(course_selected) { 
    try {
        var checked = document.getElementById(course_selected)
        console.log(checked.value)
        if (checked.checked == true){
            var checkBox = checked.value;
            for (let obj in props.coursesSelected){
                if (props.coursesSelected[obj] == checked.value){
                    console.log(checked.value)
                    props.coursesSelected.indexOf(checked.value)
                    console.log(props.coursesSelected.indexOf(checked.value))
                    props.coursesSelected.splice(props.coursesSelected.indexOf(checked.value), 1)
                    console.log(typeof(props.coursesSelected))
                    regcourse = Object.values(props.coursesSelected)
                    console.log(regcourse)
                }
                
            }
            let Course_Registered = {'Course_Registered': regcourse}
            console.log(Course_Registered)
            let id = localStorage.getItem("staff_id");
            console.log(id)
            const response = await axios.put('http://127.0.0.1:5000/req/'+id+'/'+props.jobrole['Job_Role_ID'] + '/', Course_Registered);
        }

        } catch (error) {
            alert(`DB is inaccesible at the moment due to ${error.message}`);
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
    
    .pink-button{
    background-color: #F64C72;
    color: white;
    }

    .pink-button:hover{
        background-color: #F64C72;
        color: black;
    }
</style>