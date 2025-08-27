# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class EntidadExterna(models.Model):
    ent_id = models.AutoField(primary_key=True)
    ent_nombre = models.CharField(max_length=100)
    ent_contacto = models.CharField(max_length=100, blank=True, null=True)
    ent_correo = models.CharField(max_length=100, blank=True, null=True)
    ent_telefono = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'entidad_externa'


class Localidad(models.Model):
    loc_id = models.AutoField(primary_key=True)
    loc_descripcion = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'localidad'


class Moderador(models.Model):
    mod_id = models.AutoField(primary_key=True)
    mod_nombre = models.CharField(max_length=50)
    mod_apellido = models.CharField(max_length=50)
    mod_correo = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'moderador'


class Reporte(models.Model):
    rep_id = models.AutoField(primary_key=True)
    tip = models.ForeignKey('TipoReporte', models.DO_NOTHING)
    rep_descripcion = models.CharField(max_length=255)
    rep_url_imagen = models.CharField(max_length=255)
    rep_nivel_incidencia = models.IntegerField()
    usu = models.ForeignKey('Usuario', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'reporte'


class Sector(models.Model):
    sec_id = models.AutoField(primary_key=True)
    loc = models.ForeignKey(Localidad, models.DO_NOTHING)
    sec_direccion = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'sector'


class Solucion(models.Model):
    sol_id = models.AutoField(primary_key=True)
    rep = models.ForeignKey(Reporte, models.DO_NOTHING)
    mod = models.ForeignKey(Moderador, models.DO_NOTHING)
    ent = models.ForeignKey(EntidadExterna, models.DO_NOTHING, blank=True, null=True)
    sol_fecha = models.DateField()
    sol_descripcion = models.TextField()

    class Meta:
        managed = False
        db_table = 'solucion'


class TipoReporte(models.Model):
    tip_id = models.AutoField(primary_key=True)
    tip_descripcion = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'tipo_reporte'


class Usuario(models.Model):
    usu_id = models.AutoField(primary_key=True)
    usu_nombre = models.CharField(max_length=50)
    usu_apellido = models.CharField(max_length=50)
    sec = models.ForeignKey(Sector, models.DO_NOTHING)
    usu_correo = models.CharField(max_length=80)

    class Meta:
        managed = False
        db_table = 'usuario'
