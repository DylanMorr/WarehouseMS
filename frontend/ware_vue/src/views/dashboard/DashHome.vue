<template>
	<div class="home-page">
		<Sidebar />

		<div class="dash-home-page">
			<h1 class="home-title">Welcome to the Dashboard</h1>

			<div class="custom-hr"></div>

			<div class="row">
				<div class="col-sm-6 mb-2">
					<div class="card" style="background-color: #00B9AE; color: white;">
						<div class="card-header" style="background-color: #B5EBE7; color: black;">Stock Warnings</div>
						<div class="card-body">
							<table class="table table-bordered table-condensed" style="background-color: #B5EBE7; border: 1px solid black;">
                <tbody>
                  <tr>
                    <td id="table-data">Item ID: item_id</td>
										<td id="table-data">Location: location</td>
										<td id="table-data">Stock: stock</td>
                  </tr>
                </tbody>
              </table>
						</div>
					</div>
				</div>
				<div class="col-sm-6">
					<div class="card" style="background-color: #00B9AE; color: white;">
						<div class="card-header" style="background-color: #B5EBE7; color: black;">Shipping Warning</div>
						<div class="card-body">
							<table class="table table-bordered table-condensed" style="background-color: #B5EBE7; border: 1px solid black;">
                <tbody>
                  <tr>
                    <td id="table-data">Order ID: order_id</td>
										<td id="table-data">Shipping By: due_date</td>
                  </tr>
                </tbody>
              </table>
						</div>
					</div>
				</div>
			</div>
		</div>
	</div>
</template>

<script>
import Sidebar from '@/components/Sidebar'

export default {
	name: 'DashHome',
	components: {
		Sidebar
	},
}
</script>

<style lang="scss">
:root {
	--primary: #5AD2CA;
	--grey: #64748b;
	--dark: #00B9AE;
	--dark-alt: #B5EBE7;
	--light: #f1f5f9;
	--sidebar-width: 300px;
}

#table-data {
	border: 1px solid black;
	text-align: center;
}

* {
	margin: 0;
	padding: 0;
	box-sizing: border-box;
}

body {
	background: var(--light);
}

.home-title {
	text-align: center;
	margin-top: 50px;
	margin-bottom: 50px;
}

.custom-hr {
	border-top: 2px solid black;
	margin-top: 50px;
	margin-bottom: 50px;
}

button {
	cursor: pointer;
	appearance: none;
	border: none;
	outline: none;
	background: none;
}

.home-page {
	display: flex;
}

.dash-home-page {
	margin: auto;
	padding: 2rem;
}

@media (max-width: 1024px) {
	.dash-home-page {
		padding-left: 6rem;
	}
}
</style>
