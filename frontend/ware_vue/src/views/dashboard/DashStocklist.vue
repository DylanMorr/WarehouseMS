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
            <tbody>
            </tbody>
          </table>


          <div class="modal fade" id="editModal" tabindex="-1" aria-labelledby="editModalLabel" aria-hidden="true">
            <div class="modal-dialog modal-lg modal-dialog-centered">
              <div class="modal-content">
                <div class="modal-header">
                  <!-- Title of the modal -->
                  <h5 class="modal-title" id="editModalLabel">{{ modalTitle }}</h5>
                  <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>

                <div class="modal-body">
                  <div class="d-flex flex-row bd-highlight mb-3">
                    <div class="p-2 w-50 bd-highlight">

                      <div class="input-group mb-3">
                        <!-- edit name form field -->
                        <span class="input-group-text">Name</span>
                        <input type="text" class="form-control" v-model="Stock_Name">
                      </div>

                      <div class="input-group mb-3">
                        <!-- edit Supplier form field -->
                        <span class="input-group-text">Supplier</span>
                        <input type="text" class="form-control" v-model="Supplier">
                      </div>

                      <div class="input-group mb-3">
                        <!-- edit Product form field -->
                        <span class="input-group-text">Product ID</span>
                        <input type="number" class="form-control" v-model="Product_Id">
                      </div>

                      <div class="input-group mb-3">
                        <!-- edit Price form field -->
                        <span class="input-group-text">Price</span>
                        <input type="number" class="form-control" v-model="Price">
                      </div>

                      <div class="input-group mb-3">
                        <!-- edit Quantity form field -->
                        <span class="input-group-text">Quantity</span>
                        <input type="number" class="form-control" v-model="Quantity">
                      </div>

                      <div class="input-group mb-3">
                        <!-- edit lcoation Sector form field -->
                        <span class="input-group-text">Sector</span>
                        <select class="form-select" v-model="Location_Sector">
                          <option>A</option>
                          <option>B</option>
                          <option>C</option>
                          <option>D</option>
                          <option>E</option>
                        </select>
                      </div>

                      <div class="input-group mb-3">
                        <!-- edit lcoation Shelf form field -->
                        <span class="input-group-text">Shelf</span>
                        <select class="form-select" v-model="Location_Shelf">
                          <option>1</option>
                          <option>2</option>
                          <option>3</option>
                          <option>4</option>
                          <option>5</option>
                        </select>
                      </div>

                    </div>
                    <div class="p-2 w-50 bd-highlight">
                      <!-- image upload form field -->
                      <img :src="PhotoPath + PhotoImgName" />
                      <input class="m-2" type="file" @change="imageUpload">
                    </div>
                  </div>

                  <!-- update button  -->
                  <button type="button" v-if="Sid != 0" class="btn btn-primary" @click="updateStock()">Update</button>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import Sidebar from '@/components/Sidebar'
import axios from 'axios';
import $ from 'jquery'

const PHOTO_URL = "http://127.0.0.1:8000/Assets/"

export default {
  name: 'DashHome',
  components: {
    Sidebar
  },
  data() {
    return {
      stock: [],
      modalTitle: "",
      Sid: 0,
      Stock_Name: "",
      Supplier: "",
      Product_Id: 0,
      Price: 0.00,
      Quantity: 0,
      Location_Sector: "",
      Location_Shelf: 0,
      PhotoImgName: "vue.png",
      PhotoPath: PHOTO_URL,
    }
  },
  mounted() {
    this.refreshData();
  },
  methods: {
    getTable() {
      const table = this.$refs.myTable;

          $(table).DataTable({
            "stateSave": true,
            "stateDuration": -1, // session storage state saving
            dom: '<"d-flex justify-content-between"lBf>rt<"d-flex justify-content-between"ip>',
            buttons: [
              'csv',
              'print'
            ],
            data: this.stock,
            columns: [
              { data: 'Stock_Name' },
              { data: 'Supplier' },
              { data: 'Product_Id' },
              { data: 'Price' },
              { data: 'Quantity' },
              { data: 'Location_Sector', render: function (data, type, row) { return data + row.Location_Shelf; } },
              { data: 'PhotoImgName' },
              {render: function (data, type, row) {
                  return `
                    <button type="button" class="btn btn-light mr-1" data-bs-toggle="modal" data-bs-target="#editModal"
                      @click="editStock(${data+row.Sid})">
                      <span class="material-icons">edit</span>
                    </button>
                    <button type="button" class="btn btn-light mr-1" @click="deleteStock(${data+row.Sid})">
                      <span class="material-icons">delete</span>
                    </button>
                    <button type="button" class="btn btn-light mr-1">
                      <span class="material-icons">add</span>
                    </button>
                  `;
                }
              }
            ]

          });
    },
    refreshData() {
      axios.get('/stock')
        .then((response) => {
          this.stock = response.data;

          this.getTable();
        });
    },
    editStock(stk) {
      this.modalTitle = "Edit Product";
      this.Sid = stk.Sid;
      this.Stock_Name = stk.Stock_Name;
      this.Supplier = stk.Supplier;
      this.Product_Id = stk.Product_Id;
      this.Price = stk.Price;
      this.Quantity = stk.Quantity;
      this.Location_Sector = stk.Location_Sector;
      this.Location_Shelf = stk.Location_Shelf;
      this.PhotoImgName = stk.PhotoImgName;
    },
    updateStock() {
      axios.put('/stock', {
        Sid: this.Sid,
        Stock_Name: this.Stock_Name,
        Supplier: this.Supplier,
        Product_Id: this.Product_Id,
        Price: this.Price,
        Quantity: this.Quantity,
        Location_Sector: this.Location_Sector,
        Location_Shelf: this.Location_Shelf,
        PhotoImgName: this.PhotoImgName
      })
        .then((response) => {
          this.refreshData();
          alert(response.data);
        });
    },
    deleteStock(stkID) {
      if (!confirm("Are you sure?")) {
        return;
      }
      axios.delete('/stock/' + stkID)
        .then((response) => {
          this.refreshData();
          alert(response.data);
        });
    },
    imageUpload(event) {
      let formData = new FormData();
      formData.append('file', event.target.files[0]);

      axios.post('/stock/savefile', formData)
        .then((response) => {
          this.PhotoImgName = response.data;
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
  border-color: black;
  /* Change to desired color */
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
