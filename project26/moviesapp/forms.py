from moviesapp.models import MovieTable
from django import forms

class MovieTableForm(forms.ModelForm):
	class Meta:
		model = MovieTable 
		fields = ('id', 'moviename', 'hero', 'heroine')