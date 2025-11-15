import React from "react";
import { BrowserRouter as Router, Routes, Route, Link } from "react-router-dom";
import Customers from "./components/Customers";
import Articles from "./components/Articles";
import Orders from "./components/Orders";
import Invoices from "./components/Invoices";

function App() {
  return (
    <Router>
      <div>
        <nav>
          <ul>
            <li><Link to="/customers">Kunden</Link></li>
            <li><Link to="/articles">Artikel</Link></li>
            <li><Link to="/orders">Aufträge</Link></li>
            <li><Link to="/invoices">Rechnungen</Link></li>
          </ul>
        </nav>

        <Routes>
          <Route path="/customers" element={<Customers />} />
          <Route path="/articles" element={<Articles />} />
          <Route path="/orders" element={<Orders />} />
          <Route path="/invoices" element={<Invoices />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
