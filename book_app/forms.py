from django import forms
from .models import *
from django.contrib.auth.models import User

# form for registration:
class regform(forms.ModelForm):
    class Meta:
        model=regmodel
        fields='__all__'



# loginform:
class logform(forms.Form):
    email=forms.EmailField()
    psw=forms.CharField(max_length=50)




# form for bookmodel:
class bookform(forms.ModelForm):
    class Meta:
        model=bookmodel
        fields='__all__'


#forms for userprofile:
class userprofileform(forms.ModelForm):
    class Meta:
        model=userprofilemodel
        fields='__all__'


# audiobook upload:
class audiobookform(forms.ModelForm):
    class Meta:
        model=audiobookmodel
        fields='__all__'