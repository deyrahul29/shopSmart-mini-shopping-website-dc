import { Link } from "react-router-dom";

export default function Navbar() {
  return (
    <div style={{
      background: "#333",
      padding: 10,
      color: "white",
      display: "flex",
      gap: 20
    }}>
      <Link to="/" style={{ color: "white" }}>Products</Link>
      <Link to="/cart" style={{ color: "white" }}>Cart</Link>
    </div>
  );
}
