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
                    <div v-for="each in eachcourse.courses">
                        <input type="checkbox" name="Courses[]"  @change="checkeditem(each.split(',')[0])" :id="each.split(',')[0]" :value="each" :class="each.split(',')[0]"> {{each.split(',')[0]}}
                        <div type ="hidden" style="display: none;visibility: hidden;" id="jobroleid">{{jobroleid}}</div>

                    </div>
                </div>
                </div>
                <div class="modal-footer">
                    <button class="btn pink-button" :data-bs-target="'#back-button'+i+SkillSelected" data-bs-toggle="modal" @click="get_data()">Confirm</button>
                </div>
            </div>
        </div>
    </div>

    
    <a class="btn btn-sm pink-button" data-bs-toggle="modal" :href="'#add-button'+i+SkillSelected" role="button">Add Course</a>
</template>

<script setup>
    // import { TextModes } from '@vue/compiler-core';
import axios from 'axios'
    const props = defineProps({
        CoursesSelected: Object,
        i: Number,
        SkillSelected: String,
        JobRole: Object,
        jobroleid:Number,
        checkcourse:Object,
        
    })





    let item = []
    const checkeditem = function(course_selected){
        console.log(course_selected)
 

        // console.log(course_selected)
        // item.push(course_selected)
        // console.log(item)
    }
    
    let regcourse
        async function get_data() { 

        try {

    

            for (let i in item){
                for (let obj in props.CoursesSelected){
                    console.log(item[i])
                    console.log(props.CoursesSelected[obj].courses)
                    if (props.CoursesSelected[obj] == item[i]){
                        props.CoursesSelected.indexOf(item[i])
                        props.CoursesSelected.splice(props.CoursesSelected.indexOf(item[i]), 1)
                        console.log(typeof(props.CoursesSelected))
                        regcourse = Object.values(props.CoursesSelected)
                        console.log(regcourse)
                        
                    }

            let Course_Registered = {'Course_Registered': regcourse}
            console.log(Course_Registered)
            let id = localStorage.getItem("staff_id");
            console.log(regcourse.length)
        //     let jrid = document.getElementById('jobroleid')
        //     console.log(jrid.innerText)
        //     const response = await axios.put('http://127.0.0.1:5000/req/'+id+'/'+jrid.innerText + '/', Course_Registered);
        //     if(response.status == 200)
        //                     {
        //                         alert("Course Added!")
        //                     }        }
        
            }}

         } catch (error) {console.log(error)}}

        //      if (error.response.status == 400){
        //         alert("Learning Jounrey already exists!")
        //     }

        //     else if(error.response.status == 200){
        //         alert("Course Added!")
        //     }
        //     else{
        //      alert(`DB is inaccesible at the moment due to ${error.message}`)
        //      console.log(error.response);
        // }
    Checking()

    async function Checking(){
        // var check = document.getElementById(course_selected)
        for (let obj in props.CoursesSelected){
            for(let i in props.CoursesSelected[obj].courses){
        // console.log(props.CoursesSelected[obj].courses[i].split(',')[0])
                let onecourse = props.CoursesSelected[obj].courses[i].split(',')[0];
                    if(props.checkcourse.length>0){
                        for( let indcourse in props.checkcourse){
                        // console.log(props.checkcourse[indcourse])
                            if(props.checkcourse[indcourse]==onecourse){
                                    // console.log(props.CoursesSelected[obj].courses[i])
                                    props.CoursesSelected[obj].courses[i]='-'
   
                                                            
                                    // console.log(props.CoursesSelected[obj].courses[i])


                                    }


                                }
                            

                            }


            // console.log(onecourse)
            }
        }
        
    }
    RemoveEmptyCheckbox()
    RemoveCheckbox() 

 



     async function RemoveEmptyCheckbox(){
        

        var temp = document.getElementById('-')
        if(temp!=null){
            temp.remove()
        }
 




        



    }

    async function RemoveCheckbox(){

        for (let obj in props.CoursesSelected){
            for(let i in props.CoursesSelected[obj].courses){
                let onecourse = props.CoursesSelected[obj].courses[i].split(',')[0];
                if(onecourse=='-'){
                    props.CoursesSelected[obj].courses[i]='   '
       
                }

        // console.log(props.CoursesSelected[obj].courses[0])

                    }
                }



                var y = document.getElementById('   ')
                console.log(y)
                y.remove()
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