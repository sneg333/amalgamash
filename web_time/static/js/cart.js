var csrfToken = $('input[name=csrfmiddlewaretoken]').val();

function updateCartTotals() {
  $.ajax({
    url: '/get_cart_totals/',
    method: 'GET',
    success: function(response) {
      $('.cart-total').text(response.cart_total);
      $('.cart-item-total').each(function() {
        var cartItemId = $(this).data('cart-item-id');
        var cartItemTotal = response.cart_item_totals[cartItemId];
        $(this).text(cartItemTotal);
      });
    },
    error: function(xhr, ajaxOptions, thrownError) {
      console.log(thrownError);
    }
  });
}

// Функция для удаления товара из корзины
function removeFromCart(cartItemId) {
  $.ajax({
    url: '/remove_from_cart/',
    method: 'POST',
    data: {
      'csrfmiddlewaretoken': csrfToken,
      'cart_item_id': cartItemId
    },
    success: function (data) {
      $('.cart-total').html(data.cart_total);
      $('.cart-items').html(data.cart_items);
      $('.cart-item-quantity[data-cart-item-id="' + cartItemId + '"]').closest('tr').remove();
    },
    error: function (error) {
      console.log(error);
    }
  });
}

// Обработчик событий для изменения количества товара в корзине
$('.cart-item-quantity').on('change', function() {
  var cartItemId = $(this).data('cart-item-id');
  var quantity = $(this).val();
  changeCartItemQuantity(cartItemId, quantity);
});

// Функция для изменения количества товара в корзине
function changeCartItemQuantity(cartItemId, quantity) {
  $.ajax({
    url: '/cart/update_quantity/',
    method: 'POST',
    data: {
      'cart_item_id': cartItemId,
      'quantity': quantity,
      'csrfmiddlewaretoken': csrfToken
    },
    success: function(response) {
      $('.cart-item-total[data-cart-item-id="' + cartItemId + '"]').text(response.cart_item_total);
      $('.cart-total').text(response.cart_total);
    },
    error: function(xhr, ajaxOptions, thrownError) {
      console.log(thrownError);
    }
  });
}

// Обработчик событий для удаления товара из корзины
$('.remove-from-cart').click(function(event) {
  event.preventDefault();
  var cartItemId = $(this).data('cart-item-id');
  removeFromCart(cartItemId);
});

  