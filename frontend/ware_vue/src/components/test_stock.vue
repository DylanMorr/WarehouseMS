<template>
  <div>
    <h1>This is the Stock page</h1>

    <button type="button" class="btn btn-primary m-2 float-end" data-bs-toggle="modal" data-bs-target="#editModal"
      @click="addStock()">Add Product</button>

    <table class="table table-striped">
      <thead>
        <tr>
          <th>
            Name
          </th>
          <th>
            Supplier
          </th>
          <th>
            Product ID
          </th>
          <th>
            Price
          </th>
          <th>
            Quantity
          </th>
          <th>
            Location
          </th>
          <th>
            Image
          </th>
          <th>
            Actions
          </th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="stk in stock">
          <td>{{ stk.Stock_Name }}</td>
          <td>{{ stk.Supplier }}</td>
          <td>{{ stk.Product_Id }}</td>
          <td>{{ stk.Price }}</td>
          <td>{{ stk.Quantity }}</td>
          <td>{{ stk.Location_Sector }}-{{ stk.Location_Shelf }}</td>
          <td>{{ stk.PhotoImgName }}</td>
          <td>
            <button type="button" class="btn btn-light mr-1" data-bs-toggle="modal" data-bs-target="#editModal"
              @click="editStock(stk)">
              <span class="material-icons">edit</span>
            </button>
            <button type="button" class="btn btn-light mr-1" @click="deleteStock(stk.Sid)">
              <span class="material-icons">delete</span>
            </button>
          </td>
        </tr>
      </tbody>
    </table>

    <div class="modal fade" id="editModal" tabindex="-1" aria-labelledby="editModalLabel" aria-hidden="true">
      <div class="modal-dialog modal-lg modal-dialog-centered">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title" id="editModalLabel">{{ modalTitle }}</h5>
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
          </div>

          <div class="modal-body">
            <div class="d-flex flex-row bd-highlight mb-3">
              <div class="p-2 w-50 bd-highlight">

                <div class="input-group mb-3">
                  <span class="input-group-text">Name</span>
                  <input type="text" class="form-control" v-model="Stock_Name">
                </div>

                <div class="input-group mb-3">
                  <span class="input-group-text">Supplier</span>
                  <input type="text" class="form-control" v-model="Supplier">
                </div>

                <div class="input-group mb-3">
                  <span class="input-group-text">Product ID</span>
                  <input type="number" class="form-control" v-model="Product_Id">
                </div>

                <div class="input-group mb-3">
                  <span class="input-group-text">Price</span>
                  <input type="number" class="form-control" v-model="Price">
                </div>

                <div class="input-group mb-3">
                  <span class="input-group-text">Quantity</span>
                  <input type="number" class="form-control" v-model="Quantity">
                </div>

                <div class="input-group mb-3">
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
                <img :src="PhotoPath + PhotoImgName" />
                <input class="m-2" type="file" @change="imageUpload">
              </div>
            </div>

            <button type="button" v-if="Sid == 0" class="btn btn-primary"
              @click="createStock()">Create</button>
            <button type="button" v-if="Sid != 0" class="btn btn-primary"
              @click="updateStock()">Update</button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

const PHOTO_URL = "http://127.0.0.1:8000/Assets/"

export default {
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
  methods: {
    refreshData() {
      axios.get('/stock')
        .then((response) => {
          this.stock = response.data;
        });
    },
    addStock() {
      this.modalTitle = "Add Product";
      this.Sid = 0;
      this.Stock_Name = "";
      this.Supplier = "";
      this.Product_Id = 0;
      this.Price = 0.00;
      this.Quantity = 0;
      this.Location_Sector = "";
      this.Location_Shelf = 0;
      this.PhotoImgName = "vue.png";
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
    createStock() {
      axios.post('/stock', { 
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
  },
  mounted: function () {
    this.refreshData();
  }
}
</script>