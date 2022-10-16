<template style="min-height: 100vh;">
    <div class="card w-75">
        <div class="card-body">

            <h1 class="card-title">{{profile.Name}}</h1>
            <h6>{{profile.Email}}</h6>
            <br>

            <div class="row">
                <div class="col-sm">
                <h5 class="card-title">Staff Particulars</h5>
                <p class="card-text">
                    <ul>
                        <li>Staff ID: {{profile.StaffID}}</li>
                        <li>Department: {{profile.Department}}</li>
                    </ul>
                </p>
                </div>
                
                <div class="col-sm">
                <h5 class="card-title">Skills Attained</h5>
                <p class="card-text">
                    <ul>
                        <li v-for="skill in profile.Skills">{{skill}}
                        </li>
                    </ul>
                </p>
                </div>
                <div class="col-sm">
                <h5 class="card-title">Current Roles</h5>
                <p class="card-text">
                    <ul>
                        <li v-for="role in profile.Roles">{{role}}</li>
                    </ul>
                </p>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    import axios from 'axios';
    export default{
        data(){
            return{
                profile: 
                    {
                        StaffID: "",
                        Name: "",
                        Department: "",
                        Email: "",
                        Skills: ["Python", "PHP"],
                        Roles: ["Software Engineer", "Developer"]
                    }
            }
        },
        mounted(){
            const slug = this.$route.params.slug; 
            axios.get(`/staff/${slug}`)
            .then(response => {
                // console.log(response.data);
                this.profile.StaffID = response.data.Staff_ID;
                this.profile.Name = response.data.Staff_FName + " " + response.data.Staff_LName;
                this.profile.Department = response.data.Dept;
                this.profile.Email = response.data.Email;
            })
        }
    }
</script>

<style scoped>
    .card{
        margin: 10px auto;
        border-color: white;
    }

    .card-body{
        background-color: #2F2FFA;
        color: white;
        padding: 20px 35px;
        border-radius: 10px;
    }

    .card-title{
        padding: 10px 0px;
    }
    
    .col-auto{
        display: inline-block;
        margin-right: 15%;
    }

    .title-header{
        font-size: 1rem;
        color: #F64C72;
    }
    
    h5{
        color: #F64C72;
    }

    #spacing{
        padding-right: 42px;
    }
</style>
