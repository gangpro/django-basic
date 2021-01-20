# Django
> macOS Mojave 10.14.5 <br>
> python 3.6.8 <br>
> django 2.2.1

<br>
<br>
<br>

## [1] macOS에 python3 설치
* brew에서 파이썬 검색 ```brew search python``` 
###
    ➜  Django git:(master) ✗ brew search python
    ==> Formulae
    app-engine-python    boost-python@1.59    ipython@5            python-markdown      wxpython
    boost-python         gst-python           micropython          python-yq            zpython
    boost-python3        ipython              python               python@2
    
    ==> Casks
    awips-python                       kk7ds-python-runtime               mysql-connector-python
    awips-python                       kk7ds-python-runtime               mysql-connector-python
    
    If you meant "python" specifically:
    It was migrated from homebrew/cask to homebrew/core.

* 파이썬3 설치 ```brew install python3``` 
###
    ➜  Django git:(master) ✗ brew install python3
    ==> Installing dependencies for python: gdbm and xz
    ==> Installing python dependency: gdbm
    ==> Downloading https://homebrew.bintray.com/bottles/gdbm-1.18.1.mojave.bottle.1.tar.gz
    ######################################################################## 100.0%
    ==> Pouring gdbm-1.18.1.mojave.bottle.1.tar.gz
    🍺  /usr/local/Cellar/gdbm/1.18.1: 20 files, 586.8KB
    ==> Installing python dependency: xz
    ==> Downloading https://homebrew.bintray.com/bottles/xz-5.2.4.mojave.bottle.tar.gz
    ==> Downloading from https://akamai.bintray.com/01/010667293df282c8bceede3bcd36953dd57c56cef608d09a5b506
    ######################################################################## 100.0%
    ==> Pouring xz-5.2.4.mojave.bottle.tar.gz
    🍺  /usr/local/Cellar/xz/5.2.4: 92 files, 1MB
    ==> Installing python
    ==> Downloading https://homebrew.bintray.com/bottles/python-3.7.3.mojave.bottle.tar.gz
    ==> Downloading from https://akamai.bintray.com/25/25e0099852136c4ef1efd221247d0f67aa71f7b624211b98898f8
    ######################################################################## 100.0%
    ==> Pouring python-3.7.3.mojave.bottle.tar.gz
    ==> /usr/local/Cellar/python/3.7.3/bin/python3 -s setup.py --no-user-cfg install --force --verbose --ins
    ==> /usr/local/Cellar/python/3.7.3/bin/python3 -s setup.py --no-user-cfg install --force --verbose --ins
    ==> /usr/local/Cellar/python/3.7.3/bin/python3 -s setup.py --no-user-cfg install --force --verbose --ins
    ==> Caveats
    Python has been installed as
      /usr/local/bin/python3
    
    Unversioned symlinks `python`, `python-config`, `pip` etc. pointing to
    `python3`, `python3-config`, `pip3` etc., respectively, have been installed into
      /usr/local/opt/python/libexec/bin
    
    If you need Homebrew's Python 2.7 run
      brew install python@2
    
    You can install Python packages with
      pip3 install <package>
    They will install into the site-package directory
      /usr/local/lib/python3.7/site-packages
    
    See: https://docs.brew.sh/Homebrew-and-Python
    ==> Summary
    🍺  /usr/local/Cellar/python/3.7.3: 3,863 files, 59.8MB
    ==> Caveats
    ==> python
    Python has been installed as
      /usr/local/bin/python3
    
    Unversioned symlinks `python`, `python-config`, `pip` etc. pointing to
    `python3`, `python3-config`, `pip3` etc., respectively, have been installed into
      /usr/local/opt/python/libexec/bin
    
    If you need Homebrew's Python 2.7 run
      brew install python@2
    
    You can install Python packages with
      pip3 install <package>
    They will install into the site-package directory
      /usr/local/lib/python3.7/site-packages
    
    See: https://docs.brew.sh/Homebrew-and-Python

<br>
<br>
<br>

## [2] Django 설치
1. Pycharm 앱 실행
2. ```Django```이름의 새로운 프로젝트 생성
3. 터미널에서 아래 코드 실행
  - ```pip install django```
  - ```django-admin startproject intro .```
  - ```python manage.py runserver```
    ###
        (venv) ➜  Django pip install django
        Collecting django
          Using cached https://files.pythonhosted.org/packages/b1/1d/2476110614367adfb079a9bc718621f9fc8351e9214e1750cae1832d4090/Django-2.2.1-py3-none-any.whl
    
        # 현재 디렉토리에 intro란 이름의 django 설치
        (venv) ➜  Django django-admin startproject intro .
    
        # 서버 실행
        (venv) ➜  Django python manage.py runserver
        
        Watching for file changes with StatReloader
        Performing system checks...
        
        System check identified no issues (0 silenced).
        
        You have 17 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
        Run 'python manage.py migrate' to apply them.
        
        June 03, 2019 - 06:56:50
        Django version 2.2.1, using settings 'intro.settings'
        Starting development server at http://127.0.0.1:8000/
        Quit the server with CONTROL-C.
        [03/Jun/2019 06:56:52] "GET / HTTP/1.1" 200 16348
        [03/Jun/2019 06:56:52] "GET /static/admin/css/fonts.css HTTP/1.1" 200 423
        Not Found: /robots.txt
        [03/Jun/2019 06:56:52] "GET /robots.txt HTTP/1.1" 404 1968
        [03/Jun/2019 06:56:52] "GET /static/admin/fonts/Roboto-Bold-webfont.woff HTTP/1.1" 200 86184
        [03/Jun/2019 06:56:52] "GET /static/admin/fonts/Roboto-Regular-webfont.woff HTTP/1.1" 200 85876
        [03/Jun/2019 06:56:52] "GET /static/admin/fonts/Roboto-Light-webfont.woff HTTP/1.1" 200 85692
        Not Found: /favicon.ico
        [03/Jun/2019 06:56:53] "GET /favicon.ico HTTP/1.1" 404 1971

