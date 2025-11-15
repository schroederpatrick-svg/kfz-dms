<template>
  <div class="invoices">
    <h1>Rechnungsverwaltung</h1>

    <table>
      <thead>
        <tr>
          <th>Auftrag</th>
          <th>Kunde</th>
          <th>Gesamtbetrag</th>
          <th>Aktion</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="invoice in invoices" :key="invoice.id">
          <td>{{ invoice.order_id }}</td>
          <td>{{ invoice.customer.name }}</td>
          <td>{{ invoice.total.toFixed(2) }} €</td>
          <td>
            <button @click="downloadInvoice(invoice.id)">Download PDF</button>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'Invoices',
  data() {
    return {
      invoices: []
    }
  },
  async mounted() {
    this.invoices = (await axios.get('/api/invoices')).data
  },
  methods: {
    async downloadInvoice(id) {
      const response = await axios.get(`/api/invoices/${id}/pdf`, { responseType: 'blob' })
      const url = window.URL.createObjectURL(new Blob([response.data]))
      const link = document.createElement('a')
      link.href = url
      link.setAttribute('download', `invoice_${id}.pdf`)
      document.body.appendChild(link)
      link.click()
    }
  }
}
</script>

<style scoped>
.invoices {
  padding: 20px;
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
button {
  padding: 4px 10px;
}
</style>
