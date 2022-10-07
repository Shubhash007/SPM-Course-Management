<template>
    <div class="card w-75">
        <div class="card-body">

            <h1 class="card-title">STAFF NAME</h1>
            <br><br>

            <div class="row">
                <div class="col-sm">
                <h5 class="card-title">Staff Particulars</h5>
                <p class="card-text">
                    <ul>
                        <li>Staff ID: {{profile.StaffID}}</li>
                        <li>Department: {{profile.Department}}</li>
                        <li>Email: {{profile.Email}}</li>
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
    export default{
        data(){
            return{
                profile: 
                    {
                        StaffID: "12345",
                        Department: "IT",
                        Email: "fwasung@<name>.com",
                        Skills: ["Python", "PHP"],
                        Roles: ["Software Engineer", "Developer"]
                    }
            }
        }
    }
</script>


<style scoped>
    /* Create Job Role */
    .card{
        margin: 10px auto;
    }

    .card-body{
        background-color: #2F2FFA;
        color: white;
        padding: 20px 35px;
    }

    .card-title{
        padding: 10px 0px;
    }

    h5{
        color: #F64C72;
    }

    #spacing{
        padding-right: 42px;
    }

</style>
