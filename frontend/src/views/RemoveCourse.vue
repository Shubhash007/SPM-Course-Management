<template>
  <NavBar></NavBar>
  <div style="min-height: 80vh">
    <div class="row g-3" style="margin: 20px 50px"></div>
    <div class="accordion" id="accordionExample">
      <div class="accordion-item"  v-for="(role, index) in roles">
        <h2 class="accordion-header" id="headingOne">
          <button class="accordion-button" type="button" data-bs-toggle="collapse" data-bs-target="#collapseOne" aria-expanded="true" aria-controls="collapseOne">
            <div>
              <h3>
                {{role.RoleName}}
              </h3>
            </div>
          </button>
        </h2>
        <div id="collapseOne" class="accordion-collapse collapse show" aria-labelledby="headingOne" data-bs-parent="#accordionExample">
          <div class="accordion-body">
            
              <ul>
                <li  v-for="(item, index) in role.items">
                  
                  {{item.message}}
                  
                    <button type="button" class="btn btn-primary btn-sm">Small button</button>
                  
                  
                </li>
                
              </ul>
            
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script setup>
    import NavBar from '../components/NavBar.vue';
</script>
<script>
export default {
  data() {
    return {
      roles: [
        {
          RoleName:"Software Enginner",
          items: [{ message: 'Foo' }, { message: 'Bar' }]
        },
        {
          RoleName:"Consultant",
          items: [{ message: 'Foor' }, { message: 'Baar' }]
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
