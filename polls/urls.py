from django.urls import path, include
# from rest_framework_swagger.views import get_swagger_view
from rest_framework.routers import DefaultRouter
from rest_framework.schemas import get_schema_view
from rest_framework.documentation import include_docs_urls

from .apiviews import (
    PollViewSet, ChoiceList, CreateVote,
    UserCreate, LoginView
)

# schema_view = get_swagger_view(title='Polls API')

router = DefaultRouter()
router.register('polls', PollViewSet, base_name='polls')

urlpatterns = [
    # Default auth
    path(r'api-auth/', include('rest_framework.urls')),

    path('polls/<int:pk>/choices/', ChoiceList.as_view(), name='choice_list'),
    path('polls/<int:pk>/choices/<int:choice_pk>/vote/',
         CreateVote.as_view(), name='create_vote'
         ),
    path('users/', UserCreate.as_view(), name='user_create'),
    path('login/', LoginView.as_view(), name='login'),

    # Schema docs
    # path(r'swagger-docs/', schema_view),
    path('openapi/', get_schema_view(title='Polls',
                                     description='API for creating polls.'
                                     ), name='openapi-schema'),
    path('docs/', include_docs_urls(title='Polls API')),
]

urlpatterns += router.urls
