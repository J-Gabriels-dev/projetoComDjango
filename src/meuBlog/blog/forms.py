from django import forms 

class EmalIPostForm(forms.Form) :
    name = forms.CharField(max_length=25)
    email = forms.EmailField()
    to = forms.EmailField()
    comments = forms.CharField(
        required= False,
        widget = forms.Textarea
    )