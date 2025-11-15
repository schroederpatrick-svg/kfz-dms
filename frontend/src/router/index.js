import { createRouter, createWebHistory } from 'vue-router'
import Dashboard from '../views/Dashboard.vue'
import Customers from '../views/Customers.vue'
import Vehicles from '../views/Vehicles.vue'
import Articles from '../views/Articles.vue'
import Orders from '../views/Orders.vue'
import Invoices from '../views/Invoices.vue'

const routes = [
  { path: '/', name: 'Dashboard', component: Dashboard },
  { path: '/customers', name: 'Customers', component: Customers },
  { path: '/vehicles', name: 'Vehicles', component: Vehicles },
  { path: '/articles', name: 'Articles', component: Articles },
  { path: '/orders', name: 'Orders', component: Orders },
  { path: '/invoices', name: 'Invoices', component: Invoices }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
