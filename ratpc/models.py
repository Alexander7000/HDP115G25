from django.db import models

class Libro(models.Model):
    id=models.AutoField(primary_key=True)
    titulo=models.CharField(max_length=100, verbose_name='Titulo')

    def __str__(self):
        return 'id: %s, nombre: %s' % (self.id, self.titulo)

    class Meta:
        ordering = ["id"]


class Nacionalidad(models.Model):
    id_nacionalidad = models.AutoField(primary_key=True)
    nombre_nacion = models.CharField(max_length=30, null=False, blank=False)

    class Meta:
        db_table = 'nacionalidad'


class Persona(models.Model):
    id_persona = models.AutoField(primary_key=True)
    id_nacionalidad = models.ForeignKey(Nacionalidad, on_delete=models.CASCADE,
                                                      db_column='id_nacionalidad',
                                                      null=False, blank=False)
    identificacion = models.CharField(max_length=20, null=False, blank=False)
    tipo_identificacion = models.CharField(max_length=50, null=False, blank=False)
    nombre_persona = models.CharField(max_length=50, null=False, blank=False)
    apellido = models.CharField(max_length=50, null=False, blank=False)
    telefono = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'persona'
        unique_together = (('id_nacionalidad', 'identificacion'),)


class Transportista(models.Model):
    id_transportista = models.AutoField(primary_key=True)
    id_persona = models.OneToOneField(Persona, on_delete=models.CASCADE, null=False, blank=False)
    fecha_nacimiento = models.DateField(null=False, blank=False)
    direccion = models.CharField(max_length=100, null=False, blank=False)
    tipo_licencia = models.CharField(max_length=30, null=False, blank=False)

    class Meta:
        db_table = 'transportista'


class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    id_persona = models.OneToOneField(Persona, on_delete=models.CASCADE, null=False, blank=False)
    nombre_usuario = models.CharField(unique=True, max_length=50, null=False, blank=False)
    clave = models.CharField(max_length=20, null=False, blank=False)
    email = models.CharField(max_length=50, null=False, blank=False)
    es_agente = models.BooleanField(null=False, blank=False, default=False)

    class Meta:
        db_table = 'usuario'


class Vehiculo(models.Model):
    id_vehiculo = models.AutoField(primary_key=True)
    id_nacionalidad = models.ForeignKey(Nacionalidad, on_delete=models.CASCADE,
                                                      db_column='id_nacionalidad',
                                                      null=False, blank=False)
    placa = models.CharField(max_length=10, null=False, blank=False)
    modelo = models.CharField(max_length=50, null=False, blank=False)
    ano = models.IntegerField(null=False, blank=False)
    cant_asientos = models.IntegerField(null=False, blank=False)
    color = models.CharField(max_length=30, null=False, blank=False)

    class Meta:
        db_table = 'vehiculo'
        unique_together = (('id_nacionalidad', 'placa'),)


class Informe(models.Model):
    id_informe = models.AutoField(primary_key=True)
    id_transportista = models.ForeignKey(Transportista, on_delete=models.CASCADE,
                                                        db_column='id_transportista',
                                                        null=False, blank=False)
    id_vehiculo = models.ForeignKey(Vehiculo, on_delete=models.CASCADE,
                                              db_column='id_vehiculo',
                                              null=False, blank=False)
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE,
                                            db_column='id_usuario',
                                            null=False, blank=False)
    tipo_traslacion = models.CharField(max_length=20, null=False, blank=False)
    fecha = models.DateField(auto_now_add=True)

    class Meta:
        db_table = 'informe'


class Mercaderia(models.Model):
    id_mercaderia = models.AutoField(primary_key=True)
    detalleMercaderia = models.ManyToManyField(Informe)
    nombre_mercaderia = models.CharField(max_length=50, null=False, blank=False)
    categoria = models.CharField(max_length=20, null=False, blank=False)
    cantidad = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)
    procedencia = models.CharField(max_length=50, null=False, blank=False)

    class Meta:
        db_table = 'mercaderia'