# Generated by Django 2.2.2 on 2020-02-27 04:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Interface',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('interface_name', models.CharField(db_index=True, help_text='请输入接口名称', max_length=32, verbose_name='接口名称')),
                ('interface_url', models.CharField(help_text='请输入接口地址', max_length=255, verbose_name='接口地址')),
                ('request_mode', models.CharField(choices=[('GET', 'GET'), ('POST', 'POST'), ('PUT', 'PUT'), ('DELETE', 'DELETE'), ('PATCH', 'PATCH')], default='GET', help_text='请选择请求方式', max_length=11, verbose_name='请求方式')),
                ('create_time', models.DateTimeField(auto_now_add=True, null=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, null=True, verbose_name='修改时间')),
            ],
            options={
                'verbose_name': '接口列表',
                'verbose_name_plural': '接口列表',
                'db_table': 'interface',
            },
        ),
        migrations.CreateModel(
            name='Scene',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('scene_name', models.CharField(db_index=True, help_text='请输入场景名称', max_length=32, verbose_name='场景名称')),
                ('request_head', models.TextField(blank=True, default='', help_text='请输入字典格式的请求头', null=True, verbose_name='请求头')),
                ('request_parameter', models.TextField(blank=True, default='', help_text='请输入字典格式的请求参数', null=True, verbose_name='请求参数')),
                ('body_type', models.CharField(blank=True, choices=[('x-www-form-urlencoded', 'application/x-www-form-urlencoded'), ('json', 'application/json'), ('form-data', 'multipart/form-data'), ('xml', 'text/xml')], default='x-www-form-urlencoded', help_text='请选择请求体类型', max_length=21, null=True, verbose_name='请求体类型')),
                ('request_body', models.TextField(blank=True, default='', help_text='请输入浏览器原生表单、json、文件或xml格式的请求体', null=True, verbose_name='请求体')),
                ('response_result', models.TextField(blank=True, default='', help_text='请输入字典格式的响应结果', null=True, verbose_name='响应结果')),
                ('create_time', models.DateTimeField(auto_now_add=True, null=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, null=True, verbose_name='修改时间')),
                ('scene_group', models.ForeignKey(help_text='请选择接口', on_delete=django.db.models.deletion.CASCADE, related_name='interfaces', to='imitate.Interface', verbose_name='接口')),
            ],
            options={
                'verbose_name': '场景列表',
                'verbose_name_plural': '场景列表',
                'db_table': 'scene',
            },
        ),
    ]