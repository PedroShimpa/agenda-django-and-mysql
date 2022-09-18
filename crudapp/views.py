from django.shortcuts import render, redirect, get_object_or_404
from .models import Contact
from .forms import ContactForm
from django.views.generic import ListView, DetailView


class IndexView(ListView):
    template_name = 'crudapp/index.html'
    context_object_name = 'contact_list'

    def get_queryset(self):
        return Contact.objects.all()


def contact_detail_view(request, primary_key):
    contact = get_object_or_404(Contact, pk=primary_key)
    return render(request, 'catalog/contact_detail.html', context={'contact': contact})


class ContactDetailView(DetailView):

    model = Contact

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


def create(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    form = ContactForm()

    return render(request, 'crudapp/create.html', {'form': form})


def edit(request, pk):
    contact = get_object_or_404(Contact, pk=pk)

    form = ContactForm(request.POST or None,  instance=contact)
    if form.is_valid():
        form.save()
        return redirect('index')
    return render(request, 'crudapp/edit.html', {'form': form})


def delete(request, pk, template_name='crudapp/confirm_delete.html'):
    contact = get_object_or_404(Contact, pk=pk)
    if request.method == 'POST':
        contact.delete()
        return redirect('index')
    return render(request, template_name)
