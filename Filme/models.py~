from django.db import models

# Create your models here.

#coding:utf-8
from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator

# Create your models here.

TIPO_FILME = [
      
      ('A','ACAO'),
      ('B','AVENTURA'),
      ('C','TERROR'),
      ('D','COMEDIA'),
      ('E','SUSPENSE'),
      ('F','ANIMACAO'),
      ('G','FICCAO'),
      ('H','DRAMA'),
      ('I','ROMANCE'),
     

]


class Filme (models.Model):
	NomeEvento = models.CharField('Nome do Filme',max_length=100,null=True)
	#TipoEvento = models.CharField('Tipo de Filme',max_length=1,choices=TIPO_FILME,null=True)
	Datalocacao = models.DateField('Data de Locacao',null=True)
	DataEntregue = models.DateField('Data Entregue',null=True)
	Dia Entregue = models.CharField('Dia Entregue',max_length=100,null=True)
	#DataLocacao = models.TimeField('DataLocacao',null=True)
	#ClienteLocacao = models.CharField('ClienteLocacao',max_length=100)
	 Tipo= models.IntegerField('Tipo de filme',null=True)
	
class Alocacao(models.Model):

	Alocacao = models.ForeignKey(Filme,verbose_name="Alocacao",null=False)
	#Alocacao = models.OneToOneField(Alocacao,verbose_name="Filme",null=False)
	NomeAloca = models.CharField('Nome do filme',max_length=100,null=True)
	Filme = models.CharField('Genero do filme',max_length=1,choices=TIPO_EVENTO,null=True)
	Cliente = models.ForeignKey('cadastro do Cliente',verbose_name="Alocacao do Filme",null=True)
	DatadaAlocacao = models.DateField('Data da Alocacao',null=True)
	DiaEntregue = models.IntegerField('Dia Entregue',null=True, help_text="Informar dias que o cliente ficou com o filme alocado")
	QuantdeFilmeAlugado = models.IntegerField('Quantidade de filme alocado',validators=[MinValueValidator(1),MaxValueValidator(1000)],null=True,)
	class Meta:
	verbose_name = "Alocacao"
	verbose_name_plural = "Alocacao"
	def __unicode__(self):
	return self.NomeAlocacao






 
