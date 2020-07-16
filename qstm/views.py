from rest_framework.generics import (
    ListCreateAPIView, 
    RetrieveUpdateDestroyAPIView,
)

from .models import (
    # User,
    CustomUser,
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

from django_filters.rest_framework import DjangoFilterBackend

class UserListView(ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['username', 'password']

class UserDetailView(RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer


class ParentListView(ListCreateAPIView):
    queryset = Parent.objects.all()
    serializer_class = ParentSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['email', 'cellphone']

class ParentDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Parent.objects.all()
    serializer_class = ParentSerializer


class StudentListView(ListCreateAPIView):
    # queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['user_id']
    def get_queryset(self):
        """
        This view should return a list students
        for the currently authenticated parent_id.
        """
        user = self.request.user

        # Get a query based on the params
        # http://127.0.0.1:8000/api/v1/students/?parent_id=2
        parent_id = self.request.query_params.get('parent_id', None)
        if not parent_id :
            # this scenario is http://127.0.0.1:8000/api/v1/students/,
            # so will give all the students
            return Student.objects.all()
        else:
            return Student.objects.filter(parent_id=parent_id)
        

class StudentDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class TaskListView(ListCreateAPIView):
    serializer_class = TaskSerializer

    def get_queryset(self):
        """
        This view should return a list of student's tasks
        for the currently authenticated student_id.
        """
        # Get a query based on the params
        # http://127.0.0.1:8000/api/v1/tasks/?student_id=n
        student_id = self.request.query_params.get('student_id', None)
        if not student_id :
            # this scenario is http://127.0.0.1:8000/api/v1/tasks/,
            # so will give all the tasks in the DB.
            return Task.objects.all()
        else:
            return Task.objects.filter(student_id=student_id)



class TaskDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class SiteListView(ListCreateAPIView):    
    serializer_class = SiteSerializer
    def get_queryset(self):
        """
        This view should return a list of student's tasks
        for the currently authenticated student_id.
        """
        # Get a query based on the params
        # http://127.0.0.1:8000/api/v1/sites/?student_id=n
        student_id = self.request.query_params.get('student_id', None)
        if not student_id :
            # this scenario is http://127.0.0.1:8000/api/v1/sites/,
            # so will give all the tasks in the DB.
            return Site.objects.all()
        else:
            return Site.objects.filter(student_id=student_id)


class SiteDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Site.objects.all()
    serializer_class = SiteSerializer