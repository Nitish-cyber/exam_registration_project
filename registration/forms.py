# registration/forms.py
from django import forms

class ExamRegistrationForm(forms.Form):
    name = forms.CharField(max_length=100, label='Full Name')
    email = forms.EmailField(label='Email')
    father_name = forms.CharField(max_length=100, label="Father's Name")
    mother_name = forms.CharField(max_length=100, label="Mother's Name")
    gender = forms.ChoiceField(label='Gender', choices=(('male', 'Male'), ('female', 'Female')))
    date_of_birth = forms.DateField(label='Date of Birth')
    address = forms.CharField(widget=forms.Textarea, label='Address')
    city = forms.CharField(max_length=100, label='City')
    state = forms.CharField(max_length=100, label='State')
    country = forms.CharField(max_length=100, label='Country')
    phone_number = forms.CharField(max_length=15, label='Phone Number')
    qualifications = forms.CharField(widget=forms.Textarea, label='Qualifications')
    photo = forms.ImageField(label='Photo')
    signature = forms.ImageField(label='Signature')
    declaration = forms.BooleanField(label='I agree to the terms and conditions')
