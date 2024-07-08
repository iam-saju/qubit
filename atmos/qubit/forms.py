from django.forms import ModelForm
from .models import auto


class userform(ModelForm):
    class Meta:
        model=auto
        fields=['no']