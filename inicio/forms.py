from django import forms

class FormularioBaseAuto(forms.Form):
    patente = forms.CharField(max_length=20)
    marca = forms.CharField(max_length=30)
    ano = forms.IntegerField()
    
class FomularioCreacionAuto(FormularioBaseAuto):
    patente = forms.CharField(max_length=20)
    marca = forms.CharField(max_length=30)
    ano = forms.IntegerField()
    
class FomularioEdicionAuto(FormularioBaseAuto):
    nafta = forms.IntegerField()
    
class FomularioBusquedaAuto(forms.Form):
    patente = forms.CharField(max_length=20, required=False)
    
    