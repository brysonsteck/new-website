from django.db import models
from markdownfield.models import MarkdownField, RenderedMarkdownField
from markdownfield.validators import VALIDATOR_STANDARD

# Create your models here.
class Project(models.Model):
  title = models.CharField(max_length=200)
  current = models.BooleanField(default=True)
  overview = models.TextField()
  description = MarkdownField(rendered_field='text_rendered',use_editor=False, use_admin_editor=True, validator=VALIDATOR_STANDARD)
  text_rendered = RenderedMarkdownField()
  image = models.ImageField(upload_to='projects/static/projects/images/')