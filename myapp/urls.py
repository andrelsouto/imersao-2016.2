from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^cadastro/aluno/$', views.cadastro_aluno, name='cadastro_aluno'),
	url(r'^edita/aluno/(?P<pk>[0-9]+)/$', views.editar_aluno, name='edita_aluno'),
	url(r'^remove/aluno/(?P<pk>[0-9]+)/$', views.remover_aluno, name='remove_aluno'),
]