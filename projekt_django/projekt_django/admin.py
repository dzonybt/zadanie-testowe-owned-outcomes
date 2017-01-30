from django.forms import ModelForm, TextInput
from django.contrib.admin import ModelAdmin

from django.contrib import admin
from.models import Frase, Url


class FraseForm(ModelForm):
    class Meta:
        widgets = {
            'frase': TextInput(attrs={'class': 'input-mini'})
        }


class FraseAdmin(ModelAdmin):
    form = FraseForm

admin.site.register(Frase, FraseAdmin)
admin.site.register(Url)