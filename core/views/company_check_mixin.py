from rest_framework.viewsets import GenericViewSet
from rest_framework.exceptions import NotAuthenticated, NotFound

from core.models import CustomUser, UserRole


class CompanyCheckMixin:

    def initial(self, request, *args, **kwargs):
        if not request.user or not request.user.is_authenticated:
            raise NotAuthenticated

        company_pk = kwargs.get('company_pk')

        if company_pk is None:
            raise NotFound

        try:
            user = CustomUser.objects.get(id=request.user.id)
            self.company = UserRole.objects.get(user__id=user.id, company__id=company_pk)
        except (CustomUser.DoesNotExist, UserRole.DoesNotExist):
            raise NotFound

        super().initial(request, *args, **kwargs)