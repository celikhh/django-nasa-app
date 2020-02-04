from django import forms


class SearchForm(forms.Form):
    keyword = forms.CharField()      #ADD MAX LENGHT etc
