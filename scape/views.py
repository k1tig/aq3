from django.views.generic import ListView, DetailView  
from scape.models import Scape, Profile
from flora.models import Plant
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
    plants = Scape.objects.get(id=1)
    plants = plants.plants.all()
    profile_obj = Profile.objects.get(id=pk)
    
    
   
   
    context = {
        'pk' : pk,
        'name' : scape_obj[0].name,
        'profile' : profile_obj,
        'scapes' : scape_obj,
        'plants' : plants,
        



    }

    
    return render(request, 'user_details.html', context)



    

    

    
    


