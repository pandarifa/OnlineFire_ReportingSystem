from django.forms import ModelForm
from .models import TeamLocation
class TeamLocationForm(ModelForm):
    class Meta:
        model = TeamLocation
        fields = ['team','lat','lon']