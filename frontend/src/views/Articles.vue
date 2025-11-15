<template>
  <div class="articles">
    <h1>Artikelverwaltung</h1>

    <form @submit.prevent="addArticle">
      <input v-model="newArticle.name" placeholder="Name" required />
      <input v-model.number="newArticle.price_net" placeholder="Preis netto" type="number" step="0.01" />
      <input v-model.number="newArticle.vat_rate" placeholder="MwSt %" type="number" step="0.01" />
      <input v-model.number="newArticle.stock" placeholder="Lagerbestand" type="number" />
      <button type="submit">Hinzufügen</button>
    </form>

    <table>
      <thead>
        <tr>
          <th>Name</th>
          <th>Preis netto</th>
          <th>MwSt %</th>
          <th>Lager</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="article in articles" :key="article.id">
          <td>{{ article.name }}</td>
          <td>{{ article.price_net.toFixed(2) }} €</td>
          <td>{{ article.vat_rate }} %</td>
          <td>{{ article.stock }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'Articles',
  data() {
    return {
      articles: [],
      newArticle: {
        name: '',
        price_net: 0,
        vat_rate: 19,
        stock: 0
      }
    }
  },
  async mounted() {
    this.fetchArticles()
  },
  methods: {
    async fetchArticles() {
      this.articles = (await axios.get('/api/articles')).data
    },
    async addArticle() {
      await axios.post('/api/articles', this.newArticle)
      this.newArticle = { name: '', price_net: 0, vat_rate: 19, stock: 0 }
      this.fetchArticles()
    }
  }
}
</script>

<style scoped>
.articles {
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
