<template>
  <Nav />

  <div class="home">
    <div class="jumbotron">
      <div class="container">
        <h1 class="display-4" style="color: black">Welcome to WareAbouts</h1>

        <h2 class="lead" style="color: black">Hands on management of your warehouse</h2>
      </div>
    </div>

    <section class="section">
      <div class="container">
        <div class="row">
          <div class="card-deck">
            <div class="card">
              <img class="card-img-top" src="@/assets/logo.png" alt="Card image cap"
                style="width: 100%; height: 200px; object-fit: scale-down;">
              <div class="card-body">
                <h5 class="card-title">Manage at your own pace</h5>
                <p class="card-text">This is just placeholder text.</p>
              </div>
            </div>

            <div class="card">
              <img class="card-img-top" src="@/assets/logo.png" alt="Card image cap"
                style="width: 100%; height: 200px; object-fit: scale-down;">
              <div class="card-body">
                <h5 class="card-title">Manage with others</h5>
                <p class="card-text">This is just placeholder text.</p>
              </div>
            </div>

            <div class="card">
              <img class="card-img-top" src="@/assets/logo.png" alt="Card image cap"
                style="width: 100%; height: 200px; object-fit: scale-down;">
              <div class="card-body">
                <h5 class="card-title">Manage from home</h5>
                <p class="card-text">This is just placeholder text.</p>
              </div>
            </div>
          </div>

          <div class="col-md-12 text-center click-but">
            <a class="btn btns btn-lg mt-6 mb-6" @click.prevent="handleClick">Click to get started</a>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
import Nav from '@/components/Nav'

export default {
  name: 'HomeView',
  components: {
    Nav
  },
  methods: {
    handleClick() {
      if (this.$store.state.user.isAuthenticated) {
        alert('User already logged in')
      } else {
        window.location.href = '/login-sign-up'
      }
    }
  }
}
</script>

<style scoped>
.jumbotron {
  background-color: #B5EBE7;
}

.btns {
  background-color: #00B9AE;
  border: 1px solid black;
}

.btns:hover {
  background-color: #00B9AE;
  border: 1px solid black;
  font-weight: 500;
}

.click-but {
  margin-top: 50px;
  margin-bottom: 70px;
  color: white;
}
</style>
