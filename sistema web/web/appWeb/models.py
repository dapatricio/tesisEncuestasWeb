from django.db import models

# Create your models here.

class Area(models.Model):
	id_area=models.AutoField(primary_key=True)
	nombArea=models.CharField(max_length=75, verbose_name='Nombre Areas')

	class Meta:
		db_table='area'

	def __str__(self):
		return u'%s' %self.nombArea

class Tema(models.Model):
	id_tema=models.AutoField(primary_key=True)
	nombTema=models.CharField(max_length=75, verbose_name='Nombre Area de Competencia')
	detalleTema=models.CharField(max_length=75, verbose_name='Detalle Tema')

	class Meta:
		db_table='tema'

	def __str__(self):
		return u'%s' %self.nombTema

class TipoCuest(models.Model):
	id_tipoCuest=models.AutoField(primary_key=True)
	nombCuest=models.CharField(max_length=75, verbose_name='Tipo de cuestionario')

	class Meta:
		db_table='tipoCuest'

	def __str__(self):
		return u'%s' %self.nombCuest	

class TipoDep(models.Model):
	id_tipoDep=models.AutoField(primary_key=True)
	nombTipoDep=models.CharField(max_length=75, verbose_name='Nombre Tipo de Dependencia')
	tipoDepartamento=models.IntegerField()

	class Meta:
		db_table='tipoDep'

	def __str__(self):
		return u'%s' %self.nombTipoDep	

class Dependencia(models.Model):
	id_dependencia=models.AutoField(primary_key=True)
	nombDependencia=models.CharField(max_length=75, verbose_name='Nombre Dependencia')

	id_tipoDep=models.ForeignKey(TipoDep, models.DO_NOTHING, db_column='id_tipoDep')
	id_area=models.ForeignKey(Area, models.DO_NOTHING, db_column='id_area')


	class Meta:
		db_table='dependencia'

	def __str__(self):
		return u'%s' %self.nombDependencia	

class Subtema(models.Model):
	id_subtema=models.AutoField(primary_key=True)
	nombSubtema=models.CharField(max_length=75, verbose_name='Nombre Competencia')
	detalleSubtema=models.CharField(max_length=75, verbose_name='Detalle Subtema')

	id_tema=models.ForeignKey(Tema, models.DO_NOTHING, db_column='id_tema')

	class Meta:
		db_table='subtema'

	def __str__(self):
		return u'%s' %self.nombSubtema	

class Usuarios(models.Model):
	idUsr=models.AutoField(primary_key=True)
	nombUsr=models.CharField(max_length=75, verbose_name='Nombre Usuario')
	cedula=models.CharField(max_length=11, verbose_name='Cédula Usuario')
	correo=models.CharField(max_length=75, verbose_name='Correo Usuario')
	clave=models.CharField(max_length=75, verbose_name='Contraseña')
	ESTUDIANTE='E'
	DOCENTE='D'
	ADMINISTRATIVO='A'
	USUARIOS_CHOICES=(
        (ESTUDIANTE, 'Estudiante'),
        (DOCENTE, 'Docente'),
        (ADMINISTRATIVO, 'Administrativo'),
    )
    tipo_usuario = models.CharField(
    	max_length=1,
    	choices=USUARIOS_CHOICES,
    	default=ESTUDIANTE,
    	)

	idDependencia=models.ForeignKey(Dependencia, models.DO_NOTHING, db_column='id_dependencia')

	class Meta:
		db_table='usuarios'

	def __str__(self):
		return u'%s' %self.nombUsr			

class Pregunta(models.Model):
	id_pregunta=models.AutoField(primary_key=True)
	pregunta=models.CharField(max_length=250, verbose_name='Pregunta')
	ayuda=models.CharField(max_length=100, verbose_name='Ayuda para la Pregunta')

	id_tipoCuest=models.ForeignKey(TipoCuest, models.DO_NOTHING, db_column='id_tipoCuest')
	id_subtema=models.ForeignKey(Subtema, models.DO_NOTHING, db_column='id_subtema')

	class Meta:
		db_table='pregunta'

	def __str__(self):
		return u'%s' %self.pregunta	

class Recomendacion(models.Model):
	id_recomendacion=models.AutoField(primary_key=True)
	recomendacion=models.CharField(max_length=75, verbose_name='Recomendación valor respuesta')
	valor=models.IntegerField()

	id_pregunta=models.ForeignKey(Pregunta, models.DO_NOTHING, db_column='id_pregunta')

	class Meta:
		db_table='recomendacion'

	def __str__(self):
		return u'%s' %self.recomendacion

class Respuesta(models.Model):
	id_respuesta=models.AutoField(primary_key=True)
	respuesta=models.CharField(max_length=75, verbose_name='Respuesta pregunta')
	valorRta=models.IntegerField()

	id_pregunta=models.ForeignKey(Pregunta, models.DO_NOTHING, db_column='id_pregunta')

	class Meta:
		db_table='respuesta'

	def __str__(self):
		return u'%s' %self.respuesta

class RtaUsr(models.Model):
	id_rtaUser=models.AutoField(primary_key=True)
	rtaUser=models.CharField(max_length=75, verbose_name='Respuesta usuario')

	id_pregunta=models.ForeignKey(Pregunta, models.DO_NOTHING, db_column='id_pregunta')
	id_usr=models.ForeignKey(Usuarios, models.DO_NOTHING, db_column='id_usr')

	class Meta:
		db_table='rtaUser'

	def __str__(self):
		return u'%s' %self.rtaUser

class Nivel(models.Model):
	id_nivel=models.AutoField(primary_key=True)
	nomNivel=models.CharField(max_length=75, verbose_name='Valor Nivel')

	id_subtema=models.ForeignKey(Subtema, models.DO_NOTHING, db_column='id_subtema')
	id_dependencia=models.ForeignKey(Dependencia, models.DO_NOTHING, db_column='id_dependencia')

	class Meta:
		db_table='nivel'

	def __str__(self):
		return u'%s' %self.nombNivel