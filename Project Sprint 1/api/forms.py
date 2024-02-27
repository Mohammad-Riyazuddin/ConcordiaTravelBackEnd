# travel/forms.py

from django import forms
from .models import Package, Flight, Hotel, Activity

class PackageForm(forms.ModelForm):
    class Meta:
        model = Package
        fields = ['name', 'description', 'travel_duration_days', 'flight', 'hotel', 'activity', 'price']

    def __init__(self, *args, **kwargs):
        super(PackageForm, self).__init__(*args, **kwargs)

        # Populate choices dynamically
        self.fields['flight'].queryset = Flight.objects.all()
        self.fields['hotel'].queryset = Hotel.objects.all()
        self.fields['activity'].queryset = Activity.objects.all()
