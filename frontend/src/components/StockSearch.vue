<template>
  <div>
    <input v-model="stockCode" placeholder="Enter Stock Code" />
    <button @click="fetchPrediction">Search</button>
    <div v-if="prediction">Prediction: {{ prediction }}</div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      stockCode: '',
      prediction: null,
    };
  },
  methods: {
    async fetchPrediction() {
      if (!this.stockCode) return;
      try {
        const response = await axios.post('http://localhost:8001/predict/', {
          stock_code: this.stockCode,
        });
        this.prediction = response.data.prediction;
      } catch (error) {
        console.error('Error fetching prediction:', error);
        this.prediction = null;
      }
    },
  },
};
</script>
