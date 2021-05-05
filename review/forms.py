from django.forms import ModelForm 
from .models import Review,ExpertProfile

class ReviewForm(ModelForm):
    class Meta:
        model=Review
        fields=['title','description']


class ExpertProfileForm(ModelForm):
    class Meta:
        model=ExpertProfile
        fields=['number','description','category','photo']
