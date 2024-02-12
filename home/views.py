from django.shortcuts import render, HttpResponse


def index (request):
    return render(request, 'index.html')
    # return HttpResponse("this is homepage")
    
# def add(request):
    
#     val1 = request.GET['num1']
#     val2 = request.GET['num2']
#     res = val1 + val2
    
#     return render(request, 'result.html', {'result': res})

def about(request):
    return render(request, 'about.html')

def services(request):
     return render(request, 'Services.html')

def Contact(request):
    return render(request, 'Contact.html')

   
# Create your views here.
