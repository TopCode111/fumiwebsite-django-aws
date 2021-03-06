# Generated by Django 3.2.3 on 2021-05-30 04:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='お名前')),
                ('email', models.EmailField(max_length=254, verbose_name='メールアドレス')),
                ('phone', models.CharField(max_length=20, verbose_name='電話番号')),
                ('topics', models.CharField(choices=[('ご家族のお悩み', 'ご家族のお悩み'), ('お金のお悩み', 'お金のお悩み'), ('お仕事のお悩み', 'お仕事のお悩み'), ('日常生活のお悩み', '日常生活のお悩み')], max_length=300, verbose_name='お問い合わせ内容')),
                ('message', models.TextField(verbose_name='詳細をお書きください')),
            ],
        ),
    ]
