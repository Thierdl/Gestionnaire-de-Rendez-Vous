from django import forms

class ResearchForm(forms.Form):
    query=forms.CharField(label="recherche", max_length=255)
                          