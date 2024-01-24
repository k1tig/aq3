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