* 서버가 실행되면 인터넷 브라우저에서 아래와 같은 화면이 뜬다.
<img width="1123" alt="Screen Shot 2019-06-03 at 16 03 44" src="https://user-images.githubusercontent.com/46523571/58782318-356ab200-8619-11e9-9110-9862f14ac2b3.png">

<br>
<br>
<br>

## [3] .gitignore 파일 생성
1. Django 프로젝트에서 ```.gitignore``` 이름의 새로운 파일 생성
2. ```https://www.gitignore.io/``` 접속해서 아래와 같이 추가한 후 Create 버튼 클릭
<img width="953" alt="Screen Shot 2019-06-03 at 16 08 26" src="https://user-images.githubusercontent.com/46523571/58782680-2cc6ab80-861a-11e9-955d-6aa0275ff0f0.png">
3. 생성된 코드를 ```.gitignore```파일에 붙여넣은 후 저장하기

<br>
<br>
<br>

## [4] pages 새로운 앱 생성
* pages란 이름으로 앱을 하나 생성하겠다 라는 의미
  - 터미널 실행
  - ```python manage.py startapp pages```

* pages 폴더 안에 파일 의미
  - admin.py : 관리자 페이지 설정 가능
  - apps.py : 앱의 정보가 담기는 곳(default 상태 유지하기)
  - models.py : 데이터베이스, 앱에서 사용하는 모델 설정 
  - tests.py : 테스트 코드 작성하는 곳
  - views.py : Spring MVC에서 컨트롤러를 하는 곳

* 하나의 앱을 만들고 나면 반드시 해야할 게 있다.
  - intro 폴더 settings.py 안에 소스코드 수정
  - ```INSTALLED_APPS = [
    'pages.apps.PagesConfig',``` 추가 해야한다.´  
    # pages 폴더 - apps.py - class PagesConfig(AppConfig): 값을 의미


* 추가 설정
  - intro 폴더 settings.py 안에 소스코드 수정
    - ```LANGUAGE_CODE = 'ko-kr'```
    - ```TIME_ZONE = 'Asia/Seoul'```

<br>
<br>
<br>

## [5] intro - urls.py 코드 수정
    from django.contrib import admin
    from django.urls import path
    from pages import views
    
    urlpatterns = [
        path('index/', views.index),  # index란 곳으로 들어오면 views의 index를 실행하겠다 선언
        path('admin/', admin.site.urls),
    ]

<br>
<br>
<br>

## [6] pages - views.py 함수 코드 추가 
    from django.shortcuts import render
    
    
    # Create your views here.
    def index(request):
        return render(request, 'index.html')
   
<br>
<br>
<br>
     
## [7] pages 폴더 안에 새로운 ```templates``` 폴더 생성

<br>
<br>
<br>

## [8] pages 폴더 - templates 폴더 - index.html 파일 생성
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>index</title>
    </head>
    <body>
    
        <h1>Hello World :)</h1>
    
    </body>
    </html>
    
<br>
<br>
<br>

## [9] index.html 웹으로 실행해 보기
* 터미널 실행
* 서버 시작
  - ```python manage.py runserver```
    ###
        (venv) ➜  Django python manage.py runserver
        Watching for file changes with StatReloader
        Performing system checks...
        
        System check identified no issues (0 silenced).
        
        You have 17 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
        Run 'python manage.py migrate' to apply them.
        
        June 03, 2019 - 16:40:08
        Django version 2.2.1, using settings 'intro.settings'
        Starting development server at http://127.0.0.1:8000/
        Quit the server with CONTROL-C.
        Not Found: /
        [03/Jun/2019 16:40:11] "GET / HTTP/1.1" 404 2026

* http://127.0.0.1:8000/ 접속하면 서버는 실행되지만 Page not found가 뜸.
* 이유는 우리는 index.html 파일만 만들었기 때문
* http://127.0.0.1:8000/index/ 이렇게 입력하면 'Hello World'가 뜬다 :)
* <img width="484" alt="Screen Shot 2019-06-03 at 17 09 05" src="https://user-images.githubusercontent.com/46523571/58786361-571c6700-8622-11e9-9c6e-ce307f6d0513.png">

