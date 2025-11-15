import axios from "axios";

const API_URL = process.env.REACT_APP_API_URL;

export const getCustomers = () => axios.get(`${API_URL}/customers`);
export const createCustomer = (data) => axios.post(`${API_URL}/customers`, data);

export const getArticles = () => axios.get(`${API_URL}/articles`);
export const createArticle = (data) => axios.post(`${API_URL}/articles`, data);

export const getOrders = () => axios.get(`${API_URL}/orders`);
export const createOrder = (data) => axios.post(`${API_URL}/orders`, data);

export const getInvoices = () => axios.get(`${API_URL}/invoices`);
