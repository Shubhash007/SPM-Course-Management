<template>
    <div class="row p-5" id="row">
        <div class="col-sm-6">
            <div class="card">
            <div class="card-body">
                <h5 class="card-title">Create a New Role</h5>
                <p class="card-text">Input a new role into the system. You will not be able to create an existing role.</p>
                <button @click.prevent='CreateRole()' class="btn" id="card-button">Create Role</button>
            </div>
            </div>
        </div>
        <div class="col-sm-6">
            <div class="card">
            <div class="card-body">
                <h5 class="card-title">Create a New Skill</h5>
                <p class="card-text">Input a new skill into the system. You will not be able to create an existing skill.</p>
                <a href="#" class="btn" id="card-button">Create Skill</a>
            </div>
            </div>
        </div>
    </div>
</template>
<script>
    export default{
        methods:{
            CreateRole(){
                this.$router.push('/CreateRole')
            }
        }
    }
</script>