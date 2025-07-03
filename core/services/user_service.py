from core.models import Company, CustomUser, UserRole
from core.models.role import Role
from django.contrib.auth.models import Group


def register_new_user(company_name, email, password, **kwargs):
    company = Company.objects.create(name=company_name)
    username = email
    user = CustomUser.objects.create_user(username, email, password, **kwargs)
    user_role = UserRole()
    user_role.company = company
    user_role.user = user
    user_role.role = Role.COMPANY_ADMIN
    user_role.save()

    company_admin_group = Group.objects.get(name=Role.COMPANY_ADMIN)
    user.groups.add(company_admin_group)

    return user