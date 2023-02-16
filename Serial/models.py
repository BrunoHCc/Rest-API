from django.db import models

# Create your models here.

class Base(models.Model):
    criacao = models.DateTimeField(auto_now_add=True)
    atualizacao = models.DateTimeField(auto_now=True)
    ativo = models.BooleanField(default=True)


class Cursos(Base):
    titulo = models.CharField(max_length=100)
    url = models.URLField(unique=True)

    def __str__(self):
        return self.titulo

class Avaliacao(Base):
        curso = models.ForeignKey(Cursos, related_name='avaliacoes', on_delete=models.CASCADE)
        nome = models.CharField(max_length=100)
        email = models.EmailField()
        comentario = models.TextField(blank=True, default="")
        #avaliacao = models.DecimalField(max_digits=2, decimal_places=1)
        
        def __str__(self):
            return self.nome
