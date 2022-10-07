<template>
  <div style="min-height: 80vh">
    <div class="row g-3" style="margin: 20px 50px">
      <div class="col-auto">
        <label for="filter" class="visually-hidden">Filter</label>
        <input
          type="text"
          class="form-control filter-textbox"
          id="filter"
          placeholder="Filter by Job Role..."
        />
      </div>
      <div class="col-auto">
        <button type="submit" class="btn filter-button mb-3">Filter</button>
      </div>
    </div>
        <table class="table table-responsive" style="width: 75%; border-color: #2F2FFA; margin: 20px 60px;" border="#2F2FFA">
            <thead>
                <tr>
                <th scope="col">S/N</th>
                <th scope="col">Staff Name</th>
                <th scope="col">Job Role</th>
                <!-- <th></th> -->
                </tr>
            </thead>
            <!-- <tbody v-if="hasSearch">
                <tr v-for="(employee, index) in returnData">
                    <th scope="row" style="color: #2F2FFA">{{index+1}}</th>
                    <td>{{ employee.Staff }}</td>
                    <td>{{ employee.Role }}</td> -->
                    <!-- <td width="150px"><button href="#" class="btn search-button" style="transform: scale(0.7); margin: -10px;">Assign Role</button></td> -->
                <!-- </tr>
            </tbody> -->
            <tbody id="tbody">
                <tr v-for="(employee, index) in employees">
                    <th scope="row" style="color: #2F2FFA">{{index+1}}</th>
                    <td>{{ employee.Staff }}</td> <!--link to staff profile page-->
                    <td>{{ employee.Role }}</td> 
                    <!-- <td width="150px"><button href="#" class="btn search-button" style="transform: scale(0.7); margin: -10px;">Assign Role</button></td> -->
                </tr>
            </tbody>
        </table>
    </div>
  </div>
</template>
<script>
    export default{
        data(){
            return{
                employees: [
                    {
                        Role: "Software Engineer",
                        Staff: "Mary Lamb"
                    },
                    {
                        Role: "Software Engineer",
                        Staff: "Mary Cow"
                    },
                    {
                        Role: "Consultant",
                        Staff: "Bob Tan"
                    },
                    {
                        Role: "Consultant",
                        Staff: "Benjamin Toh"
                    }
                ],
                category: "Category",
                keyword: "",
                hasSearch: false,
                returnData: []
            }
        }, methods:{
            searchButton:function(){
                let text = this.keyword;
                let category = this.category;

                if (text != "" && category != "Category"){
                    this.hasSearch = true;
                }
                this.returnData = [];
                for (var employee in this.employees){
                    if(category == "staff"){
                        if(employee.Staff == text || text.includes(employee.Staff)){
                            this.returnData.push(employee);
                        }
                    }else if(category == "role"){
                        if(employee.Role == text || text.includes(employee.Role)){
                            this.returnData.push(employee);
                        }
                    }
                }
                this.hasSearch = false;
                return this.returnData;
            },

            searchFunction: function () {
                var input, filter, table, tbody, tr, tdName, tdRoles, i, txtValue;
                input = document.getElementById("search");
                filter = input.value.toUpperCase();
                table = document.getElementById("roles");
                tbody = document.getElementById("tbody");
                tr = tbody.getElementsByTagName("tr");

                for (i = 0; i < tr.length; i++) {
                    tdName = tr[i].getElementsByTagName("td")[0];
                    tdRoles = tr[i].getElementsByTagName("td")[1];
                    if (tdName && tdRoles) {
                    txtValue = [tdName.textContent, tdRoles.textContent];
                    console.log(txtValue)
                    if ((txtValue[0].toUpperCase().indexOf(filter) > -1) || (txtValue[1].toUpperCase().indexOf(filter) > -1)) {
                        tr[i].style.display = "";
                    } else {
                        tr[i].style.display = "none";
                    }
                    }
                }
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

    .category-dropdown{
        border-color: #F64C72;
        color: #F64C72;
    }

    .category-dropdown:hover{
        border-color: #F64C72;
        color: black
    }

    .category-dropdown:focus{
        border-color: #F64C72;
        color: black;
        box-shadow: none;
    }
    
    .search-button{
        background-color: #F64C72;
        color: white;
    }

    .search-button:hover{
        background-color: #F64C72;
        color: black;
    }
    td{
        color: #2F2FFA;
    }
</style>