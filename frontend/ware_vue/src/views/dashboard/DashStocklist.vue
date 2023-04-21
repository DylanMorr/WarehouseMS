<template>
  <div class="stocklist-page">
    <Sidebar />

    <div class="container dash-stocklist-page">
      <h1 style="text-align: center; padding: 50px;">Warehouse Stocklist</h1>
      <div class="table-con">
        <p style="text-align: left; padding-left: 20px; padding-top: 20px; font-weight: bold;">Manage Stock</p>
        <div class="table-container">
          <table ref="myTable" class="table table-bordered my-table">
            <thead style="background-color: #00B9AE; color: white;">
              <tr>
                <th id="table-head-border">Name</th>
                <th id="table-head-border">Supplier</th>
                <th id="table-head-border">Product ID</th>
                <th id="table-head-border">Price</th>
                <th id="table-head-border">Quantity</th>
                <th id="table-head-border">Location</th>
                <th id="table-head-border">Image</th>
                <th id="table-head-border">Actions</th>
              </tr>
            </thead>
            <tbody></tbody>
          </table>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import Sidebar from '@/components/Sidebar'
import testdata from "./testdata"
import $ from 'jquery'

export default {
  name: 'DashHome',
  components: {
    Sidebar
  },
  mounted() {
    this.getItems();
  },
  methods: {
    getItems() {
      // Get reference to the table element
      const table = this.$refs.myTable;

      $(table).DataTable({
        "stateSave": true,
        "stateDuration": -1, // session storage state saving
        dom: '<"d-flex justify-content-between"lBf>rt<"d-flex justify-content-between"ip>',
        buttons: [
            'csv',
            'print'
        ],
        data: testdata,
        columns: [
          { data: 'name' },
          { data: 'supplier' },
          { data: 'prod_id' },
          { data: 'price' },
          { data: 'quantity' },
          { data: 'location' },
          { data: 'image' },
          { data: 'actions' }
        ]
      });
    }
  }
};
</script>

<style lang="scss">
.stocklist-page {
  display: flex;
}

.dash-stocklist-page {
  margin: auto;
  text-align: center;
}

.table-con {
  background-color: #B5EBE7;
  border-radius: 20px;
  padding-left: 40px;
  padding-right: 40px;
}

.table-container {
  overflow-x: auto;
  padding: 20px;
  max-width: 100%;
}

.dataTables_wrapper .dt-buttons .btn {
  background-color: #00B9AE; 
  font-weight: bold;
  border-color: black; 
  color: white;
}

.dataTables_wrapper .dt-buttons .btn:hover {
  background-color: #B5EBE7; 
  color: black; 
}

.dataTables_paginate .pagination .page-item .page-link {
  border-color: black; 
  background-color: #00B9AE;
  color: white; 
}

/* Customize page number color */
.dataTables_paginate .pagination .page-item:not(.disabled) .page-link {
  background-color: #00B9AE;
  border-color: black; 
  color: white; 
}

/* Customize page number color on hover */
.dataTables_paginate .pagination .page-item:not(.disabled) .page-link:hover {
  background-color: #B5EBE7;
  color: black; 
}

/* Customize active page border color */
.dataTables_paginate .pagination .page-item.active .page-link {
  border-color: black; /* Change to desired color */
}

.dataTables_wrapper .dataTables_filter input {
  border-color: #000000; 
  color: #000000; 
}

.dataTables_wrapper .dataTables_filter input:focus {
  background-color: #F9F9F9; 
  color: #000000; 
}

.my-table {
  border-collapse: collapse;
  width: 100%;
  background-color: white;

  td {
    border: 1px solid black;
    padding: 8px;
  }
}

#table-head-border {
  border-color: black;
}
</style>
