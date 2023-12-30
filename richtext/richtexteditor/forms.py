from django import forms
from .models import RichTextModel
from ckeditor.widgets import CKEditorWidget

from .models import YourModel

class YourForm(forms.ModelForm):
    class Meta:
        model = YourModel
        fields = ['editor_content']

class RichTextModelForm(forms.ModelForm):
    class Meta:
        model = RichTextModel
        fields = ['title', 'content']
        widgets = {
            'content': CKEditorWidget(),
        }