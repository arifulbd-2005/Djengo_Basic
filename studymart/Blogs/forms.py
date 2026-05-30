from django import forms

class TeachersRegistration(forms.Form):
    first_name = forms.CharField(label='Enter Your Frist Name', label_suffix=' ', initial='Studymart')
    last_name = forms.CharField(label='Enter Your Last Name')
    email = forms.EmailField(initial='studymart@gmail.com', disabled=True)
    password = forms.CharField(widget=forms.PasswordInput)
    textarea = forms.CharField(widget=forms.Textarea)
    file = forms.CharField(widget=forms.FileInput)
    checkbox = forms.CharField(widget=forms.CheckboxInput)