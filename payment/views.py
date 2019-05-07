from django.shortcuts import render
from booking.models import Booking
from .models import Payment
from django.core.mail import send_mail
from django.contrib import messages
from .forms import PaymentForm


def make_payment(request):
    booking_id = request.session['booking_id']
    booking = Booking.objects.get(pk=booking_id)
    form = PaymentForm()
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            payment = form.save(False)
            payment.booking_id = booking.id
            payment.save()

            message = '''Hi {}, \n
            This is to confirm that we have received your payment of {}$ 
            and that you are all set for the {} from {} to {}.\n
            Thank you,\n The iTour.com team'''.format(payment.first_name, 
            booking.price, booking.tour.name, booking.start_date, booking.end_date)
            send_mail('Your booking is confirmed', message,
                 'support@itour.com', [payment.email], fail_silently=False)
            return render(request, 'payment_confirmation.html', {
                    'email': payment.email
                })

    return render(request, 'payment.html', {
            'booking': booking,
            'form': form
        })


