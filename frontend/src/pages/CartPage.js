export default function ProductCard({ product, onAdd }) {
  return (
    <div style={{
      border: "1px solid #ccc",
      padding: 10,
      width: 200,
      textAlign: "center"
    }}>
      <img src={product.image} width="100%" alt="" />
      <h3>{product.name}</h3>
      <p>{product.price} USD</p>
      <button onClick={onAdd}>Add to Cart</button>
    </div>
  );
}