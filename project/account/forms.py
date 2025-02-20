from allauth.account.forms import SignupForm
from django import forms

class CustomSignupForm(SignupForm):
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                'placeholder': 'exemple@gmail.com', 
                'class': 'form-control'
                }
            )
        )


    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                    'placeholder':'albert', 
                    'class':'form-control'
                }
            )
        )


    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'placeholder':'********', 
                'class':'form-control'
            }
        )
    )



    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder":"********", 
                "class": "form-control"
            }
        )
    )
   

    class Meta:
        fields = ('email', 'username', 'password1', 'password2')


