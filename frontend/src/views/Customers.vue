<template>
  <div class="customers">
    <h1>Kundenverwaltung</h1>

    <form @submit.prevent="addCustomer">
      <input v-model="newCustomer.name" placeholder="Name" required />
      <input v-model="newCustomer.email" placeholder="Email" />
      <input v-model="newCustomer.phone" placeholder="Telefon" />
      <button type="submit">Hinzufügen</button>
    </form>

    <table>
      <thead>
        <tr>
          <th>Name</th>
          <th>Email</th>
          <th>Telefon</th>
          <th>Aktion</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="customer in customers" :key="customer.id">
          <td>{{ customer.name }}</td>
          <td>{{ customer.email }}</td>
          <td>{{ customer.phone }}</td>
          <td>
            <button @click="deleteCustomer(customer.id)">Löschen</button>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'Customers',
  data() {
    return {
      customers: [],
      newCustomer: {
        name: '',
        email: '',
        phone: ''
      }
    }
  },
  async mounted() {
    this.fetchCustomers()
  },
  methods: {
    async fetchCustomers() {
      this.customers = (await axios.get('/api/customers')).data
    },
    async addCustomer() {
      await axios.post('/api/customers', this.newCustomer)
      this.newCustomer = { name: '', email: '', phone: '' }
      this.fetchCustomers()
    },
    async deleteCustomer(id) {
      await axios.delete(`/api/customers/${id}`)
      this.fetchCustomers()
    }
  }
}
</script>

<style scoped>
.customers {
  padding: 20px;
}
form {
  margin-bottom: 20px;
}
input {
  margin-right: 10px;
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
</style>
