# 개 품종 검색 및 이미지 생성 시스템

## 프로젝트 개요
CLIP과 Stable Diffusion을 활용한 개 품종 검색 및 이미지 생성 시스템입니다. 업로드된 개 이미지를 분석하여 유사한 품종의 개를 찾고, 필요시 AI 이미지 생성 기능을 제공합니다.

## 주요 기능
- 🐕 개 품종 자동 인식 (YOLO)
- 🎨 색상 분석 및 분류
- 🔍 CLIP 기반 유사 이미지 검색
- 🖼️ Stable Diffusion 기반 이미지 생성
- 🌐 Flask 웹 API 제공

## 설치 방법

### 1. Python 환경 설정
```bash
# Python 3.8+ 설치 확인
python --version

# 가상환경 생성 (권장)
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

### 2. 의존성 설치
```bash
pip install -r requirements.txt
```

### 3. 모델 파일 다운로드
다음 모델 파일들을 다운로드하여 해당 폴더에 저장해야 합니다:

- **YOLO 모델**: `process/model/` 폴더
  - `seg.pt` - 세그멘테이션 모델
  - `detect6.pt` - 품종 감지 모델
  - `0818.pt` - 객체 감지 모델

- **Stable Diffusion 모델**: `process/converted-model/realistic-hypervae/` 폴더
  - Hugging Face에서 다운로드

- **LoRA 가중치**: `process/lora/` 폴더
  - 각 품종별 LoRA 파일들

- **FAISS 인덱스**: `process/CLIP/` 폴더
  - `dog_index_img.faiss` - 이미지 임베딩 인덱스
  - `dog_ids_img.npy` - 이미지 ID 배열
  - `dog_colors_lab.npy` - 색상 Lab 값 배열
  - `dog_breeds.npy` - 품종 정보 배열

## 사용법

### 웹 서버 실행
```bash
python app.py
```
서버가 실행되면 `http://localhost:5000`에서 웹 인터페이스를 사용할 수 있습니다.

### CLI 사용
```bash
# 이미지 생성 후 검색
python main.py --image path/to/image.jpg --generate

# 업로드된 이미지로만 검색
python main.py --image path/to/image.jpg

# 디버그 모드
python main.py --image path/to/image.jpg --debug --visualize
```

## API 엔드포인트

### POST /search/generated
이미지 생성 후 유사 이미지 검색
- **입력**: 이미지 파일
- **출력**: JSON 형태의 검색 결과

### POST /search/uploaded
업로드된 이미지로 직접 검색
- **입력**: 이미지 파일
- **출력**: JSON 형태의 검색 결과

## 프로젝트 구조
```
Server/
├── main.py              # 메인 검색 및 생성 로직
├── app.py               # Flask 웹 애플리케이션
├── requirements.txt     # Python 의존성
├── process/
│   ├── adapter/         # 샘플 이미지들
│   ├── input/           # 테스트 이미지들
│   ├── model/           # YOLO 모델들 (다운로드 필요)
│   ├── lora/            # LoRA 가중치들 (다운로드 필요)
│   ├── CLIP/            # FAISS 인덱스들 (다운로드 필요)
│   └── converted-model/ # Stable Diffusion 모델 (다운로드 필요)
└── static/
    └── upload/          # 업로드된 이미지들
```

## 주의사항
- 대용량 모델 파일들은 Git에 포함되지 않습니다
- 모델 파일들을 수동으로 다운로드해야 합니다
- GPU 사용을 권장합니다 (CUDA 지원)

## 라이선스
이 프로젝트는 연구 및 교육 목적으로 제작되었습니다.
