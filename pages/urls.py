from django.urls import path
from . import views

urlpatterns = [
    path('static_example/', views.static_example),

    path('artii/', views.artii),    # 워드아트? http://artii.herokuapp.com/
    path('artiiResult/', views.artiiResult),

    path('throw/', views.throw),  # 사용자가 input으로 보내는 곳
    path('catch/', views.catch),  # 받을 곳

    path('isitbirthday/', views.isitbirthday),
    path('template_language/', views.template_language),
    path('introduce/<str:name>/<int:age>/', views.introduce),
    path('greeting/<str:name>/', views.greeting),  # django 에서 url 입력시 끝에 /로 끝나야 한다.
    path('greeting/IU/', views.greetingIU),  # django 에서 url 입력시 끝에 /로 끝나야 한다.
    path('dinner/', views.dinner),
    path('index/', views.index),  # index 란 곳으로 들어오면 views 의 index 를 실행하겠다 선언
]