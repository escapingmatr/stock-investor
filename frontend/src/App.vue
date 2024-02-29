<template>
  <div id="app">
    <StockSearch />
  </div>
</template>

<script>
import StockSearch from './components/StockSearch.vue';

export default {
  name: 'App',
  components: {
    StockSearch,
  },
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
