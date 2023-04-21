<template>
  <div class="orders-page">
    <Sidebar />

    <div class="dash-orders-page">
      <h1 style="text-align: center; padding: 40px;">Add Orders for Processing</h1>

      <div class="button-con">
        <button class="order-button" data-toggle="modal" data-target="#orderModal">Add Order</button>
      </div>

      <div class="table-con">
        <p style="text-align: left; padding-left: 20px; padding-top: 20px; font-weight: bold;">Manage Orders</p>
        <div class="table-container">
          <table ref="orderTable" class="table table-bordered my-table">
            <thead style="background-color: #00B9AE; color: white;">
              <tr>
                <th id="table-head-border">Order ID</th>
                <th id="table-head-border">Product IDs</th>
                <th id="table-head-border">Quantities</th>
                <th id="table-head-border">Price</th>
                <th id="table-head-border">Buyer Name</th>
                <th id="table-head-border">Buyer Address</th>
                <th id="table-head-border">Actions</th>
              </tr>
            </thead>
            <tbody></tbody>
          </table>
        </div>
      </div>

      <!-- Modal -->
      <div class="modal" id="orderModal" tabindex="-1" role="dialog" aria-labelledby="orderModalCenterTitle"
        aria-hidden="true" data-backdrop="static">
        <div class="modal-dialog modal-dialog-centered modal-lg" role="document">
          <div class="modal-content">
            <div class="modal-header">
              <h5 class="modal-title">Confirm Details Below</h5>
              <button type="button" class="close clbut" data-dismiss="modal" aria-label="Close">
                <span aria-hidden="true">&times;</span>
              </button>
            </div>
            <div class="modal-body">
              <div class="form-group dynamic-element" style="display:none">
                <label class="dyna-marg" for="prod_id">Product ID:</label>
                <input class="dyna-marg" type="number" id="prod_id" name="Product ID" min="1" max="999999">
                <label class="dyna-marg" for="quantity">Quantity:</label>
                <input class="dyna-marg" type="number" id="qty" name="Quantity" min="1" max="999999">
                <label class="dyna-marg" for="price">Price:</label>
                <input class="dyna-marg" type="number" id="price" name="price" min="0" max="999999" step="0.01">
                <span class="delete col-md-1">x</span>
              </div>

              <div class="form-container">
                <form class="form-horizontal">
                  <fieldset>
                    <div class="main-form-dyna">
                      <label class="dyna-marg" for="quantity">Order ID:</label>
                      <input class="dyna-marg" type="number" id="order_id" name="OrderID" min="0" max="999999">

                      <label class="dyna-marg" for="b_name">Buyer Name:</label>
                      <input class="dyna-marg" type="text" id="b_name" name="BuyerName" placeholder="Buyer Name">

                      <label class="dyna-marg" for="b_address">Buyer Address:</label>
                      <input class="dyna-marg" type="text" id="b_address" name="BuyerAddress" placeholder="Buyer Address">
                    </div>
                    <div class="dynamic-stuff">
                      <label>Items:</label>
                      <!-- Dynamic element will be cloned here -->
                      <!-- You can call clone function once if you want it to show it a first element-->
                    </div>

                    <!-- Button -->
                    <div class="form-group">
                      <div class="row">
                        <div class="col-md-12">
                          <p class="add-one">+ Add Item</p>
                        </div>
                        <div class="col-md-5"></div>
                      </div>
                    </div>
                  </fieldset>
                </form>
              </div>
            </div>
            <div class="modal-footer">
              <button type="button" class="btn btns" data-dismiss="modal">Cancel</button>
              <button type="button" class="btn btns" @click="saveOrder()" data-dismiss="modal">Confirm</button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import Sidebar from '@/components/Sidebar'
import testdata from "./testorders"
import $ from 'jquery'

export default {
  name: 'DashHome',
  components: {
    Sidebar
  },
  mounted() {
    this.getItems();
    this.modalSetup();
  },
  methods: {
    saveOrder(){
      console.log('Saved Order');
    },
    getItems() {
      // Get reference to the table element
      const order_table = this.$refs.orderTable;

      $(order_table).DataTable({
        "stateSave": true,
        "stateDuration": -1, // session storage state saving
        dom: '<"d-flex justify-content-between"lBf>rt<"d-flex justify-content-between"ip>',
        buttons: [
          'csv',
          'print'
        ],
        data: testdata,
        columns: [
          { data: 'order_id' },
          { data: 'prod_id' },
          { data: 'qty' },
          { data: 'price' },
          { data: 'b_name' },
          { data: 'b_address' },
          { data: 'actions' }
        ]
      });
    },
    modalSetup() {
      //Clone the hidden element and shows it
      $('.add-one').click(function () {
        $('.dynamic-element').first().clone().appendTo('.dynamic-stuff').show();
        attach_delete();
      });


      //Attach functionality to delete buttons
      function attach_delete() {
        $('.delete').off();
        $('.delete').click(function () {
          console.log("click");
          $(this).closest('.form-group').remove();
        });
      }
    }
  }
}
</script>

<style lang="scss">
.order-button {
  background-color: #00B9AE;
  color: white;
  font-size: larger;
  font-weight: bold;
  border: 1px solid black;
  border-radius: 10px;
  width: 170px;
  height: 40px;
}

.button-con {
  display: flex;
  padding-bottom: 20px;
}

.add-one {
  color: green;
  text-align: center;
  font-weight: bolder;
  cursor: pointer;
}

.delete {
  color: red;
  text-align: center;
  font-weight: bold;
  font-size: large;
  padding-bottom: 4px;
  border-radius: 5px;
  cursor: pointer;
  display: inline-block;
}

.dynamic-element {
  margin-bottom: 0px;
}

.dyna-row {
  display: flex;
}

.dyna-marg {
  margin-right: 10px;
  width: 100px;
}

.main-form-dyna {
  display: flex;
  flex-direction: column;
  justify-content: center;
}

.orders-page {
  display: flex;
}

.dash-orders-page {
  margin: auto;
  text-align: center;
}
</style>