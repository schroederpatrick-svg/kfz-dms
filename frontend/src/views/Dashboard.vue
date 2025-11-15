<template>
  <div class="dashboard">
    <h1>KFZ Werkstatt DMS</h1>
    <p>Willkommen im Dashboard. Hier bekommst du einen schnellen Überblick.</p>

    <div class="stats">
      <div>
        <h2>Kunden</h2>
        <p>{{ customers.length }}</p>
      </div>
      <div>
        <h2>Aufträge</h2>
        <p>{{ orders.length }}</p>
      </div>
      <div>
        <h2>Artikel</h2>
        <p>{{ articles.length }}</p>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'Dashboard',
  data() {
    return {
      customers: [],
      orders: [],
      articles: []
    }
  },
  async mounted() {
    this.customers = (await axios.get('/api/customers')).data
    this.orders = (await axios.get('/api/orders')).data
    this.articles = (await axios.get('/api/articles')).data
  }
}
</script>

<style scoped>
.dashboard {
  padding: 20px;
}
.stats {
  display: flex;
  gap: 20px;
  margin-top: 20px;
}
.stats div {
  border: 1px solid #ccc;
  padding: 10px;
  flex: 1;
  text-align: center;
}
</style>
