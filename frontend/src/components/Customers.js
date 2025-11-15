import React, { useState, useEffect } from "react";
import { getCustomers, createCustomer } from "../api";

function Customers() {
  const [customers, setCustomers] = useState([]);
  const [name, setName] = useState("");
  const [email, setEmail] = useState("");

  useEffect(() => {
    fetchCustomers();
  }, []);

  const fetchCustomers = async () => {
    const res = await getCustomers();
    setCustomers(res.data);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    await createCustomer({ name, email });
    setName("");
    setEmail("");
    fetchCustomers();
  };

  return (
    <div>
      <h2>Kunden</h2>
      <form onSubmit={handleSubmit}>
        <input value={name} onChange={(e) => setName(e.target.value)} placeholder="Name" required />
        <input value={email} onChange={(e) => setEmail(e.target.value)} placeholder="Email" required />
        <button type="submit">Hinzufügen</button>
      </form>

      <ul>
        {customers.map(c => (
          <li key={c.id}>{c.name} ({c.email})</li>
        ))}
      </ul>
    </div>
  );
}

export default Customers;
