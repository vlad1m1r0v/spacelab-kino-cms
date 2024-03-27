from django import forms
from cinemas.models import Cinema, CinemaImage


class CinemaForm(forms.ModelForm):
    class Meta:
        model = Cinema
        fields = [
            "name_uk",
            "name_en",
            "description_uk",
            "description_en",
            "features_uk",
            "features_en",
            "logo",
            "upper_banner",
            "seo_url",
            "seo_title",
            "seo_keywords",
            "seo_description",
        ]
        widgets = {
            "name_uk": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter cinema name in Ukrainian",
                "aria-label": "cinema-name-uk-label",
                "aria-describedby": "cinema-name-uk-span"
            }),
            "name_en": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter cinema name in English",
                "aria-label": "cinema-name-en-label",
                "aria-describedby": "cinema-name-en-span"
            }),
            "description_uk": forms.Textarea(attrs={
                "class": "form-control",
                "aria-label": "cinema-description-uk-label",
                "aria-describedby": "cinema-description-uk-span",
                "placeholder": "Enter description in Ukrainian"
            }),
            "description_en": forms.Textarea(attrs={
                "class": "form-control",
                "aria-label": "cinema-description-en-label",
                "aria-describedby": "cinema-description-en-span",
                "placeholder": "Enter description in English"
            }),
            "features_uk": forms.Textarea(attrs={
                "class": "form-control",
                "aria-label": "cinema-features-uk-label",
                "aria-describedby": "cinema-features-uk-span",
                "placeholder": "Enter features in Ukrainian"
            }),
            "features_en": forms.Textarea(attrs={
                "class": "form-control",
                "aria-label": "cinema-features-en-label",
                "aria-describedby": "cinema-features-en-span",
                "placeholder": "Enter features in English"
            }),
            "logo": forms.FileInput(attrs={"class": "form-control custom-file-input", "type": "file"}),
            "upper_banner": forms.FileInput(attrs={"class": "form-control custom-file-input", "type": "file"}),
            "seo_url": forms.URLInput(attrs={
                "class": "form-control",
                "placeholder": "Enter SEO URL",
                "aria-label": "cinema-seo-url-label",
                "aria-describedby": "cinema-seo-url-span"
            }),
            "seo_title": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter SEO title",
                "aria-label": "cinema-seo-title-label",
                "aria-describedby": "cinema-seo-title-span"
            }),
            "seo_keywords": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter SEO keywords",
                "aria-label": "cinema-seo-keywords-label",
                "aria-describedby": "cinema-seo-keywords-span"
            }),
            "seo_description": forms.Textarea(attrs={
                "class": "form-control",
                "aria-label": "cinema-seo-description-label",
                "aria-describedby": "cinema-seo-description-span",
                "placeholder": "Enter SEO description",
                "rows": 2,
            }),
        }


class CinemaImageForm(forms.ModelForm):
    class Meta:
        model = CinemaImage
        fields = ["image"]
        widgets = {
            "image": forms.FileInput(attrs={"class": "form-control custom-file-input", "type": "file"}),
        }


