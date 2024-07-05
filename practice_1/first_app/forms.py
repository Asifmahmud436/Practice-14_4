from django import forms
import datetime

yearChoice = ['1980', '1981', '1982']
colors = [
    ('blue', 'Blue'),
    ('green', 'Green'),
    ('black', 'Black'),
]

class Practice_day1(forms.Form):
    name = forms.CharField()
    age = forms.DecimalField()
    password = forms.CharField(widget = forms.PasswordInput()) 
    comment = forms.CharField(widget=forms.Textarea(attrs={'rows':3}))
    email = forms.EmailField()
    agree = forms.BooleanField()
    date= forms.DateField()
    # birth_date = forms.DateField(widget=NumberInput(attrs={'type': 'date'}))
    birth_year = forms.DateField(widget=forms.SelectDateWidget(years=yearChoice))
    day = forms.DateField(initial=datetime.date.today)

    favorite_colors = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,choices=colors,)
    favorite_color = forms.ChoiceField(choices=colors)





