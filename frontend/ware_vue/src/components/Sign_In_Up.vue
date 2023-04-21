<template>
  <div class="container log-con" id="container-test">
    <div class="form-container sign-up-container">
      <form class="log-form" v-on:submit.prevent="submitFormRegister">
        <h1 class="log-title">Create Account</h1>

        <input class="log-input" type="email" v-model="username" placeholder="Email" />

        <input class="log-input" type="password" v-model="password" placeholder="Password" />

        <input class="log-input" type="password" v-model="repeat_pass" placeholder="Repeat Password" />

        <div class="text-danger" v-if="errors.length">
          <p v-for="error in errors" v-bind:key="error">
            {{ error }}
          </p>
        </div>

        <button id="log-btns" style="margin-top: 30px;">Sign Up</button>
      </form>
    </div>

    <div class="form-container sign-in-container">
      <form class="log-form" v-on:submit.prevent="submitFormLogin">
        <h1 class="log-title">Sign in</h1>

        <input class="log-input" type="email" v-model="username" placeholder="Email" />

        <input class="log-input" type="password" v-model="password" placeholder="Password" />

        <div class="text-danger" v-if="errors.length">
          <p v-for="error in errors" v-bind:key="error">
            {{ error }}
          </p>
        </div>

        <a class="for-pass" href="#">Forgot your password?</a>

        <button id="log-btns" style="margin-top: 10px;">Sign In</button>
      </form>
    </div>

    <div class="overlay-container">
      <div class="overlay">
        <div class="overlay-panel overlay-left">
          <h1 class="log-title">Welcome Back!</h1>
          <p class="over-msg">To get back to managing login and get started</p>
          <button id="log-btns" class="ghost" @click="showSignInPanel">Sign In</button>
        </div>
        <div class="overlay-panel overlay-right">
          <h1 class="log-title">Hi, there!</h1>
          <p class="over-msg">Enter your details and start managing today</p>
          <button id="log-btns" class="ghost" @click="showSignUpPanel">Sign Up</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  data() {
    return {
      username: '',
      password: '',
      repeat_pass: '',
      errors: []
    }
  },
  methods: {
    showSignUpPanel() {
      const container = document.querySelector('#container-test');
      container.classList.add("right-panel-active");
    },
    showSignInPanel() {
      const container = document.querySelector('#container-test');
      container.classList.remove("right-panel-active");
    },
    submitFormLogin() {
      console.log('Submit Form')

      // reset authorization 
      axios.defaults.headers.common['Authorization'] = ""

      // remove token from localStorage
      localStorage.removeItem('token')

      this.errors = []

      if (this.username === '') {
        this.errors.push('The username is missing!')
      }

      if (this.password === '') {
        this.errors.push('The password is missing!')
      }

      if (!this.errors.length) {
        const formData = {
          username: this.username,
          password: this.password
        }

        axios
          .post('/api/token/login/', formData)
          .then(response => {
            // get token from server
            const token = response.data.auth_token

            // set the token in the store
            this.$store.commit('setToken', token)

            // set default for axios 
            axios.defaults.headers.common['Authorization'] = "Token " + token

            // store in localstorage so refresh works
            localStorage.setItem('token', token)

            // redirect
            this.$router.push('/dashboard/dash-home-page')
          })
          .catch(error => {
            if (error.response) {
              for (const property in error.response.data) {
                this.errors.push(`${property}: ${error.response.data[property]}`)
              }

              console.log(JSON.stringify(error.response.data))
            } else if (error.message) {
              this.errors.push('Something went wrong, please try again')

              console.log(JSON.stringify(error))
            }
          })
      }
    },
    submitFormRegister() {
      console.log('Submit Form')

      this.errors = []

      if (this.username === '') {
        this.errors.push('The username is missing!')
      }

      if (this.password === '') {
        this.errors.push('The password is missing!')
      }

      if (this.password !== this.repeat_pass) {
        this.errors.push('The passwords do not match!')
      }

      if (!this.errors.length) {
        const formData = {
          username: this.username,
          password: this.password
        }

        axios
          .post('/api/users/', formData)
          .then(response => {
            this.$router.push('/log-in')
          })
          .catch(error => {
            if (error.response) {
              for (const property in error.response.data) {
                this.errors.push(`${property}: ${error.response.data[property]}`)
              }

              console.log(JSON.stringify(error.response.data))
            } else if (error.message) {
              this.errors.push('Something went wrong, please try again')

              console.log(JSON.stringify(error))
            }
          })
      }
    }
  },
};
</script>

