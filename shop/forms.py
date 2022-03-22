from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Repair

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=222 , required=True)
    last_name = forms.CharField(max_length=222,required=True)
    email =forms.EmailField(max_length=222,help_text='Ex. @gmail.com')

    class Meta:
        model = User
        fields = ('first_name','last_name','username','email','password1','password2')

class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)



class RepairForm(forms.ModelForm):
    class Meta:
        model = Repair
        fields = "__all__"