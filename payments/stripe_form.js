{ % block content % }

let stripe = Stripe('pk_test_ZNASggyuMPivZNtUeAVSRigy00Ksb2rkKa');

// Create an instance of Elements.
const elements = stripe.elements();

// Custom styling can be passed to options when creating an Element.
// (Note that this demo uses a wider set of styles than the guide below.)
let style = {
    base: {
        color: '#32325d',
        fontFamily: '"Helvetica Neue", Helvetica, sans-serif',
        fontSmoothing: 'antialiased',
        fontSize: '16px',
        '::placeholder': {
            color: '#aab7c4'
        }
    },
    invalid: {
        color: '#fa755a',
        iconColor: '#fa755a'
    }
};

// Create an instance of the card Element.
const card = elements.create('card', {
    style: style
});

// Add an instance of the card Element into the `card-element` <div>.
card.mount('#card-element');

// Handle real-time validation errors from the card Element.
card.addEventListener('change', function(event) {
    const displayError = document.getElementById('card-errors');
    if (event.error) {
        displayError.textContent = event.error.message;
    } else {
        displayError.textContent = '';
    }
});

// Handle form submission.
let form = document.getElementById('payment-form');
form.addEventListener('submit', function(event) {
    event.preventDefault();

    stripe.createToken(card).then(function(result) {
        if (result.error) {
            // Inform the user if there was an error.
            let errorElement = document.getElementById('card-errors');
            errorElement.textContent = result.error.message;
        } else {
            // Send the token to your server.
            stripeTokenHandler(result.token);
        }
    });
});

// Submit the form with the token ID.
function stripeTokenHandler(token) {
    // Insert the token ID into the form so it gets submitted to the server
    let form = document.getElementById('payment-form');
    let hiddenInput = document.createElement('input');
    hiddenInput.setAttribute('type', 'hidden');
    hiddenInput.setAttribute('name', 'stripeToken');
    hiddenInput.setAttribute('value', token.id);
    form.appendChild(hiddenInput);

    // Submit the form
    form.submit();
}

let successElement = document.getElementById('stripe-token-handler');
document.querySelector('.wrapper').addEventListener('click', function() {
    successElement.className = 'is-hidden';
});

// Not in demo.
function stripeTokenHandler(token) {
    successElement.className = '';
    successElement.querySelector('.token').textContent = token.id;
}

<
iframe frameborder = "0"
allowtransparency = "true"
scrolling = "no"
name = "__privateStripeController1"
allowpaymentrequest = "true"
src = "https://js.stripe.com/v3/controller-d6f1c7c962bfe2c2ff1170441192e46b.html#apiKey =pk_test_ZNASggyuMPivZNtUeAVSRigy00Ksb2rkKa&amp;stripeJsId=f9380f60-20fd-4835-8a35-065bf976f63b&amp;origin=https%3A%2F%2Fstripe.com&amp;referrer=https%3A%2F%2Fstripe.com%2Fdocs%2Fstripe-js&amp;controllerId=__privateStripeController1"
aria - hidden = "true"
tabindex = "-1"
style = "border: none!important; margin: 0 px!important; padding: 0 px!important; width: 1 px!important; min - width: 100 % !important; overflow: hidden!important; display: block!important; visibility: hidden!important; position: fixed!important; height: 1 px!important; pointer - events: none!important; user - select: none!important" > < /iframe> <
iframe frameborder = "0"
allowtransparency = "true"
scrolling = "no"
name = "__privateStripeMetricsController0"
allowpaymentrequest = "true"
src = "https://js.stripe.com/v2/m/outer.html#url=https%3A%2F%2Fstripe.com%2Fdocs%2Fstripe-js&amp;title=&amp;referrer=&amp;muid=1953841f-0d2a-44f7-b5d6-4992b7cb7b44&amp;sid=40bd7c7e-18b0-4662-9529-b66aad751abb&amp;preview=true"
aria - hidden = "true"
tabindex = "-1"
style = "border: none !important; margin: 0px !important; padding: 0px !important; width: 1px !important; min-width: 100% !important; overflow: hidden !important; display: block !important; visibility: hidden !important; position: fixed !important; height: 1px !important; pointer-events: none !important; user-select: none !important;" > < /iframe> { % endblock % }