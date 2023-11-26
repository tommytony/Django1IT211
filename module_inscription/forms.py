from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class RegisterUserForm(UserCreationForm):
    
    
    ROLE = [
        ('abonne', "Abonné"),
        ('createur', "créateur"),
        ('adminitrateur', "Administrateur"),    
    ]
    
    
    
    first_name = forms.CharField(max_length=3000,required=True,widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=3000,widget=forms.TextInput(attrs={'class': 'form-control'}))
    date_of_birth = forms.DateField(required=True,widget=forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Year-Mouth-Day'}))
    role = forms.ChoiceField(required=True,choices=ROLE ,  widget=forms.Select(attrs={'class': 'form-control'}))
    email_address = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control'}))
    
    
  
    class Meta:
        model = User 
        fields=('username', 'first_name', 'last_name', 'last_name', 'email_address' ,'date_of_birth', 'role' , 'password1', 'password2') 
    
    def __init__(self, *args, **kwargs):
        super(RegisterUserForm, self).__init__(*args, **kwargs)
        
        self.fields['username'] .widget.attrs['class'] = 'form-control'
        self.fields['password1'] .widget.attrs['class'] = 'form-control'
        self.fields['password2'] .widget.attrs['class'] = 'form-control'