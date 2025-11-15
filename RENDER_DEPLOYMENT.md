# Render 배포 가이드 / Render Deployment Guide

Render에 PNG to JPG 변환기를 배포하는 단계별 가이드입니다.
Step-by-step guide to deploy PNG to JPG converter on Render.

## 📋 사전 준비사항 / Prerequisites

- [ ] GitHub 계정
- [ ] Render 계정 (무료 가입 가능)
- [ ] Git 설치 (로컬에)

## 🚀 배포 절차 / Deployment Steps

### 1단계: 프로젝트 Git 초기화 / Initialize Git Repository

프로젝트 폴더에서 실행:

```bash
# Git 저장소 초기화 (아직 안 했다면)
git init

# 모든 파일 추가
git add .

# 첫 커밋
git commit -m "Initial commit: PNG to JPG converter"
```

### 2단계: GitHub 저장소 생성 및 푸시 / Create GitHub Repository

#### 2-1. GitHub에서 새 저장소 생성

1. [GitHub.com](https://github.com) 로그인
2. 우측 상단 "+" → "New repository" 클릭
3. 저장소 이름 입력 (예: `pngtojpg-converter`)
4. Public 또는 Private 선택
5. **"Initialize this repository with a README" 체크 해제** (이미 파일이 있으므로)
6. "Create repository" 클릭

#### 2-2. 로컬 저장소를 GitHub에 연결

GitHub에서 생성한 저장소의 URL을 복사한 후:

```bash
# 원격 저장소 추가 (yourusername을 실제 사용자명으로 변경)
git remote add origin https://github.com/yourusername/pngtojpg-converter.git

# 또는 SSH 사용 시
git remote add origin git@github.com:yourusername/pngtojpg-converter.git

# 브랜치 이름 확인 및 설정
git branch -M main

# GitHub에 푸시
git push -u origin main
```

**문제 해결:**
- 인증 오류가 나면 GitHub Personal Access Token 사용
- 또는 GitHub Desktop 사용

### 3단계: Render 계정 생성 / Create Render Account

1. [render.com](https://render.com) 접속
2. "Get Started for Free" 클릭
3. GitHub 계정으로 로그인 (권장) 또는 이메일로 가입

### 4단계: Render에서 웹 서비스 생성 / Create Web Service on Render

#### 4-1. 새 웹 서비스 시작

1. Render Dashboard에서 **"New +"** 버튼 클릭
2. **"Web Service"** 선택

#### 4-2. GitHub 저장소 연결

1. **"Connect account"** 또는 **"Connect GitHub"** 클릭
2. GitHub 계정 인증
3. 저장소 목록에서 `pngtojpg-converter` 선택
4. **"Connect"** 클릭

#### 4-3. 서비스 설정 입력

다음 정보를 입력:

| 항목 / Field | 값 / Value |
|-------------|-----------|
| **Name** | `pngtojpg-converter` (원하는 이름) |
| **Region** | `Singapore` (한국에서 가장 가까움) 또는 `Oregon` |
| **Branch** | `main` |
| **Root Directory** | (비워두기) |
| **Environment** | `Python 3` |
| **Build Command** | `pip install -r requirements.txt` |
| **Start Command** | `gunicorn -w 4 -b 0.0.0.0:$PORT app:app` |
| **Plan** | `Free` |

#### 4-4. 환경 변수 설정 (선택사항)

"Advanced" 섹션에서 환경 변수 추가:

| Key | Value |
|-----|-------|
| `FLASK_ENV` | `production` |
| `PYTHON_VERSION` | `3.11.0` |

#### 4-5. 배포 시작

1. **"Create Web Service"** 버튼 클릭
2. 자동으로 빌드 시작
3. 빌드 로그 확인 (약 2-5분 소요)

### 5단계: 배포 확인 / Verify Deployment

1. 빌드가 완료되면 **"Live"** 상태로 변경됨
2. 제공된 URL 클릭 (예: `https://pngtojpg-converter.onrender.com`)
3. 웹사이트가 정상 작동하는지 확인

### 6단계: (선택) 커스텀 도메인 설정 / Custom Domain (Optional)

1. Render Dashboard → Settings → Custom Domains
2. 원하는 도메인 입력
3. DNS 설정 안내에 따라 도메인 설정

## 🔧 문제 해결 / Troubleshooting

### 빌드 실패

**문제:** `ModuleNotFoundError` 또는 패키지 설치 실패

**해결:**
- `requirements.txt`에 모든 의존성이 포함되어 있는지 확인
- Build Command가 올바른지 확인: `pip install -r requirements.txt`

### 앱이 시작되지 않음

**문제:** 서비스가 시작되지 않거나 크래시

**해결:**
- Start Command 확인: `gunicorn -w 4 -b 0.0.0.0:$PORT app:app`
- 로그 확인: Render Dashboard → Logs 탭
- `app.py`에서 포트가 `$PORT` 환경 변수를 사용하는지 확인

### 파일 업로드 실패

**문제:** 큰 파일 업로드 시 오류

**해결:**
- `app.py`의 `MAX_CONTENT_LENGTH` 확인 (현재 100MB)
- Render 무료 플랜 제한 확인

## 📝 중요 참고사항 / Important Notes

### 무료 플랜 제한사항

- ⏰ **슬리프 모드**: 15분 비활성 시 자동 슬리프 (첫 요청 시 깨어남)
- ⏱️ **월 750시간** 제한
- 💾 **메모리**: 512MB
- 📦 **디스크**: 1GB

### 보안 설정

프로덕션 배포 전:

1. **SECRET_KEY 변경**
   ```python
   # app.py에서
   import secrets
   app.config['SECRET_KEY'] = secrets.token_hex(32)
   ```
   또는 환경 변수로 설정:
   ```
   SECRET_KEY=your-random-secret-key-here
   ```

2. **환경 변수 사용**
   - Render Dashboard → Environment
   - 민감한 정보는 환경 변수로 관리

## 🔄 업데이트 배포 / Update Deployment

코드를 수정한 후:

```bash
# 변경사항 커밋
git add .
git commit -m "Update: 설명"

# GitHub에 푸시
git push origin main
```

Render는 자동으로 감지하고 재배포합니다!

## 📊 모니터링 / Monitoring

- **로그 확인**: Dashboard → Logs 탭
- **메트릭**: Dashboard → Metrics 탭
- **이벤트**: Dashboard → Events 탭

## 🎉 완료!

배포가 완료되면:
- ✅ 웹사이트 URL 공유 가능
- ✅ 어디서나 접속 가능
- ✅ 자동 HTTPS 제공
- ✅ GitHub 푸시 시 자동 재배포

## 📞 추가 도움말

- [Render 공식 문서](https://render.com/docs)
- [Render 커뮤니티](https://community.render.com)

