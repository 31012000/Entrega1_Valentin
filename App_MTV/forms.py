from django import forms

class formularioSucursal(forms.Form):
    
    direccion = forms.CharField()
    horario = forms.DateField()
    cantidad_empleados = forms.IntegerField()