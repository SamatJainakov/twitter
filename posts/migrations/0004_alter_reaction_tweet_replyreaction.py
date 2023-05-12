# Generated by Django 4.2 on 2023-05-10 14:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
        ('posts', '0003_rename_reaction_reaction_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reaction',
            name='tweet',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reactions', to='posts.tweet'),
        ),
        migrations.CreateModel(
            name='ReplyReaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.profile')),
                ('reply', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reply_reactions', to='posts.reply')),
                ('type', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='posts.reactiontype')),
            ],
            options={
                'unique_together': {('reply', 'profile')},
            },
        ),
    ]
