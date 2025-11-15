import React, { useState, useEffect } from "react";
import { getOrders, createOrder, getCustomers, getArticles } from "../api";

function Orders() {
  const [orders, setOrders] = useState([]);
  const [customers, setCustomers] = useState([]);
  const [articles, setArticles] = useState([]);
  const [selectedCustomer, setSelectedCustomer] = useState("");
  const [description, setDescription] = useState("");
  const [items, setItems] = useState([{ article_id: "", quantity: 1 }]);

  useEffect(() => {
    fetchOrders();
    fetchCustomers();
    fetchArticles();
  }, []);

  const fetchOrders = async () => setOrders((await getOrders()).data);
  const fetchCustomers = async () => setCustomers((await getCustomers()).data);
  const fetchArticles = async () => setArticles((await getArticles()).data);

  const handleItemChange = (index, field, value) => {
    const newItems = [...items];
    newItems[index][field] = value;
    setItems(newItems);
  };

  const addItem = () => setItems([...items, { article_id: "", quantity: 1 }]);

  const handleSubmit = async (e) => {
    e.preventDefault();
    await createOrder({
      customer_id: parseInt(selectedCustomer),
      vehicle_id: 1, // Dummy Fahrzeug, später mit Auswahl
      description,
      items: items.map(i => ({ article_id: parseInt(i.article_id), quantity: parseInt(i.quantity) }))
    });
    setDescription("");
    setItems([{ article_id: "", quantity: 1 }]);
    fetchOrders();
  };

  return (
    <div>
      <h2>Aufträge</h2>
      <form onSubmit={handleSubmit}>
        <select value={selectedCustomer} onChange={e => setSelectedCustomer(e.target.value)} required>
          <option value="">Kunde wählen</option>
          {customers.map(c => <option key={c.id} value={c.id}>{c.name}</option>)}
        </select>
        <input value={description} onChange={e => setDescription(e.target.value)} placeholder="Beschreibung" />

        <h4>Artikel</h4>
        {items.map((item, idx) => (
          <div key={idx}>
            <select value={item.article_id} onChange={e => handleItemChange(idx, "article_id", e.target.value)} required>
              <option value="">Artikel wählen</option>
              {articles.map(a => <option key={a.id} value={a.id}>{a.name}</option>)}
            </select>
            <input type="number" value={item.quantity} min="1" onChange={e => handleItemChange(idx, "quantity", e.target.value)} required />
          </div>
        ))}
        <button type="button" onClick={addItem}>Artikel hinzufügen</button>
        <button type="submit">Auftrag erstellen</button>
      </form>

      <ul>
        {orders.map(o => (
          <li key={o.id}>Auftrag #{o.id} – Kunde: {o.customer.name} – {o.description}</li>
        ))}
      </ul>
    </div>
  );
}

export default Orders;

