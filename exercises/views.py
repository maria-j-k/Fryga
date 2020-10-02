from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.views import View

from .forms import BankForm
from .models import Bank


# Create your views here.

def index(request):
    return render(request, 'exercises/index.html')


def bank(request):
    exercises_list = Bank.objects.order_by('-day')
    context = {
        'exercises_list': exercises_list,
        'exercise_add': 'bank_add',
        'exercise_edit': 'bank_edit',
    }
    return render(request, 'exercises/exercise.html', context=context)


def bank_add(request):
    bank_form = BankForm()
    context = {
        'form': bank_form,
        'page_title': 'Ławka - dodaj ćwiczenie'
    }
    if request.method == 'POST':
        bank_form = BankForm(request.POST)
        if bank_form.is_valid():
            bank_form.save()
            return redirect(reverse('exercises:bank'))
    return render(request, 'exercises/exercise_form.html', context=context)


def bank_edit(request, bank_pk):
    bank = get_object_or_404(Bank, pk=bank_pk)
    bank_form = BankForm(request.POST or None, instance=bank)
    context = {
        'form': bank_form,
        'page_title': 'Ławka - edytuj ćwiczenie'
    }
    if bank_form.is_valid():
        bank_form.save()
        print(request)
        return redirect(reverse('exercises:bank'))
    return render(request, 'exercises/exercise_form.html', context=context)
