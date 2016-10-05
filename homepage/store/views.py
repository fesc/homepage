from django.shortcuts import render

# Create your views here.
# views.py는 model.py에서 필요한 정보를 받아와서 template에 전달하는 역할

def product_list(request):
    return render(request, 'store/products.html', {})