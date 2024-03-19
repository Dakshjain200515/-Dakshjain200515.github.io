from django.shortcuts import render
from .models import Entry

def calculate(weight, rate):
    amount = (weight * rate / 10)
    gst = (amount * 0.03)
    tds = (amount * 0.001)
    final_amount = amount + gst - tds
    return amount, gst, tds, final_amount

def gst_calculator(request):
    entries = Entry.objects.all()
    total_weight = sum(entry.weight for entry in entries)
    total_final_amount = sum(entry.final_amount for entry in entries)
    context = {
        'entries': entries,
        'total_weight': total_weight,
        'total_final_amount': total_final_amount
    }
    return render(request, 'gstcalc/gst_calculator.html', context)

from django.shortcuts import render
from .models import Entry
from .utils import calculate  # Import the calculate function

def add_entry(request):
    if request.method == 'POST':
        party_name = request.POST.get('partyName')
        weight_str = request.POST.get('weight')
        rate_str = request.POST.get('rate')
        purity_str = request.POST.get('bill_purity')

        # Check if any of the form fields are None
        if party_name is not None and weight_str is not None and rate_str is not None and purity_str is not None:
            try:
                weight = float(weight_str)
                rate = float(rate_str)
                purity = float(purity_str)
            except ValueError:
                # Handle the case where conversion to float fails
                # You can redirect the user to an error page or display a message
                return render(request, 'gstcalc/error.html', {'message': 'Invalid input. Please enter valid numbers.'})

            amount, gst, tds, final_amount = calculate(weight, rate)  # Assuming calculate function is defined elsewhere
            Entry.objects.create(party_name=party_name, weight=weight, rate=rate, purity=purity, amount=amount, gst=gst, tds=tds, final_amount=final_amount)
            return render(request, 'gstcalc/success.html', {'message': 'Entry added successfully.'})  # Redirect to a success page or display a success message
        else:
            # Handle the case where any of the form fields are None
            # You can redirect the user to an error page or display a message
            return render(request, 'gstcalc/error.html', {'message': 'Missing form fields. Please fill out all the required fields.'})
    else:
        # Handle GET requests
        return render(request, 'gstcalc/error.html', {'message': 'Invalid request method.'})

from django.http import JsonResponse
from .models import Entry

def delete_entry(request, entry_id):
    if request.method == 'DELETE':
        try:
            entry = Entry.objects.get(pk=entry_id)
            entry.delete()
            return JsonResponse({'message': 'Entry deleted successfully'}, status=200)
        except Entry.DoesNotExist:
            return JsonResponse({'error': 'Entry not found'}, status=404)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)
