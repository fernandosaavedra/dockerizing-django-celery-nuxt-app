<template>
  <div class="container-fluid">
    <div class="grid">
      <ChartLine />
    </div>
    <br/><br/><br/>
  </div>
</template>

<script>
import ChartLine from "@/components/chart-line";


export default {
  components: {
    ChartLine
  }
};
</script>

<style lang="scss" scoped>
  body{
    position:relative;
    height:100vh;
  }
.grid {
  display: grid;
  row-gap: 2rem;
  width:70%;
  margin: 20px auto;
}
</style>