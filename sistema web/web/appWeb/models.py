from django.db import models

# Create your models here.

class Area(models.Model):
	idArea=models.AutoField(primary_key=True)
	nombArea=models.CharField(max_length=75, verbose_name='Nombre Areas')

	class Meta:
		db_table='area'

	def __str__(self):
		return u'%s' %self.nombArea

class Tema(models.Model):
	idTema=models.AutoField(primary_key=True)
	nombTema=models.CharField(max_length=75, verbose_name='Nombre Area de Competencia')
	detalleTema=models.CharField(max_length=75, verbose_name='Detalle Tema')

	class Meta:
		db_table='tema'

	def __str__(self):
		return u'%s' %self.nombTema

class TipoCuest(models.Model):
	idTipoCuest=models.AutoField(primary_key=True)
	nombCuest=models.CharField(max_length=75, verbose_name='Tipo de cuestionario')

	class Meta:
		db_table='tipoCuest'

	def __str__(self):
		return u'%s' %self.nombCuest	

class Dependencia(models.Model):
	idDependencia=models.AutoField(primary_key=True)
	nombDependencia=models.CharField(max_length=75, verbose_name='Nombre Dependencia')

	tipoDep=models.ForeignKey(tipoDep, models.DO_NOTHING, db_column='idTipoDep')
	idArea=models.ForeignKey(area, models.DO_NOTHING, db_column='idArea')


	class Meta:
		db_table='dependencia'

	def __str__(self):
		return u'%s' %self.nombDependencia	

class Subtema(models.Model):
	idSubtema=models.AutoField(primary_key=True)
	nombSubtema=models.CharField(max_length=75, verbose_name='Nombre Competencia')
	detalleSubtema=models.CharField(max_length=75, verbose_name='Detalle Subtema')

	idTema=models.ForeignKey(tema, models.DO_NOTHING, db_column='idTema')

	class Meta:
		db_table='subtema'

	def __str__(self):
		return u'%s' %self.nombSubtema	

class TipoDep(models.Model):
	idTipoDep=models.AutoField(primary_key=True)
	nombTipoDep=models.CharField(max_length=75, verbose_name='Nombre Tipo de Dependencia')
	tipoDep=models.IntegerField()

	class Meta:
		db_table='tipoDep'

	def __str__(self):
		return u'%s' %self.nombTipoDep	

class TipoUsr(models.Model):
	idTipoUsr=models.AutoField(primary_key=True)
	nombTipoIsr=models.CharField(max_length=75, verbose_name='Nombre Usuario')
	tipoUsr=models.IntegerField()

	class Meta:
		db_table='tipoUsr'

	def __str__(self):
		return u'%s' %self.nombTipoUsr

class Usuarios(models.Model):
	idUsr=models.AutoField(primary_key=True)
	nombUsr=models.CharField(max_length=75, verbose_name='Nombre Usuario')
	cedula=models.CharField(max_length=11, verbose_name='Cédula Usuario')
	correo=models.CharField(max_length=75, verbose_name='Correo Usuario')
	clave=models.CharField(max_length=75, verbose_name='Contraseña')

	idTipoUsr=models.ForeignKey(tipoUsr, models.DO_NOTHING, db_column='idTipoUsr')
	idDependencia=models.ForeignKey(dependencia, models.DO_NOTHING, db_column='idDependencia')

	class Meta:
		db_table='usuarios'

	def __str__(self):
		return u'%s' %self.nombUsr			

class Pregunta(models.Model):
	idPregunta=models.AutoField(primary_key=True)
	pregunta=models.CharField(max_length=250, verbose_name='Pregunta')
	ayuda=models.CharField(max_length=100, verbose_name='Ayuda para la Pregunta')

	idTipoCuest=models.ForeignKey(tipoCuest, models.DO_NOTHING, db_column='idTipoCuest')
	idSubtema=models.ForeignKey(subtema, models.DO_NOTHING, db_column='idSubtema')

	class Meta:
		db_table='pregunta'

	def __str__(self):
		return u'%s' %self.pregunta	

class Recomendacion(models.Model):
	idRecomendacion=models.AutoField(primary_key=True)
	recomendacion=models.CharField(max_length=75, verbose_name='Recomendación valor respuesta')
	valor=models.IntegerField()

	idPregunta=models.ForeignKey(pregunta, models.DO_NOTHING, db_column='idPregunta')

	class Meta:
		db_table='recomendacion'

	def __str__(self):
		return u'%s' %self.recomendacion

class Respuesta(models.Model):
	idRespuesta=models.AutoField(primary_key=True)
	respuesta=models.CharField(max_length=75, verbose_name='Respuesta pregunta')
	valorRta=models.IntegerField()

	idPregunta=models.ForeignKey(pregunta, models.DO_NOTHING, db_column='idPregunta')

	class Meta:
		db_table='respuesta'

	def __str__(self):
		return u'%s' %self.respuesta

class RtaUsr(models.Model):
	idRtaUser=models.AutoField(primary_key=True)
	rtaUser=models.CharField(max_length=75, verbose_name='Respuesta usuario')

	idPregunta=models.ForeignKey(pregunta, models.DO_NOTHING, db_column='idPregunta')
	idUsr=models.ForeignKey(usuario, models.DO_NOTHING, db_column='idUsr')

	class Meta:
		db_table='rtaUser'

	def __str__(self):
		return u'%s' %self.rtaUser

class Nivel(models.Model):
	idNivel=models.AutoField(primary_key=True)
	nomNivel=models.CharField(max_length=75, verbose_name='Nivel')

	idSubtema=models.ForeignKey(subtema, models.DO_NOTHING, db_column='idSubtema')
	idDependencia=models.ForeignKey(dependencia, models.DO_NOTHING, db_column='idDependencia')

	class Meta:
		db_table='nivel'

	def __str__(self):
		return u'%s' %self.nombNivel