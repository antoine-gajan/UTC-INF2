from django import forms
from .models import Simulation
from django.contrib.auth.models import User


#Formulaire pour les simulations
class SimuForm(forms.ModelForm):
    class Meta:
        model = Simulation
        fields = ['alpha', 'beta', 'gamma', 'delta', 'epsilon']

#Formulaire pour modifier un utilisateur
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

#Formulaire pour créer un utilisateur
class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        widgets = {'password': forms.PasswordInput()}

#Formulaire pour modifier le mot de passe
class UpdatePasswordForm(forms.Form):
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput())
    password2 = forms.CharField(label="Confirm your password", widget=forms.PasswordInput())

#Formulaire pour supprimer le compte
class DeleteAccountForm(forms.Form):
    choices = [('Yes', 'Yes'), ('No', 'No')]
    delete = forms.ChoiceField(label="Do you really want to delete your account ?", choices=choices, widget=forms.RadioSelect)

