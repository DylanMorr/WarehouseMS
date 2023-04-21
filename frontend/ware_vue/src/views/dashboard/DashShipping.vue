<template>
  <div class="shipping-page">
    <Sidebar />

    <div class="dash-shipping-page">
      <h1>Order Shipments</h1>
      <nav>
        <div class="nav nav-tabs" id="nav-tab" role="tablist">
          <a class="nav-item nav-link active" id="nav-home-tab" data-toggle="tab" href="#nav-home" role="tab"
            aria-controls="nav-home" aria-selected="true">To Be Shipped</a>
          <a class="nav-item nav-link" id="nav-profile-tab" data-toggle="tab" href="#nav-profile" role="tab"
            aria-controls="nav-profile" aria-selected="false">Shipped Orders</a>
        </div>
      </nav>
      <div class="tab-content" id="nav-tabContent">
        <div class="tab-pane fade show active" id="nav-home" role="tabpanel" aria-labelledby="nav-home-tab">
          To Be Shipped
        </div>
        <div class="tab-pane fade" id="nav-profile" role="tabpanel" aria-labelledby="nav-profile-tab">
          Shipped
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
.shipping-page {
  display: flex;
}

.dash-shipping-page {
  margin: auto;
  text-align: center;
}
</style>