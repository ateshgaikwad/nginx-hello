async function fetchMessage() {
  const res = await fetch('http://localhost:5000/message');
  const data = await res.json();
  document.getElementById('message').textContent = data.message;
}
