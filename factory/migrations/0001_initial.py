<<<<<<< HEAD
# Generated by Django 4.2 on 2023-04-09 09:50

from django.db import migrations, models
import django.db.models.deletion
=======
<<<<<<< HEAD
# Generated by Django 4.2 on 2023-04-07 05:57

from django.db import migrations, models
=======
# Generated by Django 4.2 on 2023-04-09 16:32

from django.db import migrations, models
import django.db.models.deletion
>>>>>>> 97a64e0eaa101fe2d480f46c36a1383a2a9a7096
>>>>>>> master


class Migration(migrations.Migration):

    initial = True

    dependencies = [
<<<<<<< HEAD
        ('employees', '0001_initial'),
        ('client', '0001_initial'),
=======
<<<<<<< HEAD
=======
        ('client', '0001_initial'),
        ('employees', '0001_initial'),
>>>>>>> 97a64e0eaa101fe2d480f46c36a1383a2a9a7096
>>>>>>> master
    ]

    operations = [
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Запись создана')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Запись обновлена')),
                ('start_date', models.DateTimeField(verbose_name='Цена действительна с')),
                ('end_date', models.DateTimeField(verbose_name='Цена действительна до')),
                ('is_actual', models.BooleanField(default=True, verbose_name='Актуально?')),
<<<<<<< HEAD
                ('value', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='Стоимость')),
=======
<<<<<<< HEAD
                ('value', models.PositiveIntegerField(verbose_name='Стоимость')),
>>>>>>> master
            ],
            options={
                'verbose_name': 'Цены',
                'ordering': ['updated_at'],
            },
        ),
<<<<<<< HEAD
=======
    ]
=======
                ('value', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='Стоимость')),
            ],
            options={
                'verbose_name': 'Стоимость пошива',
                'ordering': ['updated_at'],
            },
        ),
>>>>>>> master
        migrations.CreateModel(
            name='RawStuff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True, verbose_name='Наименование')),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Продукт из склада',
                'verbose_name_plural': 'Продукт из склада',
            },
        ),
        migrations.CreateModel(
            name='SewingModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client', models.CharField(max_length=50, verbose_name='Клиент')),
                ('color', models.CharField(max_length=50, verbose_name='Цвет')),
                ('material', models.CharField(blank=True, max_length=50, null=True, verbose_name='Материал')),
                ('type', models.CharField(max_length=50, verbose_name='Тип модели')),
                ('price_for_one', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена за штуку')),
            ],
            options={
                'verbose_name': 'Модель',
                'verbose_name_plural': 'Модель',
            },
        ),
        migrations.CreateModel(
            name='Storage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(blank=True, max_length=50, null=True, verbose_name='Код')),
                ('color', models.CharField(blank=True, max_length=50, null=True, verbose_name='Цвет')),
                ('quantity', models.IntegerField(default=0, null=True, verbose_name='Количество')),
                ('total_price', models.DecimalField(decimal_places=2, default=0, max_digits=10, null=True, verbose_name='Сумма')),
                ('data_purchase', models.DateField(verbose_name='Дата закупки')),
                ('is_ready', models.BooleanField(default=True, verbose_name='Готово')),
                ('remainder', models.CharField(blank=True, max_length=10, null=True, verbose_name='Остаток')),
                ('defect', models.IntegerField(blank=True, default=0, null=True, verbose_name='Брак')),
                ('created_at', models.DateTimeField(verbose_name='')),
                ('where_was_purchase', models.TextField(blank=True, max_length=100, null=True, verbose_name='Поставщик')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='factory.rawstuff', verbose_name='Сырье')),
            ],
            options={
                'verbose_name': 'Склад-Сырье',
                'verbose_name_plural': 'Склад-Сырье',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_poluchenia', models.DateField(auto_now_add=True, verbose_name='Дата Получения')),
                ('quantity_zayav', models.IntegerField(default=0, verbose_name='Количество Заявленное')),
                ('quantity_fact', models.IntegerField(default=0, verbose_name='Количество Фактически выполненного')),
                ('data_zakup', models.DateField(auto_now=True, null=True, verbose_name='Дата закупа')),
                ('raskroi_tkani', models.DateField(blank=True, null=True, verbose_name='Дата когда раскроили')),
                ('pod_flizelin', models.DateField(blank=True, null=True, verbose_name='Дата подклейки флизелина')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='client.client', verbose_name='Клиент')),
                ('name_order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='factory.sewingmodel', verbose_name='Модель')),
            ],
            options={
                'verbose_name': 'Заказ',
                'verbose_name_plural': 'Заказы',
            },
        ),
        migrations.CreateModel(
            name='NewOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
<<<<<<< HEAD
                ('price', models.PositiveIntegerField()),
                ('color', models.CharField(max_length=25)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
=======
                ('price', models.PositiveIntegerField(verbose_name='Стоимость')),
                ('color', models.CharField(max_length=25, verbose_name='Цвет')),
                ('image', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Изображение')),
>>>>>>> master
                ('received_date', models.DateField(verbose_name='Дата получения')),
                ('delivery_date', models.DateField(verbose_name='Дата отправки')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='client.client', verbose_name='Клиент')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='factory.sewingmodel', verbose_name='Модель')),
            ],
<<<<<<< HEAD
=======
            options={
                'verbose_name': 'Образец',
                'verbose_name_plural': 'Образцы',
            },
>>>>>>> master
        ),
        migrations.CreateModel(
            name='FabricCutting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity_model_total', models.IntegerField(default=0, null=True)),
                ('data_start_day', models.DateField(verbose_name='Дата начала')),
                ('data_start_end', models.DateField(verbose_name='Дата окончания')),
                ('material', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='factory.storage')),
                ('model_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='factory.sewingmodel')),
            ],
            options={
                'verbose_name': 'Раскрой ткани',
                'verbose_name_plural': 'Раскрой ткани',
            },
        ),
        migrations.CreateModel(
            name='DailyWork',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
<<<<<<< HEAD
=======
                ('payment_per_day', models.IntegerField(default=0, verbose_name='Зарплата за день')),
>>>>>>> master
                ('quantity', models.PositiveIntegerField(verbose_name='Количество')),
                ('date', models.DateField(auto_now_add=True, verbose_name='Дата')),
                ('prepayment', models.IntegerField(default=0, verbose_name='Аванс')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employees.employee', verbose_name='Cотрудник')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='factory.sewingmodel', verbose_name='Модель')),
            ],
            options={
                'verbose_name': 'Ежедневник',
                'verbose_name_plural': 'Ежедневники',
            },
        ),
    ]
<<<<<<< HEAD
=======
>>>>>>> 97a64e0eaa101fe2d480f46c36a1383a2a9a7096
>>>>>>> master
