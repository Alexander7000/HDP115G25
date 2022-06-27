from django.db import models
from django.contrib.auth.models import User


class Nacionalidad(models.Model):
    id_nacionalidad = models.AutoField(primary_key=True, verbose_name='Nacionalidad')
    nombre_nacion = models.CharField(max_length=30, null=False, blank=False)

    class Meta:
        db_table = 'nacionalidad'
        ordering = ["nombre_nacion"]

    def __str__(self):
        return self.nombre_nacion


class Transportista(models.Model):
    id_transportista = models.AutoField(primary_key=True)
    id_usuario = models.ForeignKey(User, on_delete=models.PROTECT, null=False, blank=False)
    id_nacionalidad = models.ForeignKey(Nacionalidad, on_delete=models.PROTECT,
                                        db_column='id_nacionalidad',
                                        null=False, blank=False)
    identificacion = models.CharField(max_length=20, null=False, blank=False)
    tipo_identificacion = models.CharField(max_length=50, null=False, blank=False)
    nombre_persona = models.CharField(max_length=50, null=False, blank=False)
    apellido = models.CharField(max_length=50, null=False, blank=False)
    telefono = models.IntegerField(blank=True, null=True)
    fecha_nacimiento = models.DateField(null=False, blank=False)
    direccion = models.CharField(max_length=100, null=False, blank=False)
    tipo_licencia = models.CharField(max_length=30, null=False, blank=False)

    class Meta:
        db_table = 'transportista'
        unique_together = (('id_usuario', 'id_nacionalidad', 'identificacion'),)
        ordering = ["id_transportista"]

    def __str__(self):
        return self.identificacion + " - " + self.id_nacionalidad.__str__() + " - " + self.nombre_persona + ", " + self.apellido


class Vehiculo(models.Model):
    id_vehiculo = models.AutoField(primary_key=True)
    id_usuario = models.ForeignKey(User, on_delete=models.PROTECT, db_column='id_usuario', null=False, blank=False)
    id_nacionalidad = models.ForeignKey(Nacionalidad, on_delete=models.PROTECT,
                                                      db_column='id_nacionalidad',
                                                      null=False, blank=False,)
    placa = models.CharField(max_length=10, null=False, blank=False)
    modelo = models.CharField(max_length=50, null=False, blank=False)
    ano = models.IntegerField(null=False, blank=False)
    cant_asientos = models.IntegerField(null=False, blank=False)
    color = models.CharField(max_length=30, null=False, blank=False)

    class Meta:
        db_table = 'vehiculo'
        unique_together = (('id_usuario','id_nacionalidad', 'placa'),)
        ordering = ["id_vehiculo"]

    def __str__(self):
        return self.placa + " - " + self.modelo + " - " + self.id_nacionalidad.__str__()


class Mercaderia(models.Model):
    id_mercaderia = models.AutoField(primary_key=True)
    nombre_mercaderia = models.CharField(max_length=50, null=False, blank=False)
    categoria = models.CharField(max_length=20, null=False, blank=False)
    cantidad = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)
    procedencia = models.CharField(max_length=50, null=False, blank=False)

    class Meta:
        db_table = 'mercaderia'
        ordering = ["id_mercaderia"]

    def __str__(self):
        return self.nombre_mercaderia + " (" + str(self.cantidad) + ")"


class Informe(models.Model):
    id_informe = models.AutoField(primary_key=True)
    id_usuario = models.ForeignKey(User, on_delete=models.PROTECT, db_column='id_usuario', null=False, blank=False)
    id_transportista = models.ForeignKey(Transportista, on_delete=models.PROTECT,
                                                        db_column='id_transportista',
                                                        null=False, blank=False)
    id_vehiculo = models.ForeignKey(Vehiculo, on_delete=models.PROTECT,
                                              db_column='id_vehiculo',
                                              null=False, blank=False)
    detalleMercaderia = models.ManyToManyField(Mercaderia)
    tipo_traslacion = models.CharField(max_length=20, null=False, blank=False)
    fecha = models.DateField(auto_now_add=True)

    class Meta:
        db_table = 'informe'
        ordering = ["id_informe"]