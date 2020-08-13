var stripe_public_key = $(#id_stripe_public_key).text().slice(1, -1);
var client_secret = $(#id_client_secret).text().slice(1, -1);
var stripe = Stripe(stripe_public_key);
var elements = stripe.elements();
var card = elements.create('card');
card.mount('#card-element')

// Event listener for card errors

card.addEventListener('change', function(event) {
    var paymentError = document.getElementById('payment-failed');
    if (event.error) {
        var html =
            <span>${event.error.message}</span>

        $(paymentError).html(html);
    } else {
        paymentError.textContent = '';
    }
});