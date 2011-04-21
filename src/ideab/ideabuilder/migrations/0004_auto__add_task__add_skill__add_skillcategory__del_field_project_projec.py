# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Task'
        db.create_table('ideabuilder_task', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('desc', self.gf('django.db.models.fields.TextField')()),
            ('project', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ideabuilder.Project'])),
        ))
        db.send_create_signal('ideabuilder', ['Task'])

        # Adding model 'Skill'
        db.create_table('ideabuilder_skill', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ideabuilder.SkillCategory'])),
        ))
        db.send_create_signal('ideabuilder', ['Skill'])

        # Adding model 'SkillCategory'
        db.create_table('ideabuilder_skillcategory', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=20)),
        ))
        db.send_create_signal('ideabuilder', ['SkillCategory'])

        # Deleting field 'Project.project_name'
        db.delete_column('ideabuilder_project', 'project_name')

        # Deleting field 'Project.project_owner'
        db.delete_column('ideabuilder_project', 'project_owner_id')

        # Deleting field 'Project.project_desc'
        db.delete_column('ideabuilder_project', 'project_desc')

        # Adding field 'Project.name'
        db.add_column('ideabuilder_project', 'name', self.gf('django.db.models.fields.CharField')(default='', max_length=20), keep_default=False)

        # Adding field 'Project.desc'
        db.add_column('ideabuilder_project', 'desc', self.gf('django.db.models.fields.TextField')(default=''), keep_default=False)

        # Adding field 'Project.owner'
        db.add_column('ideabuilder_project', 'owner', self.gf('django.db.models.fields.related.ForeignKey')(default=1, related_name='only_owner', to=orm['auth.User']), keep_default=False)

        # Removing M2M table for field project_builder on 'Project'
        db.delete_table('ideabuilder_project_project_builder')

        # Adding M2M table for field builder on 'Project'
        db.create_table('ideabuilder_project_builder', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('project', models.ForeignKey(orm['ideabuilder.project'], null=False)),
            ('user', models.ForeignKey(orm['auth.user'], null=False))
        ))
        db.create_unique('ideabuilder_project_builder', ['project_id', 'user_id'])

        # Deleting field 'Builder.builder_credit_no'
        db.delete_column('ideabuilder_builder', 'builder_credit_no')

        # Adding field 'Builder.credit_no'
        db.add_column('ideabuilder_builder', 'credit_no', self.gf('django.db.models.fields.IntegerField')(default=0), keep_default=False)

        # Adding M2M table for field task on 'Builder'
        db.create_table('ideabuilder_builder_task', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('builder', models.ForeignKey(orm['ideabuilder.builder'], null=False)),
            ('task', models.ForeignKey(orm['ideabuilder.task'], null=False))
        ))
        db.create_unique('ideabuilder_builder_task', ['builder_id', 'task_id'])


    def backwards(self, orm):
        
        # Deleting model 'Task'
        db.delete_table('ideabuilder_task')

        # Deleting model 'Skill'
        db.delete_table('ideabuilder_skill')

        # Deleting model 'SkillCategory'
        db.delete_table('ideabuilder_skillcategory')

        # Adding field 'Project.project_name'
        db.add_column('ideabuilder_project', 'project_name', self.gf('django.db.models.fields.CharField')(default='', max_length=20), keep_default=False)

        # Adding field 'Project.project_owner'
        db.add_column('ideabuilder_project', 'project_owner', self.gf('django.db.models.fields.related.ForeignKey')(default=1, related_name='only_owner', to=orm['auth.User']), keep_default=False)

        # Adding field 'Project.project_desc'
        db.add_column('ideabuilder_project', 'project_desc', self.gf('django.db.models.fields.TextField')(default=''), keep_default=False)

        # Deleting field 'Project.name'
        db.delete_column('ideabuilder_project', 'name')

        # Deleting field 'Project.desc'
        db.delete_column('ideabuilder_project', 'desc')

        # Deleting field 'Project.owner'
        db.delete_column('ideabuilder_project', 'owner_id')

        # Adding M2M table for field project_builder on 'Project'
        db.create_table('ideabuilder_project_project_builder', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('project', models.ForeignKey(orm['ideabuilder.project'], null=False)),
            ('user', models.ForeignKey(orm['auth.user'], null=False))
        ))
        db.create_unique('ideabuilder_project_project_builder', ['project_id', 'user_id'])

        # Removing M2M table for field builder on 'Project'
        db.delete_table('ideabuilder_project_builder')

        # Adding field 'Builder.builder_credit_no'
        db.add_column('ideabuilder_builder', 'builder_credit_no', self.gf('django.db.models.fields.IntegerField')(default=0), keep_default=False)

        # Deleting field 'Builder.credit_no'
        db.delete_column('ideabuilder_builder', 'credit_no')

        # Removing M2M table for field task on 'Builder'
        db.delete_table('ideabuilder_builder_task')


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
            'task': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['ideabuilder.Task']", 'symmetrical': 'False'}),
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
            'project': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['ideabuilder.Project']"})
        }
    }

    complete_apps = ['ideabuilder']
