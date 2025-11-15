import React, { useState, useEffect } from "react";
import { getInvoices } from "../api";

function Invoices() {
  const [invoices, setInvoices] = useState([]);

  useEffect(() => {
    fetchInvoices();
  }, []);

  const fetchInvoices = async () => setInvoices((await getInvoices()).data);

  return (
    <div>
      <h2>Rechnungen</h2>
      <ul>
        {invoices.map(inv => (
          <li key={inv.id}>
            Rechnung #{inv.id} – Kunde: {inv.customer.name} – Gesamt: {inv.total.toFixed(2)} €
            <a href={`http://127.0.0.1:8000/api/invoices/${inv.id}/pdf`} target="_blank" rel="noreferrer">PDF herunterladen</a>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default Invoices;
