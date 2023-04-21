<template>
  <nav class="navbar navbar-expand-lg my-nav">
    <a class="navbar-brand title" href="#">WareAbouts</a>
    <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarTogglerDemo02"
      aria-controls="navbarTogglerDemo02" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>

    <div class="collapse navbar-collapse">
      <ul class="navbar-nav mr-auto mt-2 mt-lg-0">
        <li class="nav-item active">
          <a class="nav-link my-item" href="/">Home</a>
        </li>
      </ul>
      <div class="btns">
        <template v-if="$store.state.user.isAuthenticated">
          <router-link to="/dashboard/dash-home-page" class="dash-button">Dashboard</router-link>
        </template>

        <template v-else>
          <!-- <router-link to="/log-in" class="button">Login</router-link>
          <router-link to="/sign-up" class="button">Sign Up</router-link> -->
          <router-link to="/login-sign-up" class="button">Login / Sign Up</router-link>
        </template>
      </div>
    </div>
  </nav>
</template>

<script>
</script>

<style scoped>
.my-nav {
  background-color: #00B9AE;
  padding-left: 15px;
  padding-right: 15px;
}

.title {
  color: white;
  text-decoration: none;
}

.title:visited {
  color: white;
  text-decoration: none;
}

.title:hover {
  color: white;
}

.my-item {
  background-color: #00B9AE;
  color: white;
}

.my-item:visited {
  background-color: #00B9AE;
  color: white;
}

.my-item:hover {
  /* background-color: #B5EBE7;
  color: black;
  border-radius: 15px; */
  font-weight: 500;
}

.dash-button {
  margin-left: 10px;
  height: 35px;
  width: 100px;
  text-decoration: none;
  background-color: #B5EBE7;
  color: black;
  display:flex;
  flex-direction:column;
  justify-content: center;
  align-items:center;
  border: 1px solid black;
  border-radius: 10px;
  font-weight: 600;
}

.dash-button:hover {
  font-weight: bold;
}

.button {
  margin-left: 10px;
  height: 35px;
  width: 135px;
  text-decoration: none;
  background-color: #B5EBE7;
  color: black;
  display:flex;
  flex-direction:column;
  justify-content: center;
  align-items:center;
  border: 1px solid black;
  border-radius: 10px;
  font-weight: 600;
}

.button:hover {
  font-weight: bold;
}

.btns {
  display: flex;
}
</style>