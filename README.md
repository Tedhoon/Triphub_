# Triphub_

## > 버전
<p><strong>Triphub 0(대규모 변화) . 0(마이너한 변화) . 0(자잘한 버그)</strong></p>
<p><strong>Triphub 1.2.4 (2019.08.05)</strong></p>

<hr>

### 설치된 package install 하는 방법!
backend 안에서 <strong>pip install -r requirements.txt</strong> 을 입력


##### < 20190805 기준 : Tree 구조 >
```bash
src
├── Triphub
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── Triphub_Accounts
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── static
│   │   ├── css
│   │   │   ├── login.css
│   │   │   └── register.css
│   │   ├── img
│   │   └── js
│   ├── templates
│   │   └── registration
│   │       ├── login.html
│   │       ├── logins.html
│   │       ├── logout.html
│   │       ├── register.html
│   │       ├── register_done.html
│   │       ├── registers.html
│   │       └── user_activate_email.html
│   ├── tests.py
│   ├── tokens.py
│   ├── urls.py
│   └── views.py
│
├── Triphub_Chat
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── static
│   │   ├── css
│   │   ├── img
│   │   └── js
│   ├── templates
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│
├── Triphub_Home
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── static
│   │   ├── css
│   │   │   ├── base.css
│   │   │   └── logbase.css
│   │   ├── img
│   │   └── js
│   ├── templates
│   │   ├── base.html
│   │   ├── logbase.html
│   │   └── main.html
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│
├── Triphub_Room
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── static
│   │   ├── css
│   │   │   ├── create.css
│   │   │   └── loading.css
│   │   ├── img
│   │   └── js
│   ├── templates
│   │   ├── create.html
│   │   ├── loading.html
│   │   └── select.html
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│
├── db.sqlite3
└── manage.py


```

# urls정리

127.0.0.1/

<strong>관리자 페이지</strong>
<ul>
    <li>admin/ : admin 페이지</li>
</ul>
<strong>로그인 페이지</strong>
<ul>
    <li>/ : 로그인 페이지</li>
    <li>/register : 회원가입 페이지</li>
    <li>/logout : logout 페이지</li>
</ul>
<strong>메인(홈) 페이지</strong>
<ul>
    <li>main/ : main 페이지</li>
</ul>
<strong>방과 관련된 페이지</strong>
<ul>
    <li>room/ : room 생성 페이지</li>
    <li>room/select : select 페이지</li>
    <li>room/loading : loading 페이지</li>
</ul>
<strong>채팅 페이지</strong>
<ul>
    <li>chat/ : chat 페이지</li>
</ul>

<hr>

## pip freeze > requirements.txt