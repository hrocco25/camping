from django import forms
from .models import Camp, Review

class CampForm(forms.ModelForm):

    class Meta:
        model = Camp
        fields = ('name', 'location', 'description', 'road', 'number_of_campsites', 'number_of_days', 'image')


class ReviewForm(forms.ModelForm):

    class Meta:
        model = Review
        fields = ('title', 'content', 'author',)