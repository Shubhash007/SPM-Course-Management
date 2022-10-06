<template>
    <nav class="navbar navbar-expand-lg">
    <div class="container-fluid">
      <a class="navbar-brand" href="#">INSERT LOGO HERE</a>
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarSupportedContent">
        <ul class="navbar-nav me-auto mb-2 mb-lg-0">
          <li class="nav-item ms-5">
            <router-link to="HRHome" class="nav-link" aria-current="page">HOME</router-link>
          </li>
          <li class="nav-item ms-5">
            <router-link to="StaffHome" class="nav-link" aria-current="page">HOME(STAFF)</router-link>
          </li>
          <li class="nav-item ms-5">
            <router-link to="StaffProfile" class="nav-link" aria-current="page">ACCOUNT</router-link>
          </li>
        </ul>
        <button type="button" class="btn btn-primary navbar-button" id="navbar-login">Login</button>
        <button type="button" class="btn btn-outline-primary navbar-button" id="navbar-signup">Sign Up</button>
        
      </div>
    </div>
  </nav>
</template>