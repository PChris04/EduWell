from django import forms

class MoodForm(forms.Form):
    MOOD_CHOICES = [
        ('stressed', 'Stressed'),
        ('neutral', 'Neutral'),
        ('happy', 'Happy'),
    ]

    mood = forms.ChoiceField(
        choices=MOOD_CHOICES,
        widget=forms.RadioSelect(attrs={'class': 'mood-option'})
    )

    journal_entry = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={
            'class': 'journal-textarea',
            'placeholder': 'Want to talk about it?',
            'rows': 3
        })
    )
