from django import forms

from .models import Company


class CompanyCreationForm(forms.ModelForm):
    """
    Create team from team_name and password
    """

    class Meta:
        model = Company
        fields = ('email', 'name', 'location', 'domain', 'website',
                  'linkedin', 'github', 'twitter', 'angelist', 'blog',
                  'phone', 'achivements', )
        labels = {
            'email': 'Email',
            'name': 'Name',
            'location': 'Location',
            'domain': 'Domain',
            'website': 'Website',
            'linkedin': 'LinkedIn',
            'github': 'GitHub',
            'twitter': 'Twitter',
            'angelist': 'Angelist',
            'blog': 'Blog',
            'phone': 'Phone',
            'achivements': 'Achivements'
        }
