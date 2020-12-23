from django.shortcuts import redirect, render, get_object_or_404
from .forms import BodyMassIndexForm

# Create your views here.

def body_mass_index_view(request):
    if request.method == "POST":
        form = BodyMassIndexForm(request.POST)
        if form.is_valid():
            height = form.cleaned_data["height"]
            weight = form.cleaned_data["weight"]
            bmi = weight/(height**2)
            return render(request, "body_mass_index/bmi.html", {"form": form, "bmi": bmi})
    else:
        form = BodyMassIndexForm()
    return render(request, "body_mass_index/bmi.html", {"form": form})


