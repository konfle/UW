<<<<<<< HEAD
from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, label='Imię i Nazwisko', widget=forms.TextInput(attrs={'placeholder': 'Twoje dane'}))
    email = forms.EmailField(label='Email', widget=forms.TextInput(attrs={'placeholder': 'Twój email'}))
    message = forms.CharField(label='Wiadomość', widget=forms.Textarea(attrs={'placeholder': 'Twoja wiadomość'}))
=======
from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, label='Imię i Nazwisko',
                           widget=forms.TextInput(attrs={'placeholder': 'Twoje dane',
                                                         'class': 'form-control',
                                                         'id': 'name', 'name': 'name',
                                                         'type': 'text'}))
    email = forms.EmailField(label='Email', widget=forms.TextInput(attrs={'placeholder': 'Twój email',
                                                                          'class': 'form-control',
                                                                          'id': 'email',
                                                                          'name': 'email',
                                                                          'type': 'email'}))
    message = forms.CharField(label='Wiadomość', widget=forms.Textarea(attrs={'placeholder': 'Twoja wiadomość',
                                                                              'class': 'form-contorl',
                                                                              'id': 'message',
                                                                              'name': 'message',
                                                                              'rows': '6'}))
>>>>>>> added view after sent mesage and add attrs for form
