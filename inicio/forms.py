from django import forms

class FomularioCreacionAuto(forms.Form):
    patente = forms.CharField(max_length=20)
    marca = forms.CharField(max_length=30)
    ano = forms.IntegerField()
    