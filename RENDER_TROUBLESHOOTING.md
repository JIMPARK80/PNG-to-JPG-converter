# Render 502 Bad Gateway 오류 해결 가이드 / Render 502 Error Troubleshooting

## 🔴 502 Bad Gateway 오류 해결 방법

### 1. Render Dashboard에서 로그 확인

1. Render Dashboard 접속
2. 서비스 선택
3. **"Logs"** 탭 클릭
4. 오류 메시지 확인

### 2. 일반적인 원인 및 해결책

#### 원인 1: Gunicorn 워커 수가 너무 많음

**문제:** 무료 플랜은 리소스가 제한적입니다.

**해결:** 
- 워커 수를 2개로 줄임 (기본값: 4개)
- `Procfile` 또는 Render 설정에서:
  ```
  gunicorn --workers 2 --threads 2 --timeout 120 --bind 0.0.0.0:$PORT app:app
  ```

#### 원인 2: 타임아웃

**문제:** 이미지 처리 시간이 길어서 타임아웃 발생

**해결:**
- 타임아웃을 120초로 설정
- `--timeout 120` 옵션 추가

#### 원인 3: 빌드 실패

**문제:** 의존성 설치 실패

**해결:**
- `requirements.txt` 확인
- Build Command 확인: `pip install -r requirements.txt`

#### 원인 4: 포트 설정 오류

**문제:** 포트가 올바르게 설정되지 않음

**해결:**
- Start Command에 `$PORT` 환경 변수 사용 확인
- `--bind 0.0.0.0:$PORT` 형식 확인

### 3. 수정된 설정

**Procfile:**
```
web: gunicorn --workers 2 --threads 2 --timeout 120 --bind 0.0.0.0:$PORT app:app
```

**render.yaml:**
```yaml
startCommand: gunicorn --workers 2 --threads 2 --timeout 120 --bind 0.0.0.0:$PORT app:app
```

### 4. Render Dashboard에서 수동 설정 변경

1. Render Dashboard → 서비스 선택
2. **Settings** 탭 클릭
3. **Start Command** 수정:
   ```
   gunicorn --workers 2 --threads 2 --timeout 120 --bind 0.0.0.0:$PORT app:app
   ```
4. **Save Changes** 클릭
5. **Manual Deploy** → **Deploy latest commit** 클릭

### 5. 추가 확인 사항

- ✅ Python 버전이 올바른지 확인 (3.11.0)
- ✅ 모든 의존성이 `requirements.txt`에 포함되어 있는지 확인
- ✅ `templates` 폴더가 올바르게 포함되어 있는지 확인
- ✅ `.gitignore`에 필요한 파일이 제외되지 않았는지 확인

### 6. 로그 확인 명령어

Render Dashboard의 Logs 탭에서 다음을 확인:

```
[INFO] Starting gunicorn
[INFO] Listening at: http://0.0.0.0:XXXX
[INFO] Using worker: sync
```

오류가 있다면:
- `ModuleNotFoundError`: 의존성 누락
- `Port already in use`: 포트 충돌
- `Timeout`: 타임아웃 설정 필요

### 7. 빠른 해결 체크리스트

- [ ] Start Command가 올바른지 확인
- [ ] 워커 수를 2개로 줄임
- [ ] 타임아웃을 120초로 설정
- [ ] 로그에서 오류 메시지 확인
- [ ] 수동 재배포 실행

### 8. 여전히 문제가 있다면

1. Render Support에 문의: support@render.com
2. GitHub Issues에 문제 보고
3. 로그 전체 내용을 공유

