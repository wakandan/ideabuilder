# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Project'
        db.create_table('ideabuilder_project', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('desc', self.gf('django.db.models.fields.TextField')()),
            ('owner', self.gf('django.db.models.fields.related.ForeignKey')(related_name='only_owner', to=orm['auth.User'])),
        ))
        db.send_create_signal('ideabuilder', ['Project'])

        # Adding M2M table for field builder on 'Project'
        db.create_table('ideabuilder_project_builder', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('project', models.ForeignKey(orm['ideabuilder.project'], null=False)),
            ('user', models.ForeignKey(orm['auth.user'], null=False))
        ))
        db.create_unique('ideabuilder_project_builder', ['project_id', 'user_id'])

        # Adding model 'Builder'
        db.create_table('ideabuilder_builder', (
            ('user_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True, primary_key=True)),
            ('credit_no', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal('ideabuilder', ['Builder'])

        # Adding model 'Task'
        db.create_table('ideabuilder_task', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('desc', self.gf('django.db.models.fields.TextField')()),
            ('project', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ideabuilder.Project'])),
        ))
        db.send_create_signal('ideabuilder', ['Task'])

        # Adding M2M table for field task on 'Task'
        db.create_table('ideabuilder_task_task', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('task', models.ForeignKey(orm['ideabuilder.task'], null=False)),
            ('builder', models.ForeignKey(orm['ideabuilder.builder'], null=False))
        ))
        db.create_unique('ideabuilder_task_task', ['task_id', 'builder_id'])

        # Adding model 'SkillCategory'
        db.create_table('ideabuilder_skillcategory', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=20)),
        ))
        db.send_create_signal('ideabuilder', ['SkillCategory'])

        # Adding model 'Skill'
        db.create_table('ideabuilder_skill', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ideabuilder.SkillCategory'])),
        ))
        db.send_create_signal('ideabuilder', ['Skill'])


    def backwards(self, orm):
        
        # Deleting model 'Project'
        db.delete_table('ideabuilder_project')

        # Removing M2M table for field builder on 'Project'
        db.delete_table('ideabuilder_project_builder')

        # Deleting model 'Builder'
        db.delete_table('ideabuilder_builder')

        # Deleting model 'Task'
        db.delete_table('ideabuilder_task')

        # Removing M2M table for field task on 'Task'
        db.delete_table('ideabuilder_task_task')

        # Deleting model 'SkillCategory'
        db.delete_table('ideabuilder_skillcategory')

        # Deleting model 'Skill'
        db.delete_table('ideabuilder_skill')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'ideabuilder.builder': {
            'Meta': {'object_name': 'Builder', '_ormbases': ['auth.User']},
            'credit_no': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'user_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True', 'primary_key': 'True'})
        },
        'ideabuilder.project': {
            'Meta': {'object_name': 'Project'},
            'builder': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'builders'", 'symmetrical': 'False', 'to': "orm['auth.User']"}),
            'desc': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'only_owner'", 'to': "orm['auth.User']"})
        },
        'ideabuilder.skill': {
            'Meta': {'object_name': 'Skill'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['ideabuilder.SkillCategory']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        'ideabuilder.skillcategory': {
            'Meta': {'object_name': 'SkillCategory'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        'ideabuilder.task': {
            'Meta': {'object_name': 'Task'},
            'desc': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['ideabuilder.Project']"}),
            'task': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['ideabuilder.Builder']", 'symmetrical': 'False'})
        }
    }

    complete_apps = ['ideabuilder']
