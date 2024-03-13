from django import forms
from django.forms import inlineformset_factory

from films.models import Film, FilmImage


class FilmForm(forms.ModelForm):
    class Meta:
        model = Film
        fields = ["name_uk",
                  "name_en",
                  "description_uk",
                  "description_en",
                  "image",
                  "trailer_url",
                  "is_3d",
                  "is_2d",
                  "is_imax",
                  "seo_url",
                  "seo_title",
                  "seo_keywords",
                  "seo_description"
                  ]
        widgets = {
            "name_uk": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter film name in Ukrainian",
                "aria-label": "film-name-uk-label",
                "aria-describedby": "fime-name-uk-span"
            }),
            "name_en": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter film name in English",
                "aria-label": "film-name-en-label",
                "aria-describedby": "fime-name-en-span"
            }),
            "description_uk": forms.Textarea(attrs={
                "class": "form-control",
                "aria-label": "film-description-uk-label",
                "aria-describedby": "film-description-uk-span",
                "placeholder": "Enter description in Ukrainian"
            }),
            "description_en": forms.Textarea(attrs={
                "class": "form-control",
                "aria-label": "film-description-en-label",
                "aria-describedby": "film-description-en-span",
                "placeholder": "Enter description in English"
            }),
            "image": forms.FileInput(attrs={"class": "form-control custom-file-input", "type": "file"}),
            "trailer_url": forms.URLInput(attrs={
                "class": "form-control",
                "placeholder": "Enter trailer URL",
                "aria-label": "film-trailer-label",
                "aria-describedby": "film-image-span"
            }),
            "is_3d": forms.CheckboxInput(attrs={
                "class": "form-control form-check-input"
            }),
            "is_2d": forms.CheckboxInput(attrs={
                "class": "form-control form-check-input"
            }),
            "is_imax": forms.CheckboxInput(attrs={
                "class": "form-control form-check-input"
            }),
            "seo_url": forms.URLInput(attrs={
                "class": "form-control",
                "placeholder": "Enter SEO URL",
                "aria-label": "film-seo-url-label",
                "aria-describedby": "film-seo-url-span"
            }),
            "seo_title": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter SEO title",
                "aria-label": "film-seo-title-label",
                "aria-describedby": "film-seo-title-span"
            }),
            "seo_keywords": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter SEO keywords",
                "aria-label": "film-seo-keywords-label",
                "aria-describedby": "film-seo-keywords-span"
            }),
            "seo_description": forms.Textarea(attrs={
                "class": "form-control",
                "aria-label": "film-seo-description-label",
                "aria-describedby": "film-seo-description-span",
                "placeholder": "Enter SEO description",
                "rows": 2,
            }),
        }


class FilmImageForm(forms.ModelForm):
    class Meta:
        model = FilmImage
        fields = ["image"]
        widgets = {
            "image": forms.FileInput(attrs={"class": "form-control custom-file-input", "type": "file"}),
        }


FilmImageFormSet = inlineformset_factory(
    parent_model=Film,
    model=FilmImage,
    form=FilmImageForm,
    can_delete=True,
    can_delete_extra=True,
    extra=1)
