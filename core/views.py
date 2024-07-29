from django.http import BadHeaderError, HttpResponse
from django.shortcuts import redirect, render
from . models import *
from django.core.mail import send_mail
from django.contrib import messages
from django.http import JsonResponse
from django.urls import reverse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect
from .forms import *

# Create your views here.

def index(request):
    context = {}
    return render(request, 'index.html', context)


def about(request):
    context = {}
    return render(request, 'about-us.html', context)



def express(request):
    if request.method == 'POST':
        sender_data = {
            'name': request.POST.get('name'),
            'email': request.POST.get('email'),
            'weight': request.POST.get('weight'),
            'phonenumber': request.POST.get('phonenumber'),
            'address': request.POST.get('address'),
            'description': request.POST.get('description')
        }

        receiver_data = {
            'name': request.POST.get('rec_name'),
            'email': request.POST.get('rec_email'),
            'phonenumber': request.POST.get('rec_phonenumber'),
            'address': request.POST.get('rec_address')
        }

        # Debug: Print the form data
        print('Sender Data:', sender_data)
        print('Receiver Data:', receiver_data)

        # Basic validation
        if all(sender_data.values()) and all(receiver_data.values()):
            sender = ExpressSender.objects.create(**sender_data)
            receiver = ExpressReceiver.objects.create(**receiver_data)

            request.session['sender_id'] = sender.id
            request.session['receiver_id'] = receiver.id

            # messages.success(request, 'Data saved successfully.')
            return redirect('payment')
        else:
            messages.error(request, 'Please fill all fields.')

    return render(request, 'express.html')





def normal(request):
    if request.method == 'POST':
        nsender_form = NormalSenderForm(request.POST)
        nreceiver_form = NormalReceiverForm(request.POST)

        if nsender_form.is_valid() and nreceiver_form.is_valid():
            nsender = nsender_form.save()
            nreceiver = nreceiver_form.save()

            request.session['nsender_id'] = nsender.id
            request.session['nreceiver_id'] = nreceiver.id

            return redirect('payments')  
        else:
            messages.error(request, 'Please fill all fields.')
    else:
        nsender_form = NormalSenderForm()
        nreceiver_form = NormalReceiverForm()

    return render(request, 'normal.html', {'nsender_form': nsender_form, 'nreceiver_form': nreceiver_form})




def payment(request):
    wallet = Wallet.objects.first()
    bank = AccountDetail.objects.first()
    sender_id = request.session.get('sender_id')
    receiver_id = request.session.get('receiver_id')

    sender_data = ExpressSender.objects.get(id=sender_id) if sender_id else None
    receiver_data = ExpressReceiver.objects.get(id=receiver_id) if receiver_id else None

    if sender_data:
        weight = float(sender_data.weight)
        cost = weight * 3.50 + 10
        formatted_cost = f"{cost:.2f}"
    else:
        weight = 0
        cost = 0
        formatted_cost = f"{cost:.2f}"

    return render(request, 'payment.html', {
        'sender_data': sender_data,
        'receiver_data': receiver_data,
        'cost': formatted_cost,
        'wallet': wallet,
        'bank': bank,
        # 'formatted_cost':formatted_cost
    })



def payments(request):
    wallet = Wallet.objects.first()
    bank = AccountDetail.objects.first()
    sender_id = request.session.get('nsender_id')
    receiver_id = request.session.get('nreceiver_id')

    sender_data = Normalsender.objects.get(id=sender_id) if sender_id else None
    receiver_data = Normalreceiver.objects.get(id=receiver_id) if receiver_id else None

    if sender_data:
        weight = float(sender_data.weight)
        cost = weight * 3.50
        formatted_cost = f"{cost:.2f}"
    else:
        weight = 0
        cost = 0
        formatted_cost = f"{cost:.2f}"

    return render(request, 'payments.html', {
        'sender_data': sender_data,
        'receiver_data': receiver_data,
        'cost': formatted_cost,
        'wallet': wallet,
        'bank': bank,
    })




def oceanfreight(request):
    context = {}
    return render(request, 'ocean-freight-forwarding.html', context)

def airfreight(request):
    context = {}
    return render(request, 'air-freight-carrier.html', context)

def roadfreight(request):
    context = {}
    return render(request, 'road-freight-forwarding.html', context)

def movements(request):
    context = {}
    return render(request, 'soc-movements.html', context)

def importers(request):
    context = {}
    return render(request, 'importers-logistics-rep.html', context)

def exports(request):
    context = {}
    return render(request, 'export-import.html', context)

def logistics(request):
    context = {}
    return render(request, 'logistics.html', context)

def contact(request):
    if request.method == 'POST':
        # Process form submission
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        phonenumber = request.POST.get('phonenumber')
        message = request.POST.get('message')

        # Save the form data to the database
        contact_form_entry = ContactForm.objects.create(
            name=name,
            email=email,
            subject=subject,
            phonenumber=phonenumber,
            message=message,
        )

        # Prepare and send the notification email to the admin
        sender_name = ' Couriermail'
        sender_email = 'dcmediabusiness1@gmail.com'
        admin_email = 'decarkson@gmail.com'
        admin_subject = 'New Message Received'
        admin_message = (
            f'A new message has been received.\n\n'
            f'Name: {name}\n'
            f'Email: {email}\n'
            f'subject: {subject}\n'
            f'phonenumber: {phonenumber}\n'
            f'Message: {message}'
        )

        try:
            send_mail(
                admin_subject,
                admin_message,
                f'{sender_name} <{sender_email}>',
                [admin_email],
                fail_silently=False,
            )
            messages.success(request, 'Your message has been sent successfully!')
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        except Exception as e:
            messages.error(request, f'An error occurred: {e}')

        return redirect('index')
    
    context = {}
    return render(request, 'contact-us.html', context)


def household(request):
    context = {}
    return render(request, 'move-household-goods.html', context)

def commercial(request):
    context = {}
    return render(request, 'ship-commercial-goods.html', context)

def international(request):
    context = {}
    return render(request, 'international-freight.html', context)

def domestic(request):
    context = {}
    return render(request, 'domestic-freight.html', context)

def forwarder(request):
    context = {}
    return render(request, 'freight-forwarder.html', context)

def consultation(request):
    context = {}
    return render(request, 'freight-consultation.html', context)

def trackingDetails(request):
    context = {}
    return render(request, 'tracking-details.html', context)


@csrf_exempt
def track_number(request):
    if request.method == 'POST':
        tracking_number = request.POST.get('shipment_tracking_no', '')
        if tracking_number:
            if tracking_number == 'HZEY-JEZIS02-VKALE-ONDESW': 
                redirect_url = request.build_absolute_uri(reverse('trackingDetails'))
                return JsonResponse({'status': 'success', 'redirect_url': redirect_url})
            else:
                return JsonResponse({'status': 'error', 'message': 'Tracking number not found'})
        else:
            return JsonResponse({'status': 'error', 'message': 'Invalid tracking number'})
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'})
