# Style 적용하기 

<br />
<br />
<br />

## [1] 구조 만들기

- urls.py에 패스 추가하기

  ```
  from django.contrib import admin
  from django.urls import path
  from pages import views
  
  urlpatterns = [
      path('static_example/', views.views.static_example),
  ]
  ```

- views.py에 함수 정의하기
  ```
  def static_example(request):
      return render(request, 'static_example.html')
  ```

- pages - static 폴더 안에 static_example.html 파일 생성 후 코드 작성
  ```
  <!DOCTYPE html>
  <html lang="en">
  <head>
      <meta charset="UTF-8">
      <title>static_example</title>
  </head>
  <body>
  
  </body>
  </html>
  ```

- pages 폴더 안에 새로운 ```static``` 폴더 생성

- pages - static 폴더 안에 새로운 ```stylesheets``` 폴더 생성

- pages - static - stylesheets 폴더 안에 새로운 ```style.css``` 파일 생성 후 코드 작성

  ```
  /* 경로 : pages/static/stylesheets/style.css */
  
  h1 {
      color: blue;
  }
  ```

- static_example.html 코드 수정

  ```
  {% load static %}
  
  <!DOCTYPE html>
  <html lang="en">
  <head>
      <meta charset="UTF-8">
      <title>static_example</title>
  
      <!--CSS 파일 불러오는 주소 static 적고 '경로' 표시 -->
      <link rel="stylesheet" href="{% static 'stylesheets/style.css' %}" type="text/css">
  
  </head>
  <body>
  
      <h1>Static Example</h1>
  
  </body>
  </html>
  ```

<br />
<br />
<br />

## [2] 서버 실행

- 서버 실행 후 아래와 같이 결과가 나온다.

<img width="378" alt="Screen Shot 2019-06-04 at 15 35 11" src="https://user-images.githubusercontent.com/46523571/58856869-c22b7380-86de-11e9-87d9-1248237a04d5.png">