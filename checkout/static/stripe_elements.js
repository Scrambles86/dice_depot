var stripePublicKey = $(#id_stripe_public_key).text().slice(1, -1);
var clientSecret = $(#id_client_secret).text().slice(1, -1);
var stripe = Stripe(stripePublicKey);
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

// Handle realtime validation errors on the card element
card.addEventListener('change', function (event) {
    var errorDiv = document.getElementById('card-errors');
    if (event.error) {
        var html = `
            <span class="icon" role="alert">
                <i class="fas fa-times"></i>
            </span>
            <span>${event.error.message}</span>
        `;
        $(errorDiv).html(html);
    } else {
        errorDiv.textContent = '';
    }
});

// Stripe Form Submit
var form = document.getElementById('payment-form');

form.addEventListener('submit', function(ev) {
ev.preventDefault();
    card.update({ 'disabled': true});
    $('#submit-button').attr('disabled', true);
    stripe.confirmCardPayment(clientSecret, {
        payment_method: {
            card: card,
        }
    }).then(function(result) {
        if (result.error) {
            var html = `
            <span class="icon" role="alert">
                <i class="fas fa-times"></i>
            </span>
            <span>${event.error.message}</span>
        `;
        $(errorDiv).html(html);
        } else {
            if (result.paymentIntent.status === 'succeeded') {
                form.submit();
            }
        }
    });