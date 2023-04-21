<template>
  <div class="reports-page">
    <Sidebar/>

    <div class="dash-reports-page">
      <h1>Reports Page</h1>
      <p>This is reports page</p>
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

.reports-page {
	display: flex;
	main {
		flex: 1 1 0;
		padding: 2rem;
		@media (max-width: 1024px) {
			padding-left: 6rem;
		}
	}
}
</style>