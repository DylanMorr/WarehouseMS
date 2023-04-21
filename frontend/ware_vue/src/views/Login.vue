<template>
  <div id="login>">
    <h3 class="d-flex justify-content-center">
      Vue Front End
    </h3>
    <h5 class="d-flex justify-content-center">
      Employee Management Portal
    </h5>

    <nav class="navbar navbar-expand-sm bg-light navbar-dark">
      <ul class="navbar-nav">
        <li class="nav-item m-1">
          <button class="btn btn-light btn-outline-primary" @click="showDepartment()">Department</button>
        </li>
        <li class="nav-item m-1">
          <button class="btn btn-light btn-outline-primary" @click="showEmployee()">Employee</button>
        </li>
        <li class="nav-item m-1">
          <button class="btn btn-light btn-outline-primary" @click="showStock()">Stock</button>
        </li>
        <li class="nav-item m-1">
          <button class="btn btn-light btn-outline-primary" @click="showOrders()">Orders</button>
        </li>
      </ul>
    </nav>

    <div id="display">
      <component :is="selectedComponent"></component>
    </div>
  </div>
</template>

<script>
import test_department from '@/components/test_department.vue'
import test_employee from '@/components/test_employee.vue'
import test_stock from '@/components/test_stock.vue'
import test_orders from '@/components/test_orders.vue'

export default {
  components: {
    test_department,
    test_employee,
    test_stock,
    test_orders
  },
  data() {
    return {
      selectedComponent: "test_employee" // default component to display
    }
  },
  methods: {
    showDepartment() {
      this.selectedComponent = "test_department";
    },
    showEmployee() {
      this.selectedComponent = "test_employee";
    },
    showOrders() {
      this.selectedComponent = "test_orders";
    },
    showStock() {
      this.selectedComponent = "test_stock";
    }
  }
};
</script>

<style>
.login-view {
  margin: 40px;
  padding: 30px;
}

.jum-edit {
  text-align: center;
  background-color: whitesmoke;
  border: 1px solid black;
}
</style>