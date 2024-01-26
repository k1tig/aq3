from django import forms
from catalog.models import TankSize, TankVolume, TankFilter, TankLight, TankCo2, TankSoil, TankHardscape
from flora.models import Plant
from fauna.models import Fish ,Invertebrate


class AddScape(forms.Form):
    name = forms.CharField(label= "Scape Name", max_length=200)
    # owner = user id logged in
    size =forms.ModelChoiceField(queryset=TankSize.objects.all())
    volume =forms.ModelChoiceField(queryset=TankVolume.objects.all())
    filter =forms.ModelChoiceField(queryset=TankFilter.objects.all())
    light =forms.ModelChoiceField(queryset=TankLight.objects.all())
    co2 =forms.ModelChoiceField(queryset=TankCo2.objects.all())
    soil =forms.ModelChoiceField(queryset=TankSoil.objects.all())
    hardscape =forms.ModelChoiceField(queryset=TankHardscape.objects.all())
    
    plants = forms.ModelMultipleChoiceField(queryset=Plant.objects.all())
    fish = forms.ModelMultipleChoiceField(queryset=Fish.objects.all())
    invertebrates = forms.ModelMultipleChoiceField(queryset=Invertebrate.objects.all())
