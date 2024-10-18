from django import forms
from .models import Member

class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = [
            'vorname',
            'nachname',
            'geburtsdatum',
            'geburtsort',
            'nationalitaet',
            'familienstand',
            'telefonnummer',
            'emailadresse',
            'beruf'
        ]
