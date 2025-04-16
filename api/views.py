from rest_framework import generics, permissions
from .models import Course
from .serializers import CourseSerializer
from .permissions import IsCourseMemberOrAdmin

class CourseListView(generics.ListCreateAPIView):
    serializer_class = CourseSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return Course.objects.all()
        elif user.role == 'teacher':
            return Course.objects.filter(teacher=user)
        elif user.role == 'student':
            return user.enrolled_courses.all()

    def perform_create(self, serializer):
        serializer.save(teacher=self.request.user)

class CourseDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsCourseMemberOrAdmin]
