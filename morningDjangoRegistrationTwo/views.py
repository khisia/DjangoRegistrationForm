from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegistrationForm
from django.contrib.auth.decorators import login_required
from .models import Product

def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully')
            return redirect("register")
    else:
        form = UserRegistrationForm()
    return render(request,'register.html', {'form':form})
@login_required
def home(request):
    return render(request, 'home.html')
@login_required
def add_product(request):
    if request.method == "POST":
        p_name = request.POST.get("jina")
        p_quantity = request.POST.get("kiasi")
        p_price = request.POST.get("bei")
        product = Product(prod_name=p_name, prod_quantity=p_quantity, prod_price=p_price)
        product.save()
        messages.success(request, 'Product added successfully')
        return redirect('add-product')
    return render(request, 'add-product.html')
@login_required
def view_products(request):
    #select all the products from the database
    products= Product.objects.all()
    #render the template with products
    return render(request, 'products.html', {'products':products})

@login_required
def delete_product(request,id):
    #select the product you need to delete
    product = Product.objects.get(id=id)
    #finally delete the product
    product.delete()
    #Redirect back to products page with a success message
    messages.success(request, 'Product deleted successfully')
    return redirect('products')

@login_required
def update_products(request, id):
    #select the product to be updated
    product = Product.objects.get(id=id)
    # Check if the form has any submitted records to receive them
    if request.method == "POST":
        updated_name = request.POST.get('jina')
        updated_quantity = request.POST.get('kiasi')
        updated_price = request.POST.get('bei')
        # Update the selected product above with the received data
        product.prod_name = updated_name
        product.prod_quantity = updated_quantity
        product.prod_price = updated_price

        # Return the updated data back to the database
        product.save()
        # Redirect back to the products page with a success message
        messages.success(request, 'product updated successfully')
        return redirect('products')

    return render(request, 'update-product.html',{'product': product})










