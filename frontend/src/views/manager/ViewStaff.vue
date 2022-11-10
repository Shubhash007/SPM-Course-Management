<template>
  <NavBar v-if="userRole == 3 || userRole == 1"></NavBar>
  <div style="min-height: 80vh" v-if="userRole == 3 || userRole == 1">
    <div class="row g-3" style="margin: 20px 50px">
      <div class="col-auto">
        <label for="search" class="visually-hidden">Search</label>
        <input
          type="text"
          @keyup="searchFunction"
          class="form-control filter-textbox"
          id="search"
          placeholder="Search for Staff"
        />
      </div>
    </div>
    <table
      id="staff"
      class="table table-responsive"
      style="width: 75%; border-color: #2f2ffa; margin: 20px 60px"
      border="#2F2FFA"
    >
      <thead>
        <tr>
          <th scope="col"></th>
          <th scope="col">Staff ID</th>
          <th scope="col">Staff Name(s)</th>
          <th scope="col"></th>
        </tr>
      </thead>


      
      <tbody id="tbody">
        <tr v-for="employee in employees">
          <td scope="row" style="color: #2f2ffa"></td>
          <td>{{employee.Staff_ID}}</td>
          <td>{{employee.Staff_FName}} {{employee.Staff_LName}}</td>
          <td>
            <a href="/StaffProfile" @click="staffProfile(employee.Staff_ID)" class="btn filter-button">View Profile</a>
          </td>
        </tr>
      </tbody>



    </table>
  </div>
  <Error v-else></Error>
</template>
<script>
import NavBar from '../../components/NavBar.vue';
import Error from '../../components/Error.vue';
import axios from "axios";
export default {
    data() {
        return {
            employees:[],
            staffList: [
                {
                    name: "Mary Lamb",
                    roles: ["Software Engineer"],
                },
                {
                    name: "John Doe",
                    roles: ["Developer"],
                },
            ],
            userRole: 0
        };
    },
    methods: {
        staffProfile:function(x){
          // console.log(x)
          sessionStorage.setItem("staffID", x);
        },

        searchFunction: function () {
            var input, filter, table, tbody, tr, td, i, txtValue;
            input = document.getElementById("search");
            filter = input.value.toUpperCase();
            table = document.getElementById("staff");
            tbody = document.getElementById("tbody");
            tr = tbody.getElementsByTagName("tr");
            for (i = 0; i < tr.length; i++) {
                td = tr[i].getElementsByTagName("td")[1];
                if (td) {
                    txtValue = td.textContent || td.innerText;
                    if (txtValue.toUpperCase().indexOf(filter) > -1) {
                        tr[i].style.display = "";
                    }
                    else {
                        tr[i].style.display = "none";
                    }
                }
            }
        },


        onload: async function(){
            this.userRole = localStorage.getItem("userRole")
            await axios.get('/staff/')
            .then(response => {
                // this.course = response.data.data;
                this.employees = response.data
                console.log(response.data)
                // console.log(this.employees[10].courses);
            })
            .catch(error => alert(error)) 

          
            },


        userAuthentication: function(){
          this.userRole = localStorage.getItem("userRole");
        }
    },


    mounted(){
      this.onload()
    },
    created() {
      this.onload()
    },
    // created(){
    //   this.userAuthentication()
    // },
    components: { NavBar }
};
</script>

<style scoped>
#filter {
  border-color: #d8648b;
}

#filter::placeholder {
  color: #d8648b;
}

.filter-textbox:focus {
  box-shadow: #f5b9c6c7;
}

.filter-button {
  background-color: #f5b9c6c7;
  color: white;
}

.filter-button:hover {
  background-color: #f5b9c6c7;
  color: black;
}
td {
  color: #d8648b;
}
</style>
