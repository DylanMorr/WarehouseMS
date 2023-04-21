<template>
  <Nav />

  <Sign_In_Up />
</template>

<script>
import Sign_In_Up from '@/components/Sign_In_Up.vue'
import Nav from '@/components/Nav'

export default {
  components: {
    Sign_In_Up,
    Nav
  }
};
</script>

<style lang="scss" scoped>
</style>