# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'FlatPageImage'
        db.create_table('flatpage_images_flatpageimage', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('flatpage', self.gf('django.db.models.fields.related.ForeignKey')(related_name='images', to=orm['flatpages.FlatPage'])),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('footnote', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal('flatpage_images', ['FlatPageImage'])

    def backwards(self, orm):
        # Deleting model 'FlatPageImage'
        db.delete_table('flatpage_images_flatpageimage')

    models = {
        'flatpage_images.flatpageimage': {
            'Meta': {'object_name': 'FlatPageImage'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'flatpage': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'images'", 'to': "orm['flatpages.FlatPage']"}),
            'footnote': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {})
        },
        'flatpages.flatpage': {
            'Meta': {'ordering': "('url',)", 'object_name': 'FlatPage', 'db_table': "'django_flatpage'"},
            'content': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'enable_comments': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'registration_required': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'sites': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['sites.Site']", 'symmetrical': 'False'}),
            'template_name': ('django.db.models.fields.CharField', [], {'max_length': '70', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_index': 'True'})
        },
        'sites.site': {
            'Meta': {'ordering': "('domain',)", 'object_name': 'Site', 'db_table': "'django_site'"},
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['flatpage_images']