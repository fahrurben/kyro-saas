from rest_framework import permissions

class CompanyOwnPermission:

    def has_permission(self, request, view):
        """ Always has permission, permission check in the query filter by company id"""

        return True

    def has_object_permission(self, request, view, obj):
        """ Check if model is allow to access by user """

        user_roles = request.user.roles.all()
        company_ids = [user_role.company.id for user_role in user_roles]
        return obj.company.id in company_ids