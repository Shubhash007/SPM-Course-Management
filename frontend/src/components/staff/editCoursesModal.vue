<template>
    <div class="modal fade" :id="'edit-button'+no+skillSelected" aria-hidden="true" aria-labelledby="first-modal" tabindex="-1">
        <div class="modal-dialog modal-dialog-centered">
            <div class="modal-content">
                <div class="modal-header">
                    <h1 class="modal-title fs-5" style="margin-top: 5px;" id="first-modal">Drop Courses</h1>
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                <div class="modal-body">
                    <div v-for="eachcourse in coursesSelected">
                        <input type="checkbox" name="courses[]" @change="checkeditem(eachcourse)"  :id='eachcourse' :value="eachcourse"> {{eachcourse}}
                    </div>
                </div>
                <div class="modal-footer" id="test">
                    <button class="btn pink-button" :data-bs-target="'#back-button'+no+skillSelected" data-bs-toggle="modal" @click="get_data()">Confirm</button>
                </div>
            </div>
        </div>
    </div>

    <!-- <div class="modal fade" :id="'back-button'+no+skillSelected" aria-hidden="true" aria-labelledby="exampleModalToggleLabel2" tabindex="-1">
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
    </div> -->
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

    let item = []
    const checkeditem = function(course_selected){
        var checked = document.getElementById(course_selected)
        if (checked.checked == true){
            console.log(checked.value)
            item.push(checked.value)
            
        }
        else{
            console.log('hi')
            item.splice(item.indexOf(checked.value), 1)
        }
        console.log(item)
    }
    
    let regcourse
    // async function get_data(course_selected) { 
    // try {
        
    //     var checked = document.getElementById(course_selected)
    //     console.log(checked.value)
    //     console.log(regcourse)
        
    //         if (props.coursesSelected.length > 1){
    //             if (checked.checked == true){
    //                 var checkBox = checked.value;
    //                 for (let obj in props.coursesSelected){
    //                     if (props.coursesSelected[obj] == checked.value){
    //                         console.log(checked.value)
    //                         props.coursesSelected.indexOf(checked.value)
    //                         console.log(props.coursesSelected.indexOf(checked.value))
    //                         props.coursesSelected.splice(props.coursesSelected.indexOf(checked.value), 1)
    //                         console.log(typeof(props.coursesSelected))
    //                         regcourse = Object.values(props.coursesSelected)
    //                         console.log(regcourse)
    //                         }
    //                     }
                        
    //                 let Course_Registered = {'Course_Registered': regcourse}
    //                 console.log(Course_Registered)
    //                 let id = localStorage.getItem("staff_id");
    //                 console.log(regcourse.length)
    //                 const response = await axios.put('http://127.0.0.1:5000/req/'+id+'/'+props.jobrole['Job_Role_ID'] + '/', Course_Registered);
    //                 }
    //         }
    //         else {
    //             alert(`Unable to delete course. Learning Journey needs to have at least one course.`);
    //             document.getElementById(course_selected).checked = false;
    //             window.location = "\EditLearningJourneys"
    //         }

    //     } catch (error) {
    //         alert(`DB is inaccesible at the moment due to ${error.message}`);
    //         document.getElementById(course_selected).checked = false;
            
    //     }
        
    // }
    const dropcourse = function(){
    if (item.length == 0) {
        alert(`Please select a course to drop`);
        window.location = "\EditLearningJourneys"

    }
    else{
        alert(`Successfully dropped courses!`);
        window.location = "\EditLearningJourneys"
    }
}

    async function get_data() { 

    try {
    
        
            if (props.coursesSelected.length > 1){
                for (let i in item){
                    console.log(item[i])
                    for (let obj in props.coursesSelected){
                        if (props.coursesSelected[obj] == item[i]){
                            props.coursesSelected.indexOf(item[i])
                            props.coursesSelected.splice(props.coursesSelected.indexOf(item[i]), 1)
                            console.log(typeof(props.coursesSelected))
                            regcourse = Object.values(props.coursesSelected)
                            console.log(regcourse)
                            }
                        }

                let Course_Registered = {'Course_Registered': regcourse}
                console.log(Course_Registered)
                let id = localStorage.getItem("staff_id");
                console.log(regcourse.length)
                const response = await axios.put('http://127.0.0.1:5000/req/'+id+'/'+props.jobrole['Job_Role_ID'] + '/', Course_Registered);
                        
                }
                dropcourse()
            }
            
            else if (props.coursesSelected.length == 1){
                alert(`Unable to delete course. Learning Journey needs to have at least one course.`);
                window.location = "\EditLearningJourneys"
            }


        } catch (error) {
            alert(`DB is inaccesible at the moment due to ${error.message}`);

            
        }
        
    }

</script>
<script>
    export default{
        methods:{
            filterCompletedCourses: function(){
                axios.get("/registration/")
                .then(response => {
                    let data = response.data;
                    let coursesCompleted = [];
                    for (let item of data){
                        if (item.Staff == localStorage.getItem("staff_id") && item.Completion_Status == "Completed"){
                            coursesCompleted.push(item);
                        }
                    }
                    for (let course of coursesCompleted){
                        if (this.props.coursesSelected.includes(course.Course)){
                            let index = this.props.coursesSelected.indexOf(course.Course);
                            this.props.coursesSelected.splice(index, 1);
                        }
                    }
                })
                .catch(error => {
                    console.log(error.message);
                })
            }
        },
        created(){
            this.filterCompletedCourses();
        }
    }
</script>

<style scoped>
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