<template>
	<aside :class="`${is_expanded ? 'is-expanded' : ''}`">
		<div class="logo">
			<img :src="logoURL" alt="Vue" />
		</div>

		<div class="menu-toggle-wrap">
			<button class="menu-toggle" @click="ToggleMenu">
				<span class="material-icons">keyboard_double_arrow_right</span>
			</button>
		</div>

		<h3>WareAbouts Management Menu</h3>
		<div class="menu">
			<router-link to="/dashboard/dash-home-page" class="button">
				<span class="material-icons">home</span>
				<span class="text">Home</span>
			</router-link>
			<router-link to="/dashboard/dash-product-page" class="button">
				<span class="material-icons">assignment_add</span>
				<span class="text">Product</span>
			</router-link>
			<router-link to="/dashboard/dash-warehouse-page" class="button">
				<span class="material-icons">warehouse</span>
				<span class="text">Warehouse</span>
			</router-link>
			<router-link to="/dashboard/dash-stocklist-page" class="button">
				<span class="material-icons">assignment</span>
				<span class="text">Stock List</span>
			</router-link>
			<router-link to="/dashboard/dash-orders-page" class="button">
				<span class="material-icons">receipt_long</span>
				<span class="text">Orders</span>
			</router-link>
			<router-link to="/dashboard/dash-shipping-page" class="button">
				<span class="material-icons">local_shipping</span>
				<span class="text">Shipping</span>
			</router-link>
			<router-link to="/dashboard/dash-reports-page" class="button">
				<span class="material-icons">analytics</span>
				<span class="text">Reports</span>
			</router-link>
		</div>

		<div class="flex"></div>

		<div class="menu">
			<button @click="logout()" class="button is-danger">
				<span class="material-icons">logout</span>
				<span class="text">Logout</span>
			</button>
			<button class="button is-danger">
				<router-link to="/">
					<span class="material-icons">first_page</span>
					<span class="text">Landing Page</span>
				</router-link>
			</button>
		</div>
	</aside>
</template>

<script setup>
import axios from 'axios'
import { ref } from 'vue'
import logoURL from '../assets/logo.png'
const is_expanded = ref(localStorage.getItem("is_expanded") === "true")

const ToggleMenu = () => {
	is_expanded.value = !is_expanded.value
	localStorage.setItem("is_expanded", is_expanded.value)
}

function landingPageNav() {
	this.$router.push('/');
}

async function logout() {
	console.log('logout')

	await axios
		.post('/api/token/logout/')
		.then(response => {
			console.log("Logged out")
		})

	// reset authorization 
	axios.defaults.headers.common['Authorization'] = ""

	// remove token from localStorage
	localStorage.removeItem('token')

	// remove token from state
	this.$store.commit('removeToken')

	// redirect to main page
	this.$router.push('/')
}
</script>

<style lang="scss" scoped>
aside {
	display: flex;
	flex-direction: column;
	background-color: var(--dark);
	color: var(--light);
	width: calc(2rem + 32px);
	overflow: hidden;
	min-height: 100vh;
	padding: 1rem;
	transition: 0.2s ease-in-out;

	.flex {
		flex: 1 1 0%;
	}

	.logo {
		display: flex;
		justify-content: center;
		align-items: center;
		margin-bottom: 1rem;

		img {
			background-color: white;
			padding: 4px;
			border-radius: 5px;
			width: 3rem;
		}
	}

	.menu-toggle-wrap {
		display: flex;
		justify-content: flex-end;
		margin-bottom: 1rem;
		position: relative;
		top: 0;
		transition: 0.2s ease-in-out;

		.menu-toggle {
			transition: 0.2s ease-in-out;

			.material-icons {
				font-size: 2rem;
				color: var(--light);
				transition: 0.2s ease-out;
			}

			&:hover {
				.material-icons {
					color: var(--light);
					transform: translateX(0.5rem);
				}
			}
		}
	}

	h3,
	.button .text {
		opacity: 0;
		transition: opacity 0.2s ease-in-out;
	}

	h3 {
		color: black;
		font-size: 0.875rem;
		text-align: center;
		margin-bottom: 0.5rem;
		text-transform: uppercase;
	}

	.menu {
		margin: 0 -1rem;

		.button {
			display: flex;
			align-items: center;
			text-decoration: none;
			transition: 0.2s ease-in-out;
			padding: 0.5rem 1rem;

			.material-icons {
				font-size: 2rem;
				color: var(--light);
				transition: 0.2s ease-in-out;
			}

			.text {
				color: var(--light);
				transition: 0.2s ease-in-out;
			}

			&:hover {
				background-color: var(--dark-alt);

				.material-icons,
				.text {
					color: black;
				}
			}

			&.router-link-exact-active {
				background-color: var(--dark-alt);
				border-right: 5px solid var(--primary);

				.material-icons,
				.text {
					color: black;
				}
			}
		}
	}

	&.is-expanded {
		width: var(--sidebar-width);

		.menu-toggle-wrap {
			top: -3rem;

			.menu-toggle {
				transform: rotate(-180deg);
			}
		}

		h3,
		.button .text {
			opacity: 1;
		}

		.button {
			background-color: #5AD2CA;
			margin-bottom: 20px;

			.material-icons {
				margin-right: 1rem;
			}
		}
	}

	@media (max-width: 1024px) {
		position: absolute;
		z-index: 99;
	}
}</style>