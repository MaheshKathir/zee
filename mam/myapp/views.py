from django.shortcuts import render
# Create your views here.
def home(request):
    return render(request,'home.html' ,{'name':'madesh'})

def add(request):
    # Use request.GET.get() to handle the case where the parameters are missing
    val1 = int(request.GET('num1'))
    val2 = int(request.GET('num2'))
    res = val1 + val2
    print("res")
    return render(request, 'result.html', {"result": res})