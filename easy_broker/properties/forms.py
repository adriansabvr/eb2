from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    phone = forms.CharField()
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)
