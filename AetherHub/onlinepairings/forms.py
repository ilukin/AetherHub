from django import forms
from AetherHub.onlinepairings.models import Document, LookupField

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('document', 'current_round')

class PlayerLookupForm(forms.ModelForm):
    class Meta:
        model = LookupField
        fields = ('DCI_lookup', 'Table_lookup', ) 