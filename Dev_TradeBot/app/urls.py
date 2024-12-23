from django.urls import path, include
from .views import MasterListCreateView, MasterRetriveUpdateDistroyView, MasterListView#, testview, ChildListCreate
from rest_framework.routers import DefaultRouter

# router = DefaultRouter()
# router.register(r'masters_list', MasterListView, basename='master_list')
# router.register(r'testview', testview, basename='testview')

urlpatterns = [
    # path('master/',MasterListCreateView.as_view()),
    # path('master/<pk>',MasterRetriveUpdateDistroyView.as_view()),
    # path('test', testview.as_view({'get': 'list', 'post': 'create_user'})),
    path('master', MasterListView.as_view({'post': 'create'}), name='create Master'),
    path('masters/', MasterListView.as_view({'get':'list'}), name='list master'),
    # path('child', ChildListCreate.as_view({'post': 'create'}), name='create Child'),
    # path('childs/', ChildListCreate.as_view({'get': 'list'}), name='list Child')



    # path('detail/<int:pk>/', views.post_detail, name='post_detail'),
    # path('update/<int:pk>/', views.post_update, name='post_update'),
    # path('delete/<int:pk>/', views.post_delete, name='post_delete'),
]