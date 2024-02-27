from django.forms import ModelForm, Select, CheckboxInput, URLInput, Textarea, RadioSelect, FileInput
from banners.models import TopBanner, AdvertisementBanner, BannerSettings


class TopBannerForm(ModelForm):
    class Meta:
        model = TopBanner
        fields = ["image", "url", "description"]
        widgets = {
            "image": FileInput(attrs={"class": "form-control custom-file-input", "type": "file"}),
            "url": URLInput(attrs={"class": "form-control custom",
                                   "aria-label": "Enter URL",
                                   "placeholder": "Enter URL"}),
            "description": Textarea(attrs={"class": "form-control",
                                           "aria-label": "Enter description",
                                           "placeholder": "Enter description",
                                           "rows": 3})
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


class BannerSettingsForm(ModelForm):
    class Meta:
        model = BannerSettings
        fields = ["background_image", "is_background_image"]
        widgets = {
            "is_background_image": RadioSelect(choices=[(True, 'Image on background'),
                                                        (False, 'Just background')],
                                               attrs={}),
            "background_image": FileInput(attrs={"class": "form-control custom-file-input", "type": "file"})
        }


class AdvertisementBannerForm(ModelForm):
    class Meta:
        model = AdvertisementBanner
        fields = ["image", "url"]
        widgets = {
            "image": FileInput(attrs={"class": "form-control custom-file-input", "type": "file"}),
            "url": URLInput(attrs={"class": "form-control custom",
                                   "aria-label": "Enter URL",
                                   "placeholder": "Enter URL"}),
        }


class AdvertisementBannerSettingsForm(ModelForm):
    class Meta:
        model = BannerSettings
        fields = ["advertisement_rotation", "are_advertisements_active"]
        widgets = {
            'advertisement_rotation': Select(choices=((num, str(num)) for num in range(1, 11)),
                                             attrs={'class': 'form-control custom-select w-auto', }),
            'are_advertisements_active': CheckboxInput(attrs={'class': 'form-control custom-control-input'})
        }
