from django.views.generic import ListView, DetailView  
from scape.models import Scape, Profile
from django.shortcuts import render


# Create your views here.
class ScapeView(ListView):
    model = Scape
    template_name = 'scape_list.html'


class  ScapeDetailView(DetailView):
    model = Scape  
    template_name = 'scape_details.html'

def profile_view(request, pk):
    scape_obj = Scape.objects.filter(owner=pk)
    profile_obj = Profile.objects.get(id=pk)
    
    plant_names= []

    for i in scape_obj:
        plant_scape = i.plants.all()
        for x in plant_scape:
            plant_names.append(x.name)
    
    
   
   
    context = {
        
        'profile' : profile_obj,
        'scapes' : scape_obj,
        'plant_names' : plant_names,
    }

    
    return render(request, 'user_details.html', context)
