from django.shortcuts import render, redirect
from django import forms
from django.utils import timezone
from . models import RCI, Reklamasi
from django.views.generic import CreateView, ListView
from django.views.generic.edit import FormView
from django.core.files.storage import FileSystemStorage

class CreateRCIView(CreateView):
    model = RCI
    fields = ['segmen', 'parameter1', 'parameter2', 'parameter3']
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


from django.http import HttpResponseRedirect
from . forms import UploadFileForm

def handle_upload_file(f):
        with open('media', 'wb+') as destination:
            for chunk in f.chunks():
                destination.write(chunk)

def upload_file(request):
    
    form = UploadFileForm()
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        
        if form.is_valid():
            fs = FileSystemStorage()
            fs.save(request.FILES['file'].name, request.FILES['file'])
            print(request.FILES['file'].name)
            return HttpResponseRedirect('/')
        else:
            form = UploadFileForm()
    
    context = {
        'form' : form
    }
    
    return render(request, 'matriks/upload.html', context)


class FileFieldForm(forms.Form):
    file_field = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))

class FileFieldView(FormView):
    form_class = FileFieldForm
    template_name = 'matriks/upload.html'  # Replace with your template.
    success_url = '/'  # Replace with your URL or reverse().

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        files = request.FILES.getlist('file_field')
        if form.is_valid():
            for f in files:
                handle_upload_file(request.FILES.getlist('file_field'))
            return self.form_valid(form)
        else:
            return self.form_invalid(form)