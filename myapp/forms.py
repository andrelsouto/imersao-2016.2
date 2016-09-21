from django import forms
from .models import Aluno, Endereco

class AlunoForm(forms.ModelForm):

	class Meta():
		model = Aluno
		fields = ('nome', 'email', 'sexo')

class EnderecoForm(forms.ModelForm):

	class Meta():
		model = Endereco
		fields = ('rua',)