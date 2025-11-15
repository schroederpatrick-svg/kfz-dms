import React, { useState, useEffect } from "react";
import { getArticles, createArticle } from "../api";

function Articles() {
  const [articles, setArticles] = useState([]);
  const [name, setName] = useState("");
  const [price, setPrice] = useState("");
  const [vat, setVat] = useState("19");

  useEffect(() => {
    fetchArticles();
  }, []);

  const fetchArticles = async () => {
    const res = await getArticles();
    setArticles(res.data);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    await createArticle({ name, price_net: parseFloat(price), vat_rate: parseFloat(vat) });
    setName("");
    setPrice("");
    setVat("19");
    fetchArticles();
  };

  return (
    <div>
      <h2>Artikel</h2>
      <form onSubmit={handleSubmit}>
        <input value={name} onChange={(e) => setName(e.target.value)} placeholder="Name" required />
        <input value={price} onChange={(e) => setPrice(e.target.value)} placeholder="Preis netto" required />
        <input value={vat} onChange={(e) => setVat(e.target.value)} placeholder="MwSt %" required />
        <button type="submit">Hinzufügen</button>
      </form>

      <ul>
        {articles.map(a => (
          <li key={a.id}>{a.name} – {a.price_net}€ (+{a.vat_rate}%)</li>
        ))}
      </ul>
    </div>
  );
}

export default Articles;
