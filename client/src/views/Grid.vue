<template lang="html">
<div class="row">
  <div class="column"></div>
  <div class="column"></div>
  <div class="column"></div>
  <div class="column"></div>
</div>
</template>

<script>

export default {
    name: 'post',}

</script> 

<style scoped lang="css">
.column {
  float: left;
  width: 25%;
}

.row:after {
  content: "";
  display: table;
  clear: both;
}

</style>
