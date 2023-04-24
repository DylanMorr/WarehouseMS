<template>
	<div class="product-page">
		<Sidebar />

		<div class="dash-product-page">
			<div class="alert alert-warning alert-dismissible fade" role="alert" id="alertMessage" style="text-align: center;">
				<strong>New Product Successfully Added</strong>
			</div>

			<h1 class="prod-title">Add Products into the Warehouse</h1>

			<form class="form-deco">
				<div class="form-group row">
					<label for="inputName" class="col-md-4 mb-2 col-form-label">Name</label>
					<div class="col-md-8">
						<input type="text" class="form-control" v-model="Stock_Name">
					</div>
				</div>

				<div class="form-group row">
					<label for="inputSupplier" class="col-md-4 mb-2 col-form-label">Supplier</label>
					<div class="col-sm-8">
						<input type="text" class="form-control" v-model="Supplier">
					</div>
				</div>

				<div class="form-group row">
					<label for="inputProdID" class="col-md-4 mb-2 col-form-label">Product ID</label>
					<div class="col-sm-8">
						<input type="number" class="form-control" v-model="Product_Id">
					</div>
				</div>

				<div class="form-group row">
					<label for="inputPrice" class="col-md-4 mb-2 col-form-label">Price</label>
					<div class="col-sm-8">
						<input type="number" class="form-control" v-model="Price">
					</div>
				</div>

				<div class="form-group row">
					<label for="inputQuantity" class="col-md-4 mb-2 col-form-label">Quantity</label>
					<div class="col-sm-8">
						<input type="number" class="form-control" v-model="Quantity">
					</div>
				</div>

				<div class="form-group row">
					<label for="inputLocation" class="col-md-4 mb-2 col-form-label">Location</label>
					<div class="col-md-8">
						<div class="row">
							<div class="col-md-2">
								<label for="inputSector" class="col-form-label">Sector:</label>
							</div>
							<div class="col-md-4">
								<select class="custom-select" v-model="Location_Sector">
									<option selected></option>
									<option value="A">A</option>
									<option value="B">B</option>
									<option value="C">C</option>
									<option value="D">D</option>
									<option value="E">E</option>
								</select>
							</div>

							<div class="col-md-2">
								<label for="inputShelf" class="col-form-label">Shelf:</label>
							</div>
							<div class="col-md-4">
								<select class="form-select" v-model="Location_Shelf">
									<option>1</option>
									<option>2</option>
									<option>3</option>
									<option>4</option>
									<option>5</option>
								</select>
							</div>
						</div>
					</div>
				</div>

				<div class="form-group row">
					<label for="inputImage" class="col-md-4 mb-2 col-form-label">Image Upload</label>
					<div class="col-sm-8">
						<input class="m-2" type="file" @change="imageUpload">
					</div>
				</div>

				<div class="form-group row">
					<div class="col-md-4"></div> <!-- Add an empty column to push the button to the center -->
					<div class="col-md-4 text-center"> <!-- Use text-center class to center the button -->
						<button type="button" data-toggle="modal" data-target="#exampleModalCenter" class="save-btn">
							Save Product
						</button>
					</div>
					<div class="col-md-4"></div> <!-- Add another empty column to push the button to the center -->
				</div>
			</form>
		</div>

		<!-- Modal -->
		<div class="modal" id="exampleModalCenter" tabindex="-1" role="dialog" aria-labelledby="exampleModalCenterTitle"
			aria-hidden="true" data-backdrop="static">
			<div class="modal-dialog modal-dialog-centered" role="document">
				<div class="modal-content">
					<div class="modal-header">
						<h5 class="modal-title">Confirm Details Below</h5>
						<button type="button" class="close clbut" data-dismiss="modal" aria-label="Close">
							<span aria-hidden="true">&times;</span>
						</button>
					</div>
					<div class="modal-body">
						<p class="para"><strong>Product Information:</strong></p>
						<div class="row p-info-row">
							<div class="col-md-4">Name</div>
							<div class="col-md-3">-</div>
							<div class="col-md-5">{{Stock_Name}}</div>
						</div>

						<div class="row p-info-row">
							<div class="col-md-4">Supplier</div>
							<div class="col-md-3">-</div>
							<div class="col-md-5">{{Supplier}}</div>
						</div>

						<div class="row p-info-row">
							<div class="col-md-4">Product ID</div>
							<div class="col-md-3">-</div>
							<div class="col-md-5">{{Product_Id}}</div>
						</div>

						<div class="row p-info-row">
							<div class="col-md-4">Price</div>
							<div class="col-md-3">-</div>
							<div class="col-md-5">{{ Price }}</div>
						</div>

						<div class="row p-info-row">
							<div class="col-md-4">Quantity</div>
							<div class="col-md-3">-</div>
							<div class="col-md-5">{{ Quantity }}</div>
						</div>

						<div class="row p-info-row">
							<div class="col-md-4">Location</div>
							<div class="col-md-3">-</div>
							<div class="col-md-5">{{ Location_Sector }}-{{ Location_Shelf }}</div>
						</div>

						<div class="row p-info-row">
							<div class="col-md-4">Image</div>
							<div class="col-md-3">-</div>
							<div class="col-md-5">{{ PhotoImgName }}</div>
						</div>
					</div>
					<div class="modal-footer">
						<button type="button" class="btn btns" data-dismiss="modal">Cancel</button>
						<button type="button" v-if="Sid == 0" class="btn btn-primary" @click="createStock()" data-dismiss="modal">Create</button>
					</div>
				</div>
			</div>
		</div>
	</div>
</template>

<script>
import Sidebar from '@/components/Sidebar'
import axios from 'axios';
const PHOTO_URL = "http://127.0.0.1:8000/Assets/"

export default {
	name: 'DashHome',
	components: {
		Sidebar
	},
  data() {
    return {
      stock: [],
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
					this.saveProduct();
          this.refreshData();
          console.log(response.data);
        });
    },
		imageUpload(event) {
      let formData = new FormData();
      formData.append('file', event.target.files[0]);

      axios.post('/stock/savefile', formData)
        .then((response) => {
          this.PhotoImgName = response.data;
        });
    },
		saveProduct() {
			console.log("Product Saved")
			document.getElementById('alertMessage').classList.add('show');
			this.startTimeout();
		},
		startTimeout() {
			setTimeout(() => {
				document.getElementById('alertMessage').classList.remove('show');
			}, 5000);
		}
	}
}
</script>

<style lang="scss">
.prod-title {
	text-align: center;
	padding-bottom: 70px;
}

.alert {
	height: auto;
	width: 100%;
}

.form-deco {
	background-color: #B5EBE7;
	padding: 20px;
	border-radius: 10px;
}

.para {
	margin: 0px;
}

.save-btn {
	background-color: #00B9AE;
	color: white;
	width: 160px;
	padding: 7px;
	border: 1px solid black;
	border-radius: 20px;
}

.save-btn:hover {
	font-weight: 500;
}

label {
	font-weight: 500;
}

.product-page {
	display: flex;
}

.dash-product-page {
	margin: auto;
	padding: 2rem;
	max-width: 800px;
	width: 100%;
}

@media (max-width: 1024px) {
	.dash-product-page {
		padding-left: 6rem;
	}
}
</style>