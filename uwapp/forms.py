from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, label='Imię i Nazwisko', widget=forms.TextInput(attrs={'placeholder': 'Twoje dane'}))
    email = forms.EmailField(label='Email', widget=forms.TextInput(attrs={'placeholder': 'Twój email'}))
    message = forms.CharField(label='Wiadomość', widget=forms.Textarea(attrs={'placeholder': 'Twoja wiadomość'}))