<style lang="scss" scoped>
.log-title {
  font-weight: bold;
  margin-bottom: 30px;
}

.over-msg {
  font-weight: 500;
  line-height: 20px;
  letter-spacing: 0.5px;
  margin: 20px 0 30px;
}

.for-pass {
  color: black;
  text-decoration: underline;
  margin: 15px 0;
}

#log-btns {
  border-radius: 20px;
  border: 1px solid #00B9AE;
  background-color: #00B9AE;
  color: #FFFFFF;
  font-size: 12px;
  font-weight: bold;
  padding: 12px 45px;
  letter-spacing: 1px;
  text-transform: uppercase;
  transition: transform 80ms ease-in;
}

#log-btns:active {
  transform: scale(0.95);
}

#log-btns:focus {
  outline: none;
}

#log-btns.ghost {
  background-color: transparent;
  border-color: #FFFFFF;
}

.log-form {
  background-color: #FFFFFF;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-direction: column;
  padding: 0 50px;
  height: 100%;
  text-align: center;
}

.log-input {
  background-color: #eee;
  border: none;
  padding: 12px 15px;
  margin: 8px 0;
  width: 70%;
}

.log-con {
  background-color: #fff;
  border: 3px solid #00B9AE;
  border-radius: 10px;
  position: relative;
  overflow: hidden;
  width: 70%;
  height: 90vh;
  max-width: none;
  min-height: 90vh;
  margin-top: 20px;
}

.form-container {
  position: absolute;
  top: 0;
  height: 100%;
  transition: all 0.6s ease-in-out;
}

.sign-in-container {
  left: 0;
  width: 50%;
  z-index: 2;
}

.log-con.right-panel-active .sign-in-container {
  transform: translateX(100%);
}

.sign-up-container {
  left: 0;
  width: 50%;
  opacity: 0;
  z-index: 1;
}

.log-con.right-panel-active .sign-up-container {
  transform: translateX(100%);
  opacity: 1;
  z-index: 5;
  animation: show 0.6s;
}

@keyframes show {

  0%,
  49.99% {
    opacity: 0;
    z-index: 1;
  }

  50%,
  100% {
    opacity: 1;
    z-index: 5;
  }
}

.overlay-container {
  position: absolute;
  top: 0;
  left: 50%;
  width: 50%;
  height: 100%;
  overflow: hidden;
  transition: transform 0.6s ease-in-out;
  z-index: 100;
}

.log-con.right-panel-active .overlay-container {
  transform: translateX(-100%);
}

.overlay {
  background: -webkit-linear-gradient(to right, #00B9AE, #00B9AE);
  background: linear-gradient(to right, #00B9AE, #00B9AE);
  background-repeat: no-repeat;
  background-size: cover;
  background-position: 0 0;
  color: #FFFFFF;
  position: relative;
  left: -100%;
  height: 100%;
  width: 200%;
  transform: translateX(0);
  transition: transform 0.6s ease-in-out;
}

.log-con.right-panel-active .overlay {
  transform: translateX(50%);
}

.overlay-panel {
  position: absolute;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-direction: column;
  padding: 0 40px;
  text-align: center;
  top: 0;
  height: 100%;
  width: 50%;
  transform: translateX(0);
  transition: transform 0.6s ease-in-out;
}

.overlay-left {
  transform: translateX(-20%);
}

.log-con.right-panel-active .overlay-left {
  transform: translateX(0);
}

.overlay-right {
  right: 0;
  transform: translateX(0);
}

.log-con.right-panel-active .overlay-right {
  transform: translateX(20%);
}
</style>