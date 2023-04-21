import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import axios from 'axios'

import 'bootstrap/dist/css/bootstrap.min.css';
import 'bootstrap/js/dist/modal'; 

import 'datatables.net-bs5'
import 'datatables.net-bs5/css/dataTables.bootstrap5.min.css'
import 'jszip'
import 'pdfmake'
import 'datatables.net-buttons-bs5'
import 'datatables.net-buttons-bs5/css/buttons.bootstrap5.min.css'
import 'datatables.net-buttons/js/buttons.colVis'
import 'datatables.net-buttons/js/buttons.flash'
import 'datatables.net-buttons/js/buttons.html5'
import 'datatables.net-buttons/js/buttons.print'

axios.defaults.baseURL = 'http://127.0.0.1:8000'

createApp(App)
  .use(store)
  .use(router, axios)
  .mount('#app')
