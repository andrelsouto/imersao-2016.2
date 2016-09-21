from django.db import models

Sexo_Choices = (
	('M','Masculino'),
	('F','Feminino')
	)

class Aluno(models.Model):
	id_aluno = models.AutoField(primary_key=True,auto_created=True)
	nome = models.CharField('Nome',max_length=100)
	email = models.EmailField('Email',max_length=100)
	sexo = models.CharField('Sexo',choices=Sexo_Choices,max_length=15)
	def __unicode__(self):
		return self.nome
	
class Endereco(models.Model):
	id_endereco = models.AutoField(primary_key=True,auto_created=True)
	rua = models.CharField('Rua',max_length=100)
	id_aluno = models.OneToOneField(Aluno, null=True)
	def __unicode__(self):
		return self.rua