# forms.py
from django import forms
from .models import Membership

class MembershipForm(forms.ModelForm):
    class Meta:
        model = Membership
        fields = ['full_name', 'phone_number', 'email', 'membership_type']
