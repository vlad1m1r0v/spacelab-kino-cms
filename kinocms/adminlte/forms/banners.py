from django.forms import ModelForm, Select, CheckboxInput, FileInput, URLInput, Textarea
from banners.models import TopBanner, BannerSettings


class TopBannerForm(ModelForm):
    class Meta:
        model = TopBanner
        fields = ["image", "url", "description"]
        widgets = {
            "image": FileInput(attrs={"class": "custom-file-input form-control", "type": "file"}),
            "url": URLInput(attrs={"class": "custom form-control",
                                   "aria-label": "Enter URL",
                                   "placeholder": "Enter URL"}),
            "description": Textarea(attrs={"class": "form-control",
                                           "rows": 3,
                                           "aria-label": "Enter description",
                                           "placeholder": "Enter description"})
        }

class TopBannerSettingsForm(ModelForm):
    class Meta:
        model = BannerSettings
        fields = ["banner_rotation", "are_banners_active"]
        widgets = {
            'banner_rotation': Select(choices=((num, str(num)) for num in range(1, 11)),
                                      attrs={'class': 'form-control custom-select w-auto', }),
            'are_banners_active': CheckboxInput(attrs={'class': 'form-control custom-control-input'})
        }
