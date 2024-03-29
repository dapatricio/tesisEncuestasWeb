# Generated by Django 2.2.7 on 2019-12-10 17:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id_area', models.AutoField(primary_key=True, serialize=False)),
                ('nombArea', models.CharField(max_length=75, verbose_name='Nombre Areas')),
            ],
            options={
                'db_table': 'area',
            },
        ),
        migrations.CreateModel(
            name='Dependencia',
            fields=[
                ('id_dependencia', models.AutoField(primary_key=True, serialize=False)),
                ('nombDependencia', models.CharField(max_length=75, verbose_name='Nombre Dependencia')),
                ('id_area', models.ForeignKey(db_column='id_area', on_delete=django.db.models.deletion.DO_NOTHING, to='appWeb.Area')),
            ],
            options={
                'db_table': 'dependencia',
            },
        ),
        migrations.CreateModel(
            name='Pregunta',
            fields=[
                ('id_pregunta', models.AutoField(primary_key=True, serialize=False)),
                ('pregunta', models.CharField(max_length=250, verbose_name='Pregunta')),
                ('ayuda', models.CharField(max_length=100, verbose_name='Ayuda para la Pregunta')),
            ],
            options={
                'db_table': 'pregunta',
            },
        ),
        migrations.CreateModel(
            name='Tema',
            fields=[
                ('id_tema', models.AutoField(primary_key=True, serialize=False)),
                ('nombTema', models.CharField(max_length=75, verbose_name='Nombre Area de Competencia')),
                ('detalleTema', models.CharField(max_length=75, verbose_name='Detalle Tema')),
            ],
            options={
                'db_table': 'tema',
            },
        ),
        migrations.CreateModel(
            name='TipoCuest',
            fields=[
                ('id_tipoCuest', models.AutoField(primary_key=True, serialize=False)),
                ('nombCuest', models.CharField(max_length=75, verbose_name='Tipo de cuestionario')),
            ],
            options={
                'db_table': 'tipoCuest',
            },
        ),
        migrations.CreateModel(
            name='TipoDep',
            fields=[
                ('id_tipoDep', models.AutoField(primary_key=True, serialize=False)),
                ('nombTipoDep', models.CharField(max_length=75, verbose_name='Nombre Tipo de Dependencia')),
                ('tipoDepartamento', models.IntegerField()),
            ],
            options={
                'db_table': 'tipoDep',
            },
        ),
        migrations.CreateModel(
            name='TipoUsr',
            fields=[
                ('id_tipoUsr', models.AutoField(primary_key=True, serialize=False)),
                ('nombTipoUsr', models.CharField(max_length=75, verbose_name='Nombre Tipo de Usuario')),
                ('tipoUsr', models.IntegerField()),
            ],
            options={
                'db_table': 'tipoUsr',
            },
        ),
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('idUsr', models.AutoField(primary_key=True, serialize=False)),
                ('nombUsr', models.CharField(max_length=75, verbose_name='Nombre Usuario')),
                ('cedula', models.CharField(max_length=11, verbose_name='Cédula Usuario')),
                ('correo', models.CharField(max_length=75, verbose_name='Correo Usuario')),
                ('clave', models.CharField(max_length=75, verbose_name='Contraseña')),
                ('idDependencia', models.ForeignKey(db_column='id_dependencia', on_delete=django.db.models.deletion.DO_NOTHING, to='appWeb.Dependencia')),
                ('idTipoUsr', models.ForeignKey(db_column='id_tipoUsr', on_delete=django.db.models.deletion.DO_NOTHING, to='appWeb.TipoUsr')),
            ],
            options={
                'db_table': 'usuarios',
            },
        ),
        migrations.CreateModel(
            name='Subtema',
            fields=[
                ('id_subtema', models.AutoField(primary_key=True, serialize=False)),
                ('nombSubtema', models.CharField(max_length=75, verbose_name='Nombre Competencia')),
                ('detalleSubtema', models.CharField(max_length=75, verbose_name='Detalle Subtema')),
                ('id_tema', models.ForeignKey(db_column='id_tema', on_delete=django.db.models.deletion.DO_NOTHING, to='appWeb.Tema')),
            ],
            options={
                'db_table': 'subtema',
            },
        ),
        migrations.CreateModel(
            name='RtaUsr',
            fields=[
                ('id_rtaUser', models.AutoField(primary_key=True, serialize=False)),
                ('rtaUser', models.CharField(max_length=75, verbose_name='Respuesta usuario')),
                ('id_pregunta', models.ForeignKey(db_column='id_pregunta', on_delete=django.db.models.deletion.DO_NOTHING, to='appWeb.Pregunta')),
                ('id_usr', models.ForeignKey(db_column='id_usr', on_delete=django.db.models.deletion.DO_NOTHING, to='appWeb.Usuarios')),
            ],
            options={
                'db_table': 'rtaUser',
            },
        ),
        migrations.CreateModel(
            name='Respuesta',
            fields=[
                ('id_respuesta', models.AutoField(primary_key=True, serialize=False)),
                ('respuesta', models.CharField(max_length=75, verbose_name='Respuesta pregunta')),
                ('valorRta', models.IntegerField()),
                ('id_pregunta', models.ForeignKey(db_column='id_pregunta', on_delete=django.db.models.deletion.DO_NOTHING, to='appWeb.Pregunta')),
            ],
            options={
                'db_table': 'respuesta',
            },
        ),
        migrations.CreateModel(
            name='Recomendacion',
            fields=[
                ('id_recomendacion', models.AutoField(primary_key=True, serialize=False)),
                ('recomendacion', models.CharField(max_length=75, verbose_name='Recomendación valor respuesta')),
                ('valor', models.IntegerField()),
                ('id_pregunta', models.ForeignKey(db_column='id_pregunta', on_delete=django.db.models.deletion.DO_NOTHING, to='appWeb.Pregunta')),
            ],
            options={
                'db_table': 'recomendacion',
            },
        ),
        migrations.AddField(
            model_name='pregunta',
            name='id_subtema',
            field=models.ForeignKey(db_column='id_subtema', on_delete=django.db.models.deletion.DO_NOTHING, to='appWeb.Subtema'),
        ),
        migrations.AddField(
            model_name='pregunta',
            name='id_tipoCuest',
            field=models.ForeignKey(db_column='id_tipoCuest', on_delete=django.db.models.deletion.DO_NOTHING, to='appWeb.TipoCuest'),
        ),
        migrations.CreateModel(
            name='Nivel',
            fields=[
                ('id_nivel', models.AutoField(primary_key=True, serialize=False)),
                ('nomNivel', models.CharField(max_length=75, verbose_name='Nivel')),
                ('id_dependencia', models.ForeignKey(db_column='id_dependencia', on_delete=django.db.models.deletion.DO_NOTHING, to='appWeb.Dependencia')),
                ('id_subtema', models.ForeignKey(db_column='id_subtema', on_delete=django.db.models.deletion.DO_NOTHING, to='appWeb.Subtema')),
            ],
            options={
                'db_table': 'nivel',
            },
        ),
        migrations.AddField(
            model_name='dependencia',
            name='id_tipoDep',
            field=models.ForeignKey(db_column='id_tipoDep', on_delete=django.db.models.deletion.DO_NOTHING, to='appWeb.TipoDep'),
        ),
    ]
