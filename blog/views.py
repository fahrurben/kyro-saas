from rest_framework import viewsets
from rest_framework.permissions import DjangoModelPermissions

from blog.models import Post
from blog.serializers import PostSerializer
from core.permissions.company_own_permission import CompanyOwnPermission
from core.views.company_check_mixin import CompanyCheckMixin


class PostView(CompanyCheckMixin, viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    permission_classes = [DjangoModelPermissions, CompanyOwnPermission]

    def get_queryset(self):
        company_pk = self.kwargs.get('company_pk')
        return Post.objects.filter(company__id=company_pk)

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update({'user': self.request.user, 'company_pk': self.kwargs.get('company_pk')})
        return context