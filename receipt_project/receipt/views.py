from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegistrationForm, ReceiptForm
from django.contrib.auth.decorators import login_required
from .models import Receipt

@login_required
def index(request):
    receipts = Receipt.objects.all()
    return render(request, 'receipt/index.html', {'receipts': receipts})

def register(request):
    if request.method=='POST':
        form=RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form=RegistrationForm()

    return render(request,'receipt/register.html',{'form':form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('manage_receipts')
    else:
        form = AuthenticationForm()
    return render(request, 'receipt/login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('login')

@login_required
def manage_receipts(request):
    if not request.user.is_authenticated:
        return redirect('login')

    receipts=Receipt.objects.filter(user=request.user)

    if request.method=='POST':
        if form.is_valid():
            receipt=form.save(commit=False)
            receipt.user=request.user
            receipt.save()
            
            return redirect('manage_reciepts')

    else:
        form=ReceiptForm()

    return render(request,'receipt/manage_receipts.html', {'form': form, 'receipts': receipts})

@login_required
def delete_receipt(request, receipt_id):
    receipt = Receipt.objects.get(id=receipt_id)
    if receipt.user == request.user:
        receipt.delete()
    return redirect('manage_receipts')

@login_required
def add_receipt(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        try:
            price = float(request.POST.get('price'))
            quantity = int(request.POST.get('quantity'))
            total = price * quantity
            Receipt.objects.create(name=name, price=price, quantity=quantity, total=total, user=request.user)
        except ValueError:
            # Handle the error if conversion fails
            return render(request, 'receipt/index.html', {'receipts': Receipt.objects.filter(user=request.user), 'error': 'Invalid input for price or quantity.'})
    return redirect('index')

@login_required
def generate_bill(request):
    if not request.user.is_authenticated:
        return redirect('login')
    
    receipts = Receipt.objects.filter(user=request.user)
    total_amount = sum(receipt.total for receipt in receipts)
    
    return render(request, 'receipt/generate_bill.html', {'receipts': receipts, 'total_amount': total_amount})