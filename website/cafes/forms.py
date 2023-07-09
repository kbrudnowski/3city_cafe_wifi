from django import forms


class CreateNewList(forms.Form):
    name = forms.CharField(label = "Name", max_length = 200)
    photo = forms.CharField(label = "Photo link", max_length = 400)
    location = forms.CharField(label = "Location link", max_length = 400)
    g_rating = forms.DecimalField(label = "Google Rating", max_digits = 2, decimal_places = 1)
    work_conditions = forms.DecimalField(label = "Work Conditions (out of 5.0)", max_digits = 2, decimal_places = 1)

