from django import forms
from .models import Pokemon, Trainer

##
class TrainerForm(forms.ModelForm):
    class Meta:
        model = Trainer
        fields = '__all__'
        labels = {
            'first_name': 'Nombre',
            'last_name' : 'Apellido',
            'birth_date': 'Nacimiento',
            'level': 'nivel',
            'picture': 'Foto'
        }
        widgets = {
            'first_name' : forms.TextInput(attrs={'class': 'form-control'}),
            'last_name' : forms.TextInput(attrs={'class': 'form-control'}),
            'birth_date' : forms.DateInput(attrs={'class': 'form-control'}),
            'level' : forms.NumberInput(attrs={'class': 'form-control'}),
            'picture' : forms.ClearableFileInput(attrs={'class': 'form-control'})
        }



class PokemonForm(forms.ModelForm):
    class Meta:
        model = Pokemon
        fields = '__all__'
        labels = {
            'name': 'Nombre',
            'type' : 'Tipo',
            'height': 'Altura',
            'weight': 'Peso',
            'trainer': 'Entrenador',
            'picture': 'Foto'
        }
        widgets = {
            'name' : forms.TextInput(attrs={'class': 'form-control'}),
            'type' : forms.Select(attrs={'class': 'form-control'}),
            'height' : forms.NumberInput(attrs={'class': 'form-control'}),
            'weight' : forms.NumberInput(attrs={'class': 'form-control'}),
            'trainer' : forms.Select(attrs={'class': 'form-control'}),
            'picture' : forms.ClearableFileInput(attrs={'class': 'form-control'})
        }
        