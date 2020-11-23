# Generated by Django 2.2.16 on 2020-10-05 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Administrador',
            fields=[
                ('id_admin', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('paterno', models.CharField(max_length=50)),
                ('materno', models.CharField(blank=True, max_length=50, null=True)),
                ('contrasena', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'administrador',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Asesoria',
            fields=[
                ('id_asesoria', models.AutoField(primary_key=True, serialize=False)),
                ('fecha', models.DateField()),
                ('tipo_asesoria', models.CharField(max_length=50)),
                ('nro_asesoria', models.IntegerField()),
                ('DESCRIPCION_ASESORIA', models.CharField(max_length=500)),
            ],
            options={
                'db_table': 'asesoria',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=150, null=True, unique=True)),
            ],
            options={
                'db_table': 'auth_group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('codename', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'auth_permission',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(blank=True, max_length=128, null=True)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.BooleanField()),
                ('username', models.CharField(blank=True, max_length=150, null=True, unique=True)),
                ('first_name', models.CharField(blank=True, max_length=150, null=True)),
                ('last_name', models.CharField(blank=True, max_length=150, null=True)),
                ('email', models.CharField(blank=True, max_length=254, null=True)),
                ('is_staff', models.BooleanField()),
                ('is_active', models.BooleanField()),
                ('date_joined', models.DateTimeField()),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserGroups',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_user_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_user_user_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Capacitacion',
            fields=[
                ('nro_capacitacion', models.AutoField(primary_key=True, serialize=False)),
                ('fecha', models.DateField()),
                ('asistentes', models.BinaryField()),
                ('descripcion_capa', models.CharField(max_length=500)),
            ],
            options={
                'db_table': 'capacitacion',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Checklist',
            fields=[
                ('nro_checklist', models.AutoField(primary_key=True, serialize=False)),
                ('act_mejora', models.CharField(max_length=50)),
                ('descripcion_check', models.CharField(max_length=500)),
            ],
            options={
                'db_table': 'checklist',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id_cliente', models.AutoField(primary_key=True, serialize=False)),
                ('direccion', models.CharField(max_length=50)),
                ('nombre', models.CharField(max_length=50)),
                ('rubro', models.CharField(max_length=50)),
                ('correo', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'cliente',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Condicion',
            fields=[
                ('id_condicion', models.AutoField(primary_key=True, serialize=False)),
                ('nom_condicion', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'condicion',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ContratoServicio',
            fields=[
                ('id_servicio', models.AutoField(primary_key=True, serialize=False)),
                ('fecha_inicio', models.DateField()),
                ('fecha_termino', models.DateField()),
                ('estado', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'contrato_servicio',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DetChecklist',
            fields=[
                ('id_detchecklist', models.AutoField(primary_key=True, serialize=False)),
                ('estado', models.CharField(max_length=1)),
            ],
            options={
                'db_table': 'det_checklist',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_time', models.DateTimeField()),
                ('object_id', models.TextField(blank=True, null=True)),
                ('object_repr', models.CharField(blank=True, max_length=200, null=True)),
                ('action_flag', models.IntegerField()),
                ('change_message', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'django_admin_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_label', models.CharField(blank=True, max_length=100, null=True)),
                ('model', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'django_content_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app', models.CharField(blank=True, max_length=255, null=True)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('session_data', models.TextField(blank=True, null=True)),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_session',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Pago',
            fields=[
                ('id_pago', models.AutoField(primary_key=True, serialize=False)),
                ('pago', models.IntegerField()),
                ('fecha_pago', models.DateField(blank=True, null=True)),
                ('fecha_vencimiento', models.DateField()),
            ],
            options={
                'db_table': 'pago',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Profesional',
            fields=[
                ('rut', models.IntegerField(primary_key=True, serialize=False)),
                ('dv', models.CharField(max_length=1)),
                ('nombre', models.CharField(max_length=50)),
                ('paterno', models.CharField(max_length=50)),
                ('materno', models.CharField(blank=True, max_length=50, null=True)),
                ('contrasena', models.CharField(max_length=100)),
                ('estado', models.CharField(max_length=25)),
            ],
            options={
                'db_table': 'profesional',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SolicitudAsesoria',
            fields=[
                ('id_solicitud', models.AutoField(primary_key=True, serialize=False)),
                ('solicitud', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'solicitud_asesoria',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Visita',
            fields=[
                ('id_visita', models.AutoField(primary_key=True, serialize=False)),
                ('fecha', models.DateField()),
                ('materiales', models.CharField(max_length=500)),
                ('participantes', models.CharField(max_length=50)),
                ('descripcion', models.CharField(max_length=500)),
            ],
            options={
                'db_table': 'visita',
                'managed': False,
            },
        ),
    ]