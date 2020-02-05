from django import forms


class SearchForm(forms.Form):
    keyword = forms.CharField(max_length=24)      #ADD MAX LENGHT etc
