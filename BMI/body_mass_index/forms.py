from django import forms


class BodyMassIndexForm(forms.Form):
    #height is in meters
    #weight is in kg
    name = forms.CharField(max_length=50, required=False)
    weight = forms.DecimalField(label="Weight in kg:", required=True, min_value=0)
    height = forms.DecimalField(label="Height in meters:", required=True, min_value=0)
    
