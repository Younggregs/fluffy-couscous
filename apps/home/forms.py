from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "name",
                "class": "form-control"
            }
        ))
    email = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "email",
                "class": "form-control"
            }
        ))
    message = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "message",
                "class": "form-control"
            }
        ))
