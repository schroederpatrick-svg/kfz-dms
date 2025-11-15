<template>
  <div class="orders">
    <h1>Auftragsverwaltung</h1>

    <form @submit.prevent="addOrder">
      <select v-model="newOrder.customer_id" required>
        <option value="" disabled>Kunde wählen</option>
        <option v-for="c in customers" :key="c.id" :value="c.id">{{ c.name }}</option>
      </select>

      <input v-model="newOrder.vehicle_id" placeholder="Fahrzeug" required />

      <textarea v-model="newOrder.description" placeholder="Beschreibung"></textarea>

      <div class="order-items">
        <h3>Artikel hinzufügen</h3>
        <div v-for="(item, index) in newOrder.items" :key="index">
          <select v-model="item.article_id">
            <option value="" disabled>Artikel wählen</option>
            <option v-for="a in articles" :key="a.id" :value="a.id">{{ a.name }}</option>
          </select>
          <input v-model.number="item.quantity" type="number" min="1" placeholder="Menge" />
          <button @click.prevent="removeItem(index)">Löschen</button>
        </div>
        <button @click.prevent="addItem">Artikel hinzufügen</button>
      </div>

      <button type="submit">Auftrag erstellen</button>
    </form>

    <table>
      <thead>
        <tr>
          <th>Kunde</th>
          <th>Fahrzeug</th>
          <th>Beschreibung</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="order in orders" :key="order.id">
          <td>{{ order.customer.name }}</td>
          <td>{{ order.vehicle_id }}</td>
          <td>{{ order.description }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'Orders',
  data() {
    return {
      orders: [],
      customers: [],
      articles: [],
      newOrder: {
        customer_id: '',
        vehicle_id: '',
        description: '',
        items: []
      }
    }
  },
  async mounted() {
    await this.fetchOrders()
    this.customers = (await axios.get('/api/customers')).data
    this.articles = (await axios.get('/api/articles')).data
  },
  methods: {
    async fetchOrders() {
      this.orders = (await axios.get('/api/orders')).data
    },
    addItem() {
      this.newOrder.items.push({ article_id: '', quantity: 1 })
    },
    removeItem(index) {
      this.newOrder.items.splice(index, 1)
    },
    async addOrder() {
      await axios.post('/api/orders', this.newOrder)
      this.newOrder = { customer_id: '', vehicle_id: '', description: '', items: [] }
      this.fetchOrders()
    }
  }
}
</script>

<style scoped>
.orders {
  padding: 20px;
}
form {
  margin-bottom: 20px;
}
textarea {
  display: block;
  width: 100%;
  margin: 10px 0;
}
table {
  width: 100%;
  border-collapse: collapse;
}
th, td {
  border: 1px solid #ccc;
  padding: 8px;
  text-align: left;
}
.order-items {
  margin-top: 10px;
  margin-bottom: 10px;
}
.order-items div {
  margin-bottom: 5px;
}
</style>
