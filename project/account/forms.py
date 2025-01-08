from django import forms

class Login(forms.Form):
    username=forms.CharField(label="Nom d'Utilisateur",
                             widget=forms.TextInput(
                                 attrs={
                                     "class":"form-control"
                                 }
                            ))
    
    password=forms.CharField(label="Votre Mot de Passe",
                             widget=forms.PasswordInput(
                                 attrs={
                                     "class":"form-control"
                                 }
                             )
                             )




class Signup(forms.Form):
    name=forms.CharField(max_length=50, label="Votre Nom",
                         widget=forms.TextInput(
                                attrs={
                                  "class":"form-control"
                                }
                              ))
                          
    firstname=forms.CharField(max_length=50, label="Votre Prénom", 
                        widget=forms.TextInput(
                            attrs={
                                "class":"form-control"
                            }
                        ))
    
    adress=forms.CharField(max_length=50, label="Votre Adress", 
                        widget=forms.TextInput(
                            attrs={
                                "class":"form-control"
                            }
                        ))
    
    password=forms.CharField(label="Mot de passe",
                             widget=forms.PasswordInput(
                                 attrs={
                                     "class":"form-control"
                                 }
                             ) )

