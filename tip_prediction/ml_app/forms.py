from django import forms

class TipPredictionForm(forms.Form):
    total_bill = forms.FloatField(
        label="Total Bill",
        min_value=0.0,
        widget=forms.NumberInput(attrs={"class": "form-control", "step": "0.01", "placeholder": "e.g. 20.50"})
    )

    sex = forms.ChoiceField(
        label="Sex",
        choices=[("Female", "Female"), ("Male", "Male")],
        widget=forms.Select(attrs={"class": "form-control"})
    )

    smoker = forms.ChoiceField(
        label="Smoker",
        choices=[("No", "No"), ("Yes", "Yes")],
        widget=forms.Select(attrs={"class": "form-control"})
    )

    day = forms.ChoiceField(
        label="Day",
        choices=[("Thur", "Thur"), ("Fri", "Fri"), ("Sat", "Sat"), ("Sun", "Sun")],
        widget=forms.Select(attrs={"class": "form-control"})
    )

    time = forms.ChoiceField(
        label="Time",
        choices=[("Lunch", "Lunch"), ("Dinner", "Dinner")],
        widget=forms.Select(attrs={"class": "form-control"})
    )

    size = forms.IntegerField(
        label="Party Size",
        min_value=1,
        widget=forms.NumberInput(attrs={"class": "form-control", "placeholder": "Number of people"})
    )