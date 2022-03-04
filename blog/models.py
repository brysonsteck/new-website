from django.db import models
from django.utils import timezone
from markdownfield.models import MarkdownField, RenderedMarkdownField
from markdownfield.validators import VALIDATOR_STANDARD

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    text = MarkdownField(rendered_field='text_rendered',use_editor=False, use_admin_editor=True, validator=VALIDATOR_STANDARD)
    text_rendered = RenderedMarkdownField()
    posted = models.DateTimeField('date posted')
