# Render 배포 체크리스트 / Render Deployment Checklist

배포 전 확인사항을 체크하세요.
Check these items before deployment.

## ✅ 필수 파일 확인 / Required Files

- [x] `app.py` - Flask 애플리케이션
- [x] `requirements.txt` - 의존성 목록
- [x] `templates/index.html` - 웹 인터페이스
- [x] `Procfile` 또는 `render.yaml` - 배포 설정
- [x] `.gitignore` - Git 제외 파일

## ✅ 코드 확인 / Code Check

- [ ] `app.py`에서 `SECRET_KEY` 변경 (프로덕션용)
- [ ] 포트 설정이 `$PORT` 환경 변수 사용 (Render 자동 설정)
- [ ] 파일 크기 제한 적절히 설정됨 (100MB)

## ✅ Git 준비 / Git Preparation

- [ ] Git 저장소 초기화됨 (`git init`)
- [ ] 모든 파일 커밋됨 (`git commit`)
- [ ] GitHub 저장소 생성됨
- [ ] 원격 저장소 연결됨 (`git remote add origin`)
- [ ] GitHub에 푸시됨 (`git push`)

## ✅ Render 설정 / Render Configuration

- [ ] Render 계정 생성됨
- [ ] GitHub 저장소 연결됨
- [ ] 서비스 설정 입력:
  - [ ] Name: `pngtojpg-converter`
  - [ ] Environment: `Python 3`
  - [ ] Build Command: `pip install -r requirements.txt`
  - [ ] Start Command: `gunicorn -w 4 -b 0.0.0.0:$PORT app:app`
  - [ ] Plan: `Free`

## ✅ 배포 후 확인 / Post-Deployment Check

- [ ] 빌드 성공
- [ ] 서비스 "Live" 상태
- [ ] 웹사이트 접속 가능
- [ ] 파일 업로드 테스트
- [ ] 변환 기능 테스트
- [ ] 다운로드 기능 테스트

## 🔒 보안 체크 / Security Check

- [ ] SECRET_KEY를 환경 변수로 설정 (선택사항)
- [ ] 민감한 정보가 코드에 하드코딩되지 않음
- [ ] 파일 업로드 크기 제한 적절함

## 📝 다음 단계 / Next Steps

배포 완료 후:
1. 웹사이트 URL 저장
2. 테스트 사용자에게 공유
3. 모니터링 설정 (선택사항)
4. 커스텀 도메인 설정 (선택사항)

