<template>
  <div>
    <input
      v-model="stockCode"
      @input="validateStockCode"
      placeholder="Enter stock code"
    />
    <button :disabled="!isValidStockCode" @click="trainModel">Search</button>
    <div v-if="trainingResponse">
      <p>Model training result: {{ trainingResponse }}</p>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      stockCode: '',
      isValidStockCode: false,
      trainingResponse: null,
    };
  },
  methods: {
    validateStockCode() {
      // Simple validation rule for demonstration. Adjust as needed.
      this.isValidStockCode = this.stockCode.length > 0; // Basic validation
    },
    async trainModel() {
      try {
        const response = await fetch(
          `http://your-backend-endpoint/api/train/${this.stockCode}`,
          {
            method: 'POST', // or "GET", depending on your backend setup
            // Include headers, body, etc., as required by your backend
          }
        );
        const data = await response.json();
        this.trainingResponse = data.message; // Adjust based on the actual response structure
      } catch (error) {
        console.error('Error training model:', error);
        this.trainingResponse = 'Failed to train model.';
      }
    },
  },
};
</script>
