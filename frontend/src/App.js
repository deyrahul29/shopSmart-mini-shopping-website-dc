import React from "react";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import ProductsPage from "./pages/ProductsPage";
import CartPage from "./pages/CartPage";
import Navbar from "./components/Navbar";

function App() {
  return (
    <BrowserRouter>
      <Navbar />
      <Routes>
        <Route path="/" element={<ProductsPage />} />
        <Route path="/cart" element={<CartPage />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
