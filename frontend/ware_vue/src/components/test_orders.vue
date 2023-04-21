<template>
  <div>
    <h1>This is the Order page</h1>

    <button type="button" class="btn btn-primary m-2 float-end" data-bs-toggle="modal" data-bs-target="#editModal"
      @click="addOrder()">Add Order</button>

    <table class="table table-striped">
      <thead>
        <tr>
          <th>
            Order ID
          </th>
          <th>
            Product IDs
          </th>
          <th>
            Quantities
          </th>
          <th>
            Price
          </th>
          <th>
            Buyer Name
          </th>
          <th>
            Buyer Address
          </th>
          <th>
            Actions
          </th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="ord in orders">
          <td>{{ ord.Order_Id }}</td>
          <td>
            <span v-for="(pid, index) in ord.Product_Ids">{{ pid }}{{ index < ord.Product_Ids.length - 1 ? ', ' : ''
            }}</span>
          </td>
          <td>
            <span v-for="(qty, index) in ord.Product_Qtys">{{ qty }}{{ index < ord.Product_Qtys.length - 1 ? ', ' : ''
            }}</span>
          </td>
          <td>{{ ord.Price }}</td>
          <td>{{ ord.Buyer_Name }}</td>
          <td>{{ ord.Buyer_Address }}</td>
          <td>
            <button type="button" class="btn btn-light mr-1" data-bs-toggle="modal" data-bs-target="#editModal"
              @click="editOrder(ord)">
              <span class="material-icons">edit</span>
            </button>
            <button type="button" class="btn btn-light mr-1" @click="deleteOrder(ord.Oid)">
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
                <div>
                  <span class="input-group-text">Order ID</span>
                  <input type="number" class="form-control" v-model="Order_Id">
                </div>

                <div>
                  <span class="input-group-text">Buyer Name</span>
                  <input class="form-control" type="text" v-model="Buyer_Name">
                </div>

                <div>
                  <span class="input-group-text">Buyer Address</span>
                  <input class="form-control" type="text" v-model="Buyer_Address">
                </div>

                <div>
                    <span class="input-group-text">Product ID:</span>
                    <input class="form-control" type="text" v-model="prod_ids" placeholder="Enter numbers spaced with ',' i.e. 1, 2, 3">
                  </div>

                  <div>
                    <span class="input-group-text">Quantity</span>
                    <input class="form-control" type="text" v-model="prod_qtys" placeholder="Enter numbers spaced with ',' i.e. 1, 2, 3">
                  </div>

                  <div>
                    <span class="input-group-text">Price</span>
                    <input class="form-control" type="number" step="0.01" v-model="Price">
                  </div>
              </div>
            </div>

            <button type="button" v-if="Oid == 0" class="btn btn-primary" @click="createOrder()">Create</button>
            <button type="button" v-if="Oid != 0" class="btn btn-primary" @click="updateOrder()">Update</button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      orders: [],
      modalTitle: "",
      Oid: 0,
      Order_Id: 0,
      prod_ids: "",
      prod_qtys: "",
      Price: 0.00,
      Buyer_Name: "",
      Buyer_Address: ""
    }
  },
  methods: {
    refreshData() {
      axios.get('/order')
        .then((response) => {
          this.orders = response.data;
        });
    },
    addOrder() {
      this.modalTitle = "Add Order";
      this.Oid = 0;
      this.Order_Id = 0;
      this.prod_ids = "";
      this.prod_qtys = "";
      this.Price = 0.00;
      this.Buyer_Name = "";
      this.Buyer_Address = "";
    },
    editOrder(ord) {
      this.modalTitle = "Edit Order";
      this.Oid = ord.Oid;
      this.Order_Id = ord.Order_Id;
      this.prod_ids = ord.Product_Ids.join(", ");
      this.prod_qtys = ord.Product_Qtys.join(", ");
      this.Price = ord.Price;
      this.Buyer_Name = ord.Buyer_Name;
      this.Buyer_Address = ord.Buyer_Address;
    },
    createOrder() {
      axios.post('/order', { 
        Order_Id: this.Order_Id, 
        Product_Ids: this.prod_ids.split(',').map(x => x.trim()), 
        Product_Qtys: this.prod_qtys.split(',').map(x => x.trim()), 
        Price: this.Price, 
        Buyer_Name: this.Buyer_Name, 
        Buyer_Address: this.Buyer_Address 
      })
        .then((response) => {
          this.refreshData();
          alert(response.data);
        });
    },
    updateOrder() {
      axios.put('/order', { 
        Oid: this.Oid, 
        Order_Id: this.Order_Id, 
        Product_Ids: this.prod_ids.split(',').map(x => x.trim()), 
        Product_Qtys: this.prod_qtys.split(',').map(x => x.trim()), 
        Price: this.Price, 
        Buyer_Name: this.Buyer_Name, 
        Buyer_Address: this.Buyer_Address 
      })
        .then((response) => {
          this.refreshData();
          alert(response.data);
        });
    },
    deleteOrder(ordID) {
      if (!confirm("Are you sure?")) {
        return;
      }
      axios.delete('/order/' + ordID)
        .then((response) => {
          this.refreshData();
          alert(response.data);
        });
    }
  },
  mounted: function () {
    this.refreshData();
  }
}
</script>