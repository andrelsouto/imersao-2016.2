from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import AlunoForm, EnderecoForm
from .models import Aluno, Endereco

@login_required
def index(request):
	alunos = Endereco.objects.all()
	return render(request, 'myapp/index.html', {'alunos' : alunos})

@login_required
def cadastro_aluno(request):

	if request.method == "POST":
		formAluno = AlunoForm(request.POST)
		formEndereco = EnderecoForm(request.POST)
		if formAluno.is_valid() and formEndereco.is_valid():
			postAluno = formAluno.save()
			postEndereco = formEndereco.save(commit=False)
			postEndereco.id_aluno = postAluno
			postEndereco.save()
			return redirect('myapp.views.index')

	return render(request, 'myapp/cadastro_aluno.html')

@login_required
def editar_aluno(request, pk):
	endereco = get_object_or_404(Endereco, pk=pk)
	aluno = get_object_or_404(Aluno, pk=endereco.id_aluno.id_aluno)
	if request.method == "POST":
		formAluno = AlunoForm(request.POST, instance=aluno)
		formEndereco = EnderecoForm(request.POST, instance=endereco)
		if formAluno.is_valid and formEndereco.is_valid():
			postAluno = formAluno.save()
			postEndereco = formEndereco.save(commit=False)
			postEndereco.id_aluno = postAluno
			postEndereco.save()
			return redirect('myapp.views.index')

	return render(request, 'myapp/cadastro_aluno.html', {'aluno' : aluno, 'endereco' : endereco})

@login_required
def remover_aluno(request, pk):
	endereco = get_object_or_404(Endereco, pk=pk)
	aluno = get_object_or_404(Aluno, pk=endereco.id_aluno.id_aluno)
	endereco.id_aluno = None
	endereco.delete()
	aluno.delete()
	return redirect('myapp.views.index')