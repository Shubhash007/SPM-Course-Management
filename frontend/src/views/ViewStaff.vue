<template>
  <NavBar></NavBar>
  <div style="min-height: 80vh">
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
          <th scope="col">S/N</th>
          <th scope="col">Staff Name(s)</th>
          <th scope="col">Job Roles</th>
          <th scope="col"></th>
          <!-- <th></th> -->
        </tr>
      </thead>
      <tbody id="tbody">
        <tr v-for="staff in staffList">
          <td scope="row" style="color: #2f2ffa">1</td>
          <td>{{ staff.name }}</td>
          <td>{{ staff.roles.toString() }}</td>
          <td>
            <a href="/StaffProfile" class="btn filter-button">View Profile</a>
          </td>
          <!-- <td width="150px"><button href="#" class="btn filter-button" style="transform: scale(0.7); margin: -10px;">Assign Role</button></td> -->
        </tr>
      </tbody>
    </table>
  </div>
</template>
<script>
import NavBar from '../components/NavBar.vue';
export default {
    data() {
        return {
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
        };
    },
    methods: {
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
    },
    components: { NavBar }
};
</script>

<style scoped>
#filter {
  border-color: #2f2ffa;
}

#filter::placeholder {
  color: #2f2ffa;
}

.filter-textbox:focus {
  box-shadow: #f64c72;
}

.filter-button {
  background-color: #f64c72;
  color: white;
}

.filter-button:hover {
  background-color: #f64c72;
  color: black;
}
td {
  color: #2f2ffa;
}
</style>
