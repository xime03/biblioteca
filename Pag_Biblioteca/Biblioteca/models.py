from django.db import models
# Create your models here.

class Persona(models.Model):
    per_nombre=models.CharField(max_length=25)
    per_apellido=models.CharField(max_length=25)
    

class Usuario(models.Model):
    usu_telefono=models.CharField(max_length=10)
    usu_direccion=models.CharField(max_length=50)
    usu_email=models.CharField(max_length=50)
    persona=models.ForeignKey(Persona)

class Autor(models.Model):
    aut_ciudadnacimiento=models.CharField(max_length=25)
    aut_fechanacimiento=models.DateField()
    persona=models.ForeignKey(Persona)
    
class Estado(models.Model):
    est_descripcion=models.CharField(max_length=50)

class Categoria(models.Model):
    cat_nombre=models.CharField(max_length=25)
    
class Editorial(models.Model):
    edi_nombre=models.CharField(max_length=25)
    edi_codigopostal=models.CharField(max_length=10)
    edi_direccion=models.CharField(max_length=50)
    edi_telefono=models.CharField(max_length=10)
    edi_email=models.CharField(max_length=50)
    
class Libro(models.Model):
    lib_titulo=models.CharField(max_length=40)
    lib_fechapublicacion=models.DateField()
    lib_numpaginas=models.IntegerField()
    lib_idioma=models.CharField(max_length=15)
    lib_resumen=models.CharField(max_length=200)
    lib_link=models.CharField(max_length=100)
    categoria=models.ForeignKey(Categoria)
    editorial=models.ForeignKey(Editorial)
    autor=models.ManyToManyField(Autor)
    estado=models.ForeignKey(Estado)

class Prestamos(models.Model):
    pre_fecprestamo=models.DateField()
    pre_fecdevolucion=models.DateField()
    usuario=models.ForeignKey(Usuario)
    libro=models.ForeignKey(Libro)
    
        
