from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from scape.models import Scape, Profile
from django.shortcuts import render
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin

class CustomLoginView(LoginView):
    template_name = 'base/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('home')

class HomePageView(TemplateView):
    template_name = 'home.html'
    
class ScapeView(ListView):
    model = Scape
    template_name = 'scape_list.html'

class  ScapeDetailView(DetailView):
    model = Scape  
    template_name = 'scape_details.html'

def profile_view(request, pk):
    clean_list=[]
    plant_list=[]
    
    profile_obj = Profile.objects.get(id=pk)
    scapes = Scape.objects.filter(owner=pk)

    for i in scapes:
        scape = i.plants.all()
        for x in scape:
            plant_list.append(x)
    
    [clean_list.append(x) for x in plant_list if x not in clean_list]    
    
    plant_list = clean_list

    

    context = {
        'scapes' : scapes,
        'profile' : profile_obj,
        'plant_list' : plant_list,
        
    }
    
    return render(request, 'user_details.html', context)

class ScapeCreate(LoginRequiredMixin, CreateView):
    model = Scape
    fields = '__all__'
    template_name = 'scape_add.html'
    success_url = reverse_lazy('scape')

class ScapeEdit(UpdateView):
    model =  Scape
    fields = '__all__'
    template_name = 'scape_edit.html'
    success_url = reverse_lazy('scape')

class ScapeDelete(DeleteView):
    model = Scape
    context_object_name = 'scape'
    template_name = 'scape_delete.html'
    success_url = reverse_lazy('scape')