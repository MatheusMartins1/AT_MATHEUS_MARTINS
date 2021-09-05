from django import forms

class CaminhoPastaForm(forms.Form):
    caminho_pasta = forms.CharField(label='caminho_pasta', max_length=1000)