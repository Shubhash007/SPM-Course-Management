<template>
    <div class="modal fade" :id="'add-button'+i+SkillSelected" aria-hidden="true" aria-labelledby="second-modal" tabindex="-1">
        <div class="modal-dialog modal-dialog-centered">
            <div class="modal-content">
                <div class="modal-header">
                    <h1 class="modal-title fs-5" id="second-modal">Add Courses</h1>
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                <div class="modal-body"> 
                    <div v-for="eachcourse in CoursesSelected">
                        <input type="checkbox" name="Courses[]" @change="checkeditem(eachcourse)" :id='eachcourse' :value="eachcourse"> {{eachcourse.split(',')[0]}}
                        <div type ="hidden" style="display: none;visibility: hidden;" id="jobroleid">{{jobroleid}}</div>
                    </div>
                </div>
                <div class="modal-footer">
                    Click on the checkbox to add course to learning journey!
                </div>
            </div>
        </div>
    </div>

    
    <a class="btn btn-sm pink-button" data-bs-toggle="modal" :href="'#add-button'+i+SkillSelected" role="button">Add Course</a>
</template>

<script setup>
    import axios from 'axios'
    const props = defineProps({
        CoursesSelected: Object,
        i: Number,
        SkillSelected: String,
        JobRole: Object,
        jobroleid:Number,
    })


    const checkeditem = function(CoursesSelected){
        var checked = document.getElementById(CoursesSelected)
        get_data(CoursesSelected)
    }
    
    let regcourse
    async function get_data(CoursesSelected) { 
    try {
        var checked = document.getElementById(CoursesSelected)
        console.log(checked.value)
        if (checked.checked == true){
            var checkBox = checked.value;
            for (let obj in props.CoursesSelected){
                if (props.CoursesSelected[obj] == checked.value){
                    console.log(checked.value)
                    props.CoursesSelected.indexOf(checked.value)
                    console.log(props.CoursesSelected.indexOf(checked.value))
                    props.CoursesSelected.splice(props.CoursesSelected.indexOf(checked.value), 1)
                    console.log(typeof(props.CoursesSelected))
                    regcourse = Object.values(props.CoursesSelected)
                    regcourse.push(checked.value.split(',')[0])
                    console.log(regcourse)

                }
                
            }
            let Course_Registered = {'Course_Registered': regcourse}
            console.log(Course_Registered)
            let id = localStorage.getItem("staff_id");
            console.log(id)
            let jrid = document.getElementById('jobroleid')
            console.log(jrid.innerText)
            const response = await axios.put('http://127.0.0.1:5000/req/'+id+'/'+jrid.innerText + '/', Course_Registered);
            if(response.status == 200)
                            {
                                alert("Course Added!")
                            }        }
        

        } catch (error) {

             if (error.response.status == 400){
                alert("Learning Jounrey already exists!")
            }

            else if(error.response.status == 200){
                alert("Course Added!")
            }
            else{
             alert(`DB is inaccesible at the moment due to ${error.message}`)
             console.log(error.response);
        }
        
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