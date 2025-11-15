# 서버 배포 가이드 / Server Deployment Guide

이 가이드는 PNG to JPG 변환기를 웹 서버에 배포하는 방법을 설명합니다.
This guide explains how to deploy the PNG to JPG converter to a web server.

## 배포 옵션 / Deployment Options

### 1. PythonAnywhere (가장 쉬움 / Easiest)

**장점 / Pros:**
- 무료 플랜 제공
- 설정이 간단함
- Python 환경이 이미 준비되어 있음

**단계 / Steps:**

1. [PythonAnywhere](https://www.pythonanywhere.com)에 가입
2. Files 탭에서 프로젝트 파일 업로드
3. Web 탭에서 새 웹 앱 생성
4. WSGI 설정 파일 수정:
```python
import sys
path = '/home/yourusername/pngtojpg'
if path not in sys.path:
    sys.path.append(path)

from app import app as application
```

### 2. Render (추천 / Recommended) ⭐

**장점 / Pros:**
- 무료 플랜 제공 (Free tier)
- Heroku보다 설정이 간단함
- 자동 HTTPS 제공
- Git 연동으로 자동 배포
- 15분 비활성 시 슬리프 모드 (무료 플랜)

**단계 / Steps:**

#### 방법 1: GitHub 연동 (권장)

1. **GitHub에 프로젝트 푸시**
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git remote add origin https://github.com/yourusername/pngtojpg.git
   git push -u origin main
   ```

2. **Render 가입 및 서비스 생성**
   - [Render.com](https://render.com)에 가입 (GitHub 계정으로 가능)
   - Dashboard에서 "New +" → "Web Service" 클릭
   - GitHub 저장소 연결

3. **서비스 설정**
   - **Name**: `pngtojpg` (원하는 이름)
   - **Environment**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn -w 4 -b 0.0.0.0:$PORT app:app`
   - **Plan**: Free (무료)

4. **환경 변수 설정 (선택사항)**
   - Settings → Environment Variables
   - `FLASK_ENV=production` 추가

5. **배포**
   - "Create Web Service" 클릭
   - 자동으로 빌드 및 배포 시작
   - 완료되면 `https://your-app-name.onrender.com` 접속 가능

#### 방법 2: Render CLI 사용

```bash
# Render CLI 설치
npm install -g render-cli

# 로그인
render login

# 서비스 생성
render service:create \
  --name pngtojpg \
  --type web \
  --build-command "pip install -r requirements.txt" \
  --start-command "gunicorn -w 4 -b 0.0.0.0:$PORT app:app" \
  --env FLASK_ENV=production
```

**주의사항 / Notes:**
- 무료 플랜은 15분 비활성 시 슬리프 모드 (첫 요청 시 깨어남)
- 파일 업로드 크기 제한: 100MB (현재 설정과 동일)
- 무료 플랜은 월 750시간 제한

**render.yaml 설정 (선택사항)**

프로젝트 루트에 `render.yaml` 파일 생성:
```yaml
services:
  - type: web
    name: pngtojpg
    env: python
    buildCommand: pip install -r requirements.txt
    startCommand: gunicorn -w 4 -b 0.0.0.0:$PORT app:app
    envVars:
      - key: FLASK_ENV
        value: production
```

### 3. Heroku

**단계 / Steps:**

1. Heroku CLI 설치
2. 프로젝트 루트에 `Procfile` 생성:
```
web: gunicorn -w 4 -b 0.0.0.0:$PORT app:app
```

3. `runtime.txt` 생성:
```
python-3.11.0
```

4. 배포:
```bash
heroku create your-app-name
git push heroku main
```

### 4. VPS (Ubuntu/Debian) - Gunicorn + Nginx

**단계 / Steps:**

#### 1. 서버 준비
```bash
# Python 및 pip 설치
sudo apt update
sudo apt install python3 python3-pip python3-venv nginx

# 프로젝트 디렉토리 생성
mkdir -p /var/www/pngtojpg
cd /var/www/pngtojpg
```

#### 2. 가상환경 설정
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

#### 3. Gunicorn으로 실행
```bash
# 테스트 실행
gunicorn -w 4 -b 0.0.0.0:5000 app:app

# 백그라운드 실행 (systemd 사용 권장)
```

#### 4. Systemd 서비스 생성
`/etc/systemd/system/pngtojpg.service` 파일 생성:
```ini
[Unit]
Description=PNG to JPG Converter
After=network.target

[Service]
User=www-data
WorkingDirectory=/var/www/pngtojpg
Environment="PATH=/var/www/pngtojpg/venv/bin"
ExecStart=/var/www/pngtojpg/venv/bin/gunicorn -w 4 -b 127.0.0.1:5000 app:app

[Install]
WantedBy=multi-user.target
```

서비스 시작:
```bash
sudo systemctl daemon-reload
sudo systemctl start pngtojpg
sudo systemctl enable pngtojpg
```

#### 5. Nginx 설정
`/etc/nginx/sites-available/pngtojpg` 파일 생성:
```nginx
server {
    listen 80;
    server_name your-domain.com;

    location / {
        proxy_pass http://127.0.0.1:5000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        
        # 파일 업로드 크기 제한
        client_max_body_size 100M;
    }
}
```

활성화:
```bash
sudo ln -s /etc/nginx/sites-available/pngtojpg /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl restart nginx
```

#### 6. SSL 인증서 (Let's Encrypt)
```bash
sudo apt install certbot python3-certbot-nginx
sudo certbot --nginx -d your-domain.com
```

### 4. Docker 사용

**Dockerfile 생성:**
```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "app:app"]
```

**docker-compose.yml:**
```yaml
version: '3.8'

services:
  web:
    build: .
    ports:
      - "5000:5000"
    volumes:
      - ./uploads:/app/uploads
      - ./output:/app/output
    environment:
      - FLASK_ENV=production
```

**실행:**
```bash
docker-compose up -d
```

## 보안 설정 / Security Settings

### 1. SECRET_KEY 변경
`app.py`에서 SECRET_KEY를 강력한 랜덤 문자열로 변경:
```python
import secrets
app.config['SECRET_KEY'] = secrets.token_hex(32)
```

### 2. 환경 변수 사용
`.env` 파일 생성:
```
SECRET_KEY=your-secret-key-here
FLASK_ENV=production
```

`python-dotenv` 설치 후 `app.py`에 추가:
```python
from dotenv import load_dotenv
load_dotenv()
```

### 3. 파일 업로드 제한
현재 설정: 100MB
`app.py`에서 조정 가능:
```python
app.config['MAX_CONTENT_LENGTH'] = 100 * 1024 * 1024
```

## 성능 최적화 / Performance Optimization

### 1. Gunicorn 워커 수 조정
```bash
# CPU 코어 수에 맞게 조정
gunicorn -w $(nproc) -b 0.0.0.0:5000 app:app
```

### 2. Nginx 캐싱
Nginx 설정에 추가:
```nginx
location /static {
    alias /var/www/pngtojpg/static;
    expires 30d;
}
```

### 3. Redis 캐싱 (선택사항)
대용량 파일 처리 시 Redis를 사용하여 세션 관리

## 모니터링 / Monitoring

### 로그 확인
```bash
# Gunicorn 로그
sudo journalctl -u pngtojpg -f

# Nginx 로그
sudo tail -f /var/log/nginx/access.log
sudo tail -f /var/log/nginx/error.log
```

## 문제 해결 / Troubleshooting

### 포트가 이미 사용 중
```bash
# 포트 사용 확인
sudo lsof -i :5000

# 프로세스 종료
sudo kill -9 <PID>
```

### 권한 문제
```bash
sudo chown -R www-data:www-data /var/www/pngtojpg
sudo chmod -R 755 /var/www/pngtojpg
```

## 추천 서버 제공업체 / Recommended Hosting Providers

1. **Render** ⭐ - 가장 추천! 무료 플랜, 간편한 설정, 자동 HTTPS
2. **PythonAnywhere** - 초보자용, 무료 플랜
3. **Heroku** - 간편한 배포, 무료 플랜 (제한적)
4. **DigitalOcean** - VPS, $5/월부터
5. **AWS EC2** - 확장 가능, 복잡함
6. **Google Cloud Platform** - 유연한 설정
7. **Azure** - Microsoft 생태계

## 빠른 시작 (로컬 테스트) / Quick Start (Local Testing)

```bash
# 가상환경 활성화
source venv/bin/activate  # Linux/Mac
# 또는
venv\Scripts\activate  # Windows

# 의존성 설치
pip install -r requirements.txt

# 개발 서버 실행
python app.py

# 브라우저에서 http://localhost:5000 접속
```

## 프로덕션 실행 / Production Run

```bash
# Gunicorn 사용
gunicorn -w 4 -b 0.0.0.0:5000 app:app

# 또는 systemd 서비스 사용 (위 참조)
```

