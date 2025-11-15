import { useEffect, useState } from "react";
import { fetchProducts, addToCart } from "../api";
import ProductCard from "../components/ProductCard";

export default function ProductsPage() {
  const [products, setProducts] = useState([]);

  useEffect(() => {
    fetchProducts().then(setProducts);
  }, []);

  return (
    <div style={{ display: "flex", gap: 20 }}>
      {products.map(p => (
        <ProductCard key={p.id} product={p} onAdd={() => addToCart(p.id)} />
      ))}
    </div>
  );
}