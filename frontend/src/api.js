const API = "http://localhost:5000";

export async function fetchProducts() {
  return (await fetch(`${API}/products`)).json();
}

export async function fetchProduct(id) {
  return (await fetch(`${API}/products/${id}`)).json();
}

export async function addToCart(id) {
  return fetch(`${API}/cart`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ id })
  });
}