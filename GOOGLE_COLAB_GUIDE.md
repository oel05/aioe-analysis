# Google Colab 사용 가이드

이 문서는 AIOE 분석 프로젝트를 Google Colab에서 실행하기 위한 준비 과정을 안내합니다.

---

## 📦 1단계: 프로젝트 파일 다운로드

아래 링크를 클릭하여 `aioe_proj.zip` 파일을 다운로드하세요:

### 🔗 [aioe_proj.zip 다운로드](https://drive.google.com/file/d/1mTcXfrTEOTM5G4ZhsfUYA_rXC2gYb5UC/view?usp=sharing)

> **파일 크기**: 약 10MB
> **포함 내용**: 노트북 5개, 데이터 파일, 실습용 노트북 3개

---

## 📂 2단계: 압축 풀기

1. 다운로드한 `aioe_proj.zip` 파일을 찾으세요
   - Windows: 보통 `다운로드` 폴더
   - Mac: `Downloads` 폴더

2. 파일을 **압축 해제**하세요
   - Windows: 파일 우클릭 → `압축 풀기` 또는 `모두 압축 풀기`
   - Mac: 파일을 더블클릭

3. `aioe_proj` 폴더가 생성됩니다

---

## ☁️ 3단계: Google Drive에 업로드

1. [Google Drive](https://drive.google.com)에 접속하세요

2. **메인 화면** (내 드라이브 최상위)에 있는지 확인하세요
   - 왼쪽 메뉴에서 "내 드라이브" 클릭
   - 주소창에 `https://drive.google.com/drive/my-drive` 표시 확인

3. `aioe_proj` 폴더를 **드래그 앤 드롭**으로 업로드
   - 또는 `새로 만들기` → `폴더 업로드` 선택

4. 업로드 완료 후 **경로 확인**:
   ```
   내 드라이브/aioe_proj/
   ```

---

## ✅ 4단계: 구조 확인

업로드가 완료되면 다음 구조가 되어야 합니다:

```
내 드라이브/
└── aioe_proj/
    ├── datas/
    │   ├── raw/
    │   └── processed/
    ├── notebooks/
    │   ├── 00_AIOE_Intro.ipynb
    │   ├── 01_AIOE_Data_Preprocessing.ipynb
    │   ├── 02_AIOE_Calculation.ipynb
    │   ├── 03_AIOE_EDA.ipynb
    │   └── 04_AIOE_Outro.ipynb
    └── notebooks_실습용/
        ├── 01_AIOE_Data_Preprocessing_실습용.ipynb
        ├── 02_AIOE_Calculation_실습용.ipynb
        └── 03_AIOE_EDA_실습용.ipynb
```

**확인 방법:**
1. Google Drive에서 `aioe_proj` 폴더 클릭
2. `notebooks` 폴더가 보이는지 확인
3. `datas` 폴더가 보이는지 확인

---

## 🚀 5단계: 노트북 실행하기

### 노트북 열기

1. Google Drive에서 `aioe_proj/notebooks/` 폴더로 이동

2. `00_AIOE_Intro.ipynb` 파일 **우클릭**

3. `연결 앱` → `Google Colaboratory` 선택
   - 처음 사용하는 경우 "앱 연결" 필요할 수 있음

4. Google Colab에서 노트북이 열립니다

### 실행 순서

다음 순서대로 노트북을 실행하세요:

1. **00_AIOE_Intro.ipynb** - 프로젝트 소개 및 배경
2. **01_AIOE_Data_Preprocessing.ipynb** - 데이터 전처리
3. **02_AIOE_Calculation.ipynb** - AIOE 점수 계산
4. **03_AIOE_EDA.ipynb** - 탐색적 데이터 분석
5. **04_AIOE_Outro.ipynb** - 결론 및 다음 단계

### 실습하기 (선택사항)

- `notebooks_실습용/` 폴더의 노트북으로 직접 코딩 연습 가능
- TODO 주석에 따라 코드를 작성하세요
- 막히면 `notebooks/` 폴더의 정답 노트북 참고

---

## 💡 문제 해결

### Q1: "파일을 찾을 수 없습니다" 오류가 나요

**원인**: `aioe_proj` 폴더가 메인 드라이브가 아닌 다른 위치에 있을 수 있습니다

**해결**:
1. Google Drive에서 `aioe_proj` 폴더를 찾으세요
2. 폴더를 **메인 드라이브 최상위**로 이동:
   - 폴더 우클릭 → `이동` → `내 드라이브` 선택

### Q2: Google Colaboratory가 연결 앱 목록에 없어요

**해결**:
1. `.ipynb` 파일 우클릭
2. `연결 앱` → `앱 더보기` 클릭
3. "Colaboratory" 검색
4. `설치` 버튼 클릭
5. 권한 승인
