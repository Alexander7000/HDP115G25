from django.db import models

class Libro(models.Model):
    id=models.AutoField(primary_key=True)
    titulo=models.CharField(max_length=100, verbose_name='Titulo')

#blank=False, null=False

    def __str__(self):
        return 'id: %s, nombre: %s' % (self.id, self.titulo)

    class Meta:
        ordering = ["id"]

