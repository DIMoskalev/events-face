from django.utils.decorators import method_decorator
from drf_yasg.utils import swagger_auto_schema
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet

from .models import User
from .serializers import UserSerializer


@method_decorator(
    name="create",
    decorator=swagger_auto_schema(operation_description="Создание пользователя"),
)
@method_decorator(
    name="list",
    decorator=swagger_auto_schema(operation_description="Список пользователей"),
)
@method_decorator(
    name="retrieve",
    decorator=swagger_auto_schema(
        operation_description="Подробная информация о пользователе"
    ),
)
@method_decorator(
    name="update",
    decorator=swagger_auto_schema(
        operation_description="Изменение информации о пользователе"
    ),
)
@method_decorator(
    name="destroy",
    decorator=swagger_auto_schema(operation_description="Удаление пользователя"),
)
class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)

    def perform_create(self, serializer):
        user = serializer.save(is_active=True)
        user.set_password(user.password)
        user.save()
