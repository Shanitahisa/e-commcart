document.addEventListener("DOMContentLoaded", function () {
  // Heart toggle
  document.querySelectorAll('.fav-btn').forEach(btn => {
    btn.addEventListener('click', function (e) {
      e.preventDefault();
      this.classList.toggle('active');
      this.innerHTML = this.classList.contains('active')
        ? '<i class="bi bi-heart-fill text-danger"></i>'
        : '<i class="bi bi-heart"></i>';
    });
  });

  // Cart toggle
  document.querySelectorAll('.cart-btn').forEach(btn => {
    btn.addEventListener('click', function () {
      this.classList.toggle('active');
      this.innerHTML = this.classList.contains('active')
        ? '<i class="bi bi-cart-check-fill"></i>'
        : '<i class="bi bi-cart-plus"></i>';
    });
  });

  // Quantity controls
  const cartItems = document.querySelectorAll(".list-group-item");
  cartItems.forEach(item => {
    const minusBtn = item.querySelector(".minus-btn");
    const plusBtn = item.querySelector(".plus-btn");
    const input = item.querySelector(".quantity-input");

    minusBtn?.addEventListener("click", () => {
      let value = parseInt(input.value);
      if (value > 1) {
        input.value = value - 1;
        updateTotal();
      }
    });

    plusBtn?.addEventListener("click", () => {
      let value = parseInt(input.value);
      input.value = value + 1;
      updateTotal();
    });
  });

  function updateTotal() {
    let total = 0;
    document.querySelectorAll(".list-group-item").forEach(item => {
      const priceText = item.querySelector("small")?.textContent
        .replace("UGX", "")
        .replace(/,/g, "")
        .trim();
      const quantity = parseInt(item.querySelector(".quantity-input")?.value || 0);
      const price = parseInt(priceText);
      if (!isNaN(price)) {
        total += price * quantity;
      }
    });
    document.getElementById("cart-total").textContent = "UGX " + total.toLocaleString();
  }
});

// checkout

document.addEventListener("DOMContentLoaded", function () {
  const clearCartBtn = document.getElementById("clearCart");
  const orderSummary = document.getElementById("orderSummary");

  clearCartBtn.addEventListener("click", function () {
    orderSummary.innerHTML = `
      <li class="list-group-item text-center text-muted">
        Your cart is empty.
      </li>
    `;
  });
});
