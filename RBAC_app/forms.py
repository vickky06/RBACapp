from django import forms
from .models import wareHouse
from django.forms import ModelForm

class MySearch(ModelForm):
    CHOICES = [('1', 'Ascending'), ('2', 'Descending')]
    Order_By_Date = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES,)
    

    class Meta:
        model = wareHouse
        fields = ['claims','description','assigne',]


class ProxyForm(forms.Form):
    Proximity_String= forms.CharField(min_length=1, max_length=16,initial='enter space seperated value')
    Proximity_Range = forms.IntegerField(required=True,initial=0)


class DocumentForm(forms.ModelForm):
    class Meta:
        model = wareHouse
        fields = ['claims','description','assigne','document']




    