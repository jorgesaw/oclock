"""custom delete views."""

# Django
from django.http import HttpResponseRedirect


class SoftDeleteViewMixin:
    """Soft delete view mixin.
    
    Set status model at inactive.
    """

    
    def delete(self, request, *args, **kwars):
        self.object = self.get_object()
        success_url = self.get_success_url()
        self.object.soft_delete()
        return HttpResponseRedirect(success_url)
