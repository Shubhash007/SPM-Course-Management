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
    <table
      class="table table-responsive"
      style="width: 75%; border-color: #2f2ffa; margin: 20px 60px"
      border="#2F2FFA"
    >
      <thead>
        <tr>
          <th scope="col">S/N</th>
          <th scope="col">Job Roles</th>
          <th scope="col">Staff Name(s)</th>
          <!-- <th></th> -->
        </tr>
      </thead>
      <tbody>
        <tr v-for="(role, index) in roles">
          <th scope="row" style="color: #2f2ffa">1</th>
          <td>{{ role.RoleName }}</td>
          <td>{{ role.StaffNames.toString() }}</td>
          <!-- <td width="150px"><button href="#" class="btn filter-button" style="transform: scale(0.7); margin: -10px;">Assign Role</button></td> -->
        </tr>
      </tbody>
    </table>
  </div>
</template>
<script>
export default {
  data() {
    return {
      roles: [
        {
          RoleName: "Software Enginner",
          StaffNames: ["Mary Lamb", "Mary Cow"],
        },
        {
          RoleName: "Consultant",
          StaffNames: ["Bob Tan", "Benjamin Toh"],
        },
      ],
    };
  },
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
