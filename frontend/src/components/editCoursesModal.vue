<template>
    <div class="modal fade" :id="'edit-button'+no+skillSelected" aria-hidden="true" aria-labelledby="first-modal" tabindex="-1">
        <div class="modal-dialog modal-dialog-centered">
            <div class="modal-content">
                <div class="modal-header">
                    <h1 class="modal-title fs-5" id="first-modal">Edit Courses</h1>
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                <div class="modal-body">
                    <!-- <div v-for="eachcourse in coursesSelected">
                        <input type="checkbox" name="courses[]" @change="checkeditem()" id='course' :value="eachcourse"> {{eachcourse}}
                    </div> -->
                    <div>
                        <input type="checkbox" name="courses[]" @change="checkeditem()" id='course' :value="coursesSelected"> {{coursesSelected}}
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
        coursesSelected: String,
        no: Number,
        skillSelected: String,
        deleting: String,
        jobrole: Object
    })

    const checkeditem = function(){
        var checkBox = document.getElementById("course").value;
        console.log(checkBox)
        console.log(props.jobrole['Job_Role']['Job_Role_ID'])
        get_data()
    }


    async function get_data() { 
    try {
        var checked = document.getElementById("course")
        console.log(checked.value)
        if (checked.checked == true){
            var checkBox = checked.value;
            console.log(checkBox)
            let splitcourse = checkBox.split(':')
            console.log(splitcourse)
            let id = localStorage.getItem("staff_id");
            console.log(id)
            const response = axios.delete('http://127.0.0.1:5000/req/'+id+'/'+props.jobrole['Job_Role']['Job_Role_ID'] + '/' +splitcourse[0] + '/');
        }
            
        

        // for (let item in res) {
        //   data.skills_data = res[item].Job_Role['Skills']
        // }
        
        // console.log(typeof(data.skills_data))
        
        
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