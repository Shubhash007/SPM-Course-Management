<template>
    <div class="modal fade" :id="'add-button'+i+SkillSelected" aria-hidden="true" aria-labelledby="second-modal" tabindex="-1">
        <div class="modal-dialog modal-dialog-centered">
            <div class="modal-content">
                <div class="modal-header">
                    <h1 class="modal-title fs-5" id="second-modal" style="margin-top: auto; color: #d8648b;">Add Courses</h1>
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                <div class="modal-body"> 
                    <div v-for="eachcourse in availableCourses">
                        <input type="checkbox" name="Courses[]" v-model="Courses" :id='eachcourse' :value="eachcourse"> {{eachcourse}}
                    </div>
                </div>
                <div class="modal-footer">
                    <button class="btn pink-button" :data-bs-target="'#back-button'+i+SkillSelected" data-bs-toggle="modal" @click="addCourse()">Confirm</button>
                </div>
            </div>
        </div>
    </div>
    <a class="btn btn-sm pink-button" data-bs-toggle="modal" :href="'#add-button'+i+SkillSelected" role="button" style="margin-top: 10px; margin-left: 77%;">Add Course</a>
</template>

<script setup>
    import axios from 'axios'
    const props = defineProps({
        CoursesSelected: Object, 
        i: Number, 
        Jobrole: Object, 
    })
</script>
<script>
    export default{
        data(){
            return{
                availableCourses: [],
                Courses: []
            }
        },methods:{
            addCourse:function(){
                let staffid = localStorage.getItem('staff_id');
                let jobroleid = this.props.Jobrole.Job_Role_ID;
                let courseCodes = [];
                for (let eachCourse of this.Courses){
                    let courseCode = eachCourse.split(' ')[0];
                    courseCodes.push(courseCode);
                }
                for (let courseRegisted of this.props.CoursesSelected){
                    courseCodes.push(courseRegisted);
                }
                if (this.Courses.length == 0){
                    alert('Select at least one course');
                }else{
                    let apiCourse = {'Course_Registered': courseCodes};
                    axios.put('http://127.0.0.1:5000/req/' + staffid + '/' + jobroleid + '/' , apiCourse)
                    .then(response => {
                        console.log(response.data);
                        alert('Courses has been successfully added');
                    }).catch(error => {
                        console.log(error.message);
                    })
                    window.location = "\EditLearningJourneys";
                }
            }
            
        },
        created(){
            axios.get("/registration/")
            .then(response => {
                let data = response.data;
                let coursesCompleted = [];
                for (let item of data){
                    if (item.Staff == localStorage.getItem("staff_id") && item.Completion_Status == "Completed"){
                        coursesCompleted.push(item);
                    }
                }
                let chosenCourses = JSON.parse(JSON.stringify(this.props.CoursesSelected));
                console.log(this.props.Jobrole.Skills);
                for (let skill of this.props.Jobrole.Skills){
                    for (let course of skill.courses){
                        let aList = course.split(',');
                        if (aList[2] == "Active" && chosenCourses.indexOf(aList[0]) < 0){
                            this.availableCourses.push(aList[0]);
                        }
                    }
                }
                console.log(this.availableCourses);
                for (let course of coursesCompleted){                   
                    if (this.availableCourses.includes(course.Course)){
                        let index = this.availableCourses.indexOf(course.Course);
                        console.log(index);
                        this.availableCourses.splice(index, 1);
                    }
                }
                console.log(this.availableCourses);
            })
            .catch(error => {
                console.log(error.message);
            })
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
        box-shadow: #d8648b;
    }
    
    .pink-button{
    background-color: #d8648b;
    color: white;
    }

    .pink-button:hover{
        background-color: #d8648b;
        color: black;
    }
</style>