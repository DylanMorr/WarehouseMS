<template>
  <div>
    <h1>This is the Stock page</h1>

   

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
            <button type="button" class="btn btn-light mr-1">
              <span class="material-icons">add</span>
            </button>
          </td>
        </tr>
      </tbody>
    </table>


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