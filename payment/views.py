from django.shortcuts import render
from booking.models import Booking
from .models import Payment
from django.core.mail import send_mail


def make_payment(request, booking_id):
    booking = Booking.objects.get(pk=booking_id)
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        method = request.POST['paymentMethod']
        card_name = request.POST['card_name']
        card_number = request.POST['card_number']
        card_date = request.POST['card_date']
        card_cvv = request.POST['card_cvv']
        payment = Payment(booking=booking, first_name=first_name, last_name=last_name,
                          email=email, method=method, card_name=card_name,
                          card_number=card_number, card_date=card_date,
                          card_cvv=card_cvv)
        payment.save()
        
        message = '''Hi {}, \n
        This is to confirm that we have received your payment of {}$ 
        and that you are all set for the {} from {} to {}.\n
        Thank you,\n The iTour.com team'''.format(first_name, 
        booking.price, booking.tour.name, booking.start_date, booking.end_date)
        send_mail('Your booking is confirmed', message,
             'support@itour.com', [email], fail_silently=False)
        return render(request, 'payment_confirmation.html', {
                'email': email
            })

    return render(request, 'payment.html', {
            'booking': booking
        })


