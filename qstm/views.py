from rest_framework.generics import (
    ListCreateAPIView, 
    RetrieveUpdateDestroyAPIView,
)

from .models import (
    User,
    Parent,
    Student,
    Task,
    Site,
)

from .serializers import (
    UserSerializer,
    ParentSerializer,
    StudentSerializer,
    TaskSerializer,
    SiteSerializer,
)

class UserListView(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetailView(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ParentListView(ListCreateAPIView):
    queryset = Parent.objects.all()
    serializer_class = ParentSerializer

class ParentDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Parent.objects.all()
    serializer_class = ParentSerializer


class StudentListView(ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class TaskListView(ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TaskDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class SiteListView(ListCreateAPIView):
    queryset = Site.objects.all()
    serializer_class = SiteSerializer

class SiteDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Site.objects.all()
    serializer_class = SiteSerializer