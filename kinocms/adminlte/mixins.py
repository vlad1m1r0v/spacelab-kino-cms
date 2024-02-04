from django.contrib.auth.decorators import user_passes_test
from django.utils.decorators import method_decorator


class AdminPermissionMixin:
    @method_decorator(user_passes_test(lambda u: u.is_staff and u.is_superuser,
                                       login_url="/adminlte/login",
                                       redirect_field_name=None))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
