# Generated by Django 2.0.6 on 2019-01-28 22:44

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('goods', '0008_auto_20190128_1415'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('province', models.CharField(default='', max_length=100, verbose_name='省份')),
                ('city', models.CharField(default='', max_length=100, verbose_name='城市')),
                ('district', models.CharField(default='', max_length=100, verbose_name='区域')),
                ('address', models.CharField(default='', max_length=100, verbose_name='详细地址')),
                ('signer_name', models.CharField(default='', max_length=100, verbose_name='签收人')),
                ('signer_mobile', models.CharField(default='', max_length=11, verbose_name='电话')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户')),
            ],
            options={
                'verbose_name': '收货地址',
                'verbose_name_plural': '收货地址',
            },
        ),
        migrations.CreateModel(
            name='UserCollect',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('goods', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goods.Goods', verbose_name='商品')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户')),
            ],
            options={
                'verbose_name': '用户收藏',
                'verbose_name_plural': '用户收藏',
            },
        ),
        migrations.CreateModel(
            name='UserMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message_type', models.CharField(choices=[(1, '留言'), (2, '投诉'), (3, '询问'), (4, '售后'), (5, '求购')], help_text='留言类型: 1(留言),2(投诉),3(询问),4(售后),5(求购)', max_length=20, verbose_name='留言类型')),
                ('subject', models.CharField(default='', max_length=200, verbose_name='主题')),
                ('file', models.FileField(help_text='上传文件', upload_to='message/images', verbose_name='上传文件')),
                ('add_time', models.DateField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户')),
            ],
            options={
                'verbose_name': '用户留言',
                'verbose_name_plural': '用户留言',
            },
        ),
        migrations.AlterUniqueTogether(
            name='usercollect',
            unique_together={('user', 'goods')},
        ),
    ]
