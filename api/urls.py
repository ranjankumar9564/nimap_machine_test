
from django.urls import path
from .views import ClientListCreateView, ClientDetailView, ProjectCreateForClientView, ProjectListForUserView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    # auth
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # clients
    path('clients/', ClientListCreateView.as_view(), name='client-list'),
    path('clients/<int:pk>/', ClientDetailView.as_view(), name='client-detail'),
    path('clients/<int:client_id>/projects/', ProjectCreateForClientView.as_view(), name='client-project-create'),

    # projects for logged-in user
    path('projects/', ProjectListForUserView.as_view(), name='projects-for-user'),
]
