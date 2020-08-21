from django import forms
from homepage.models import Roast_Boast

class Add_Roast_Boast(forms.ModelForm):
    class Meta:
        model = Roast_Boast
        fields = ["content", "is_boast"]