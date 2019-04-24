from django.shortcuts import render, redirect
from django import forms
from django.utils import timezone
from . models import RCI, Reklamasi
from django.views.generic import CreateView, ListView

class CreateRCIView(CreateView):
    model = RCI
    fields = ['nama', 'parameter1', 'parameter2', 'parameter3']
    success_url = '/listrci'
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class RCIList(ListView):
    model = RCI
    context_object_name = 'rci'
    template_name='matriks/rci.html'
    ordering= ['-parameter1']
    paginate_by = 5

class CreateReklamasiView(CreateView):
    model = Reklamasi
    fields = ['nama', 'parameter1', 'parameter2', 'parameter3']
    success_url = '/listreklamasi'
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class ReklamasiList(ListView):
    model = Reklamasi
    context_object_name = 'reklamasi'
    template_name='matriks/reklamasi.html'
    ordering= ['-nama']
    paginate_by = 5

def matriks(request):
    search_term=''
    search_term_years=''
    reklamasi = Reklamasi.objects.all()
    rci = RCI.objects.all()

    if 'search' in request.GET:
        search_term = request.GET['search']
        rci = rci.filter(segmen__icontains=search_term)

    if 'search_years' in request.GET:
        search_term_years = request.GET['search_years']
        rci = rci.filter(years__icontains=search_term_years)

    context = {
        'reklamasi' : reklamasi,
        'rci' : rci,
        'search_term' : search_term
    }
    return render(request, 'matriks/matriks.html', context)