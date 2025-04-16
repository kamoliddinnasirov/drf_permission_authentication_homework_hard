from rest_framework import permissions

class IsCourseMemberOrAdmin(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.is_staff:
            return True
        if request.user.role == 'teacher':
            return obj.teacher == request.user
        if request.user.role == 'student':
            return request.user in obj.students.all()
        return False
