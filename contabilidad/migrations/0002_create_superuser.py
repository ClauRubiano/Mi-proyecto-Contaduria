
from django.db import migrations
from django.contrib.auth.models import User

def create_superuser(apps, schema_editor):
    User.objects.create_superuser('admin', 'admin@ejemplo.com', 'admin123')

class Migration(migrations.Migration):
    dependencies = [('contabilidad', '0001_initial')]
    operations = [migrations.RunPython(create_superuser)]          
