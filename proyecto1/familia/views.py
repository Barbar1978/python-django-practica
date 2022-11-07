from django.shortcuts import render
from familia.models import Entrada

# Create your views here.
def home(request):
    familia=Entrada.objects.all()
    return render(request, "familia_bonita.html", {'familia':familia})