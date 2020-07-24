from django import forms
from .models import SearchBar

class SearchForm(forms.ModelForm):
    search = forms.CharField(widget=forms.TextInput(attrs={
        "type": "search",
        "name": "search",
        "id": "search",
        "placeholder":"Search",
    }), label="")

    class Meta:
        model = SearchBar
        fields = ('search', )