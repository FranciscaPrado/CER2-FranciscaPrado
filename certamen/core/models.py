from django.db import models

class residencia(models.Model):
    numero_res = models.CharField(max_length = 30)
    dueño_res = models.CharField(max_length = 30)
    fono_dueño = models.CharField(max_length = 30)

class correspondencia(models.Model):
    fecha_recepcion = models.DateField()
    conserje = models.CharField(max_length=30)
    remitente = models.CharField(max_length=30)
    destinatario = models.CharField(max_length=30)
    estado = models.CharField(max_length=30)
    numero_res = models.ForeignKey(residencia, on_delete=models.CASCADE)
