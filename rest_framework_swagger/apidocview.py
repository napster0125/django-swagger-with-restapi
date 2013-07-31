from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from rest_framework_swagger import SWAGGER_SETTINGS

class APIDocView(APIView):

    def initial(self, request, *args, **kwargs):
        self.permission_classes = (self.get_permission_class(request),)
        protocol = "https" if request.is_secure() else "http"
        self.host = request.build_absolute_uri()
        self.api_path = '/api'
        self.api_full_uri = "%s://%s" % (protocol, request.get_host())

        return super(APIDocView, self).initial(request, *args, **kwargs)

    def get_permission_class(self, request):
        if SWAGGER_SETTINGS.get('is_superuser') and not request.user.is_superuser:
            return IsAdminUser
        if SWAGGER_SETTINGS.get('is_authenticated') and not request.user.is_authenticated():
            return IsAuthenticated

        return AllowAny


