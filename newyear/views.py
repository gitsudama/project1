from django.shortcuts import render

# Create your views here.
def newyear(request):
    return render(request, "newyear/index.html")

def greet(request, name):
    return render(request, "newyear/greet.html", {
        "name": name.upper(),
    })