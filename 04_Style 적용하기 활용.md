# Style 적용하기 활용

<br />
<br />
<br />

## [1] 구조 만들기

- Utilities - templates - utilities - base.html 생성 및 코드 작성

  - 다른 페이지가 base.html 파일을 상속을 받는다.

    ```
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Utilities Base</title>
    </head>
    <body>
        <header>
            <h1>Utilities Base</h1>
        </header>
    
        <section>  <!--index.html 부분이라고 생각하면 된다. -->
            {% block body %}
            {% endblock %}
        </section>
    
        <footer>
            <p>Copyright @ 2019</p>
        </footer>
    </body>
    </html>
    ```

- Utilities - templates - utilities - index.html 코드 수정

  - (기존)

  - ```
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>index</title>
    </head>
    <body>
    
        <h1>Welcom to index of Utilities</h1>
    
    </body>
    </html>
    ```

  - (변경)

  - ```
    {% extends 'utilities/base.html' %} <!--Utilities - templates 안에서 파일을 찾는다. +'경로('utilities/base.html')' -->
    
    {% block body %}
        <h2>Welcome to Utilities Page ;)</h2>
    {% endblock %}
    ```

- 서버를 실행 후 [http://127.0.0.1:8000/utilities/index/](http://127.0.0.1:8000/utilities/index/) 접속하면 index.html을 상속 받은 base.html을 볼 수 있다.

  - 특이한건 F12 키 누른 후 개발자모드로 보면 index.html 정보가 없이 header와 footer만 볼 수 있다.

- Utilities - static - stylesheets - base.css 파일 생성 및 코드 작성

- ```
  h2 {
      color: yellow;
  }
  ```

- base.html 코드 수정

- ```
  {% load static %}
  
  <!DOCTYPE html>
  <html lang="en">
  <head>
      <meta charset="UTF-8">
      <title>Utilities Base</title>
  
      <!--CSS 파일 불러오는 주소 static 적고 '경로' 표시 -->
      <link rel="stylesheet" href="{% static 'stylesheets/base.css' %}" type="text/css">
  
  </head>
  <body>
      <header>
          <h1>Utilities Base</h1>
      </header>
  
      <section>  <!--index.html 부분이라고 생각하면 된다. -->
          {% block body %}
          {% endblock %}
      </section>
  
      <footer>
          <p>Copyright @ 2019</p>
      </footer>
  </body>
  </html>
  ```

- index.html에서 작성한 스타일을 base.html이 상속을 받아서 코드 한줄로 표현 할 수 있다.













<br />
<br />
<br />

## [2] 서버 실행

- 서버 실행 후 아래와 같이 결과가 나온다.