from django import forms


class ContactForm(forms.Form):
    subject = forms.CharField(
        max_length=100,
        min_length=5,
        required=True,
        widget=forms.TextInput(
            attrs={'class': 'form round', 'name': 'subject','placeholder': 'Subject'}
        )
    )
    message = forms.CharField(
        max_length=100,
        min_length=5,
        required=True,
        widget=forms.TextInput(
            attrs={'class': 'form textarea round', 'name': 'subject','placeholder': 'Subject'}
        )
    )
    email = forms.CharField(
        max_length=100,
        min_length=5,
        required=True,
        widget=forms.TextInput(
            attrs={'class': 'form round', 'name': 'email','placeholder': 'Email'}
        )
    )
    name = forms.CharField(
        max_length=100,
        min_length=5,
        required=True,
        widget=forms.TextInput(
            attrs={'class': 'form round', 'name': 'name','placeholder': 'Name'}
        )
    )

