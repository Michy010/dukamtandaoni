from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser, Business

class CustomUserCreationForm(UserCreationForm):
    # tin_number = forms.CharField(max_length=15, required=True, label="TIN Number", widget=forms.TextInput(attrs={
    #     'class': 'input-field', 'placeholder': 'Enter Your TIN'
    # }))
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={'class': 'input-field', 'placeholder': 'Enter Your Password'})
    )
    
    password2 = forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput(attrs={'class': 'input-field', 'placeholder': 'Confirm Your Password'})
    )

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'username':forms.TextInput(attrs={'class':'input-field','placeholder':'Enter Your Username'}),
            'email':forms.EmailInput(attrs={'class':'input-field', 'placeholder':'Enter Your Email'}),
            # 'password1':forms.PasswordInput(attrs={'class':'input-field', 'placeholder':'Enter Your Password'}),
            # 'password2':forms.PasswordInput(attrs={'class':'input-field', 'placeholder':'Confirm Your Password'}),
            # 'tin_number':forms.TextInput(attrs={'class':'input-field', 'placeholder':'Enter Your TIN'}),
        }

class BusinessRegistrationForm(forms.ModelForm):
    class Meta:
        model = Business
        fields = ['name', 'business_type', 'tin_number']
        labels = {
            'name':'Business Name',
        }
        widgets = {
            'name':forms.TextInput(attrs={'class':'input-field', 'placeholder':'Business Name'}),
            'business_type':forms.Select(attrs={'class':'input-field'}),
            'tin_number':forms.TextInput(attrs={'class':'input-field', 'placeholder':'Enter Your TIN'}),
        }

class BusinessSelectionForm(forms.Form):
    business = forms.ModelChoiceField(queryset=Business.objects.none(), label="Select Business")

    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['business'].queryset = Business.objects.filter(user=user)
