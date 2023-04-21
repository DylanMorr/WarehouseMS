import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import LoginSignUp from '../views/LoginSignUp.vue'
import store from '../store'
import DashHome from '../views/dashboard/DashHome.vue'
import DashOrders from '../views/dashboard/DashOrders.vue'
import DashProduct from '../views/dashboard/DashProduct.vue'
import DashReports from '../views/dashboard/DashReports.vue'
import DashShipping from '../views/dashboard/DashShipping.vue'
import DashStocklist from '../views/dashboard/DashStocklist.vue'
import DashWarehouse from '../views/dashboard/DashWarehouse.vue'

import Login from '../views/Login.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/:catchAll(.*)',
    redirect: '/'
  },
  {
    path: '/login-sign-up',
    name: 'LoginSignUp',
    component: LoginSignUp,
    meta: {
      requireNotLogged: true
    }
  },
  {
    path: '/dashboard/dash-home-page',
    name: 'DashHome',
    component: DashHome,
    meta: {
      requireLogin: true
    }
  },
  {
    path: '/dashboard/dash-orders-page',
    name: 'DashOrders',
    component: DashOrders,
    meta: {
      requireLogin: true
    }
  },
  {
    path: '/dashboard/dash-product-page',
    name: 'DashProduct',
    component: DashProduct,
    meta: {
      requireLogin: true
    }
  },
  {
    path: '/dashboard/dash-reports-page',
    name: 'DashReports',
    component: DashReports,
    meta: {
      requireLogin: true
    }
  },
  {
    path: '/dashboard/dash-shipping-page',
    name: 'DashShipping',
    component: DashShipping,
    meta: {
      requireLogin: true
    }
  },
  {
    path: '/dashboard/dash-stocklist-page',
    name: 'DashStocklist',
    component: DashStocklist,
    meta: {
      requireLogin: true
    }
  },
  {
    path: '/dashboard/dash-warehouse-page',
    name: 'DashWarehouse',
    component: DashWarehouse,
    meta: {
      requireLogin: true
    }
  },

  {
    path: '/login',
    name: 'Login',
    component: Login
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

router.beforeEach((to, from, next) => {
  if (to.matched.some(record => record.meta.requireLogin) && !store.state.user.isAuthenticated) {
    next('/')
  } else if (to.matched.some(record => record.meta.requireNotLogged) && store.state.user.isAuthenticated) {
    next('/') 
  } else {
    next()
  }
})


export default router
