from rest_framework.views import APIView, Request, Response, status
from .serializers import UserSerializer, LoginSerializer
from .models import Users
from rest_framework_simplejwt.views import TokenObtainPairView


class LoginView(TokenObtainPairView):
    ...


class RegisterView(APIView):
    def get(self, request: Request) -> Response:
        users = Users.objects.all()

        serializer = UserSerializer(users, many=True)

        return Response(serializer.data)

    def post(self, request: Request) -> Response:
        serializer = UserSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status.HTTP_201_CREATED)
