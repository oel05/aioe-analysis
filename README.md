# 🤖 AIOE (AI Occupational Exposure) 분석 프로젝트

**AI가 직업에 미치는 영향을 데이터로 분석하는 프로젝트**

ChatGPT와 같은 대형 언어 모델(LLM)이 다양한 직업에 어떤 영향을 미치는지 정량적으로 분석합니다.

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

## 📊 프로젝트 개요

이 프로젝트는 Felten et al. (2023)의 연구 방법론을 기반으로 AIOE(AI Occupational Exposure) 지표를 계산하고, 머신러닝을 활용하여 AI가 직업 시장에 미치는 영향을 분석합니다.

**주요 분석 내용:**
- 📐 AIOE 점수 계산 (974개 직업)
- 🔍 탐색적 데이터 분석 (EDA)
- 🎯 임금 예측 모델링 (Regression)
- 🎨 직업 군집 분석 (K-Means Clustering)

## 🚀 빠른 시작

### 1. 환경 설정

```bash
# 저장소 클론
git clone [<repository-url>](https://github.com/oel05/aioe-analysis.git)
cd aioe_proj

# 가상환경 생성
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 필요한 패키지 설치
pip install -r requirements.txt
```

### 2. 노트북 실행

Jupyter Notebook을 실행하고 **순서대로** 노트북을 실행하세요:

```bash
jupyter notebook
```

**실행 순서:**
```
00_AIOE_intro.ipynb              ← 프로젝트 개요 (시작은 여기서!)
    ↓
01_AIOE_Data_Preprocessing.ipynb ← 데이터 전처리 및 AIOE 계산
    ↓
02_AIOE_EDA.ipynb                ← 탐색적 데이터 분석
    ↓
03_AIOE_Modeling.ipynb           ← 머신러닝 모델링
    ↓
04_AIOE_Cluster.ipynb            ← 군집 분석
```

## 📁 프로젝트 구조

```
aioe_proj/
├── README.md                           # 프로젝트 설명
├── requirements.txt                    # Python 패키지 목록
│
├── notebooks/                          # Jupyter 노트북
│   ├── 00_AIOE_intro.ipynb            # 프로젝트 소개
│   ├── 01_AIOE_Data_Preprocessing.ipynb  # 데이터 전처리
│   ├── 02_AIOE_EDA.ipynb              # 탐색적 데이터 분석
│   ├── 03_AIOE_Modeling.ipynb         # 머신러닝 모델링
│   └── 04_AIOE_Cluster.ipynb          # 군집 분석
│
├── datas/                              # 데이터
│   ├── raw/                           # 원본 데이터 (수정 금지)
│   │   ├── Abilities.txt              # O*NET 능력 데이터
│   │   ├── Occupation Data.txt        # O*NET 직업 데이터
│   │   ├── all_data_M_2024.xlsx       # BLS OEWS 임금 데이터
│   │   ├── AIOE_DataAppendixD.csv     # AI-능력 매핑
│   │   └── AIOE_DataAppendixE.csv     # AI 성능
│   │
│   └── processed/                     # 처리된 데이터 (재생성 가능)
│       ├── job_aioe_processed.csv     # 01번 노트북 출력
│       └── job_aioe_for_modeling.csv  # 02번 노트북 출력
│
└── references/                         # 참고 문헌
    ├── How will Language Modelers like ChatGPT Affect....pdf
    ├── calculating_occupational_exposure.pdf
    └── ChatGPT_Impact_Summary.md
```

## 📖 주요 개념

### AIOE (AI Occupational Exposure)

AIOE는 **각 직업이 AI 기술에 얼마나 노출되어 있는지**를 나타내는 지표입니다.

**계산 공식:**

$$\text{AIOE}_k = \frac{\sum_{j} A_{ij} \times L_{jk} \times I_{jk}}{\sum_{j} L_{jk} \times I_{jk}}$$

- **A<sub>ij</sub>**: 직업 i가 능력 j를 얼마나 필요로 하는가? (1~5점)
- **L<sub>jk</sub>**: AI 기술 k가 능력 j를 수행할 수 있는가? (0~1)
- **I<sub>jk</sub>**: AI 기술 k가 능력 j를 얼마나 잘 수행하는가? (0~1)

**예시:**
- 변호사 (Lawyers): AIOE = 4.8 (높음) → 문서 작성, 계약서 검토 등
- 요리사 (Cooks): AIOE = 2.1 (낮음) → 육체적 작업, AI 대체 어려움

## 📊 데이터 소스

| 소스 | 제공 기관 | 내용 |
|------|----------|------|
| **O*NET** | 미국 노동부 | 직업별 능력 중요도 (52개 능력) |
| **BLS OEWS** | 미국 노동통계국 | 고용 규모 및 평균 임금 |
| **Felten et al.** | 연구 논문 | AI-능력 매핑, AI 성능 데이터 |

## 🎯 주요 결과

### 1. AIOE 분포
- **최고 AIOE 직업**: 텔레마케터, 법학 교수, 언어학 교수
- **최저 AIOE 직업**: 요리사, 정비공, 건설 노동자

### 2. AIOE와 임금의 관계
- 양의 상관관계 확인 (r ≈ 0.4~0.5)
- 고AIOE ≠ 항상 고임금 (복잡한 관계)

### 3. 임금 예측 모델
- 최고 성능: LightGBM (R² ≈ 0.7~0.8)
- 텍스트 피처 추가 시 성능 향상

### 4. 직업 군집
- 5~6개 주요 그룹 발견
- "고AIOE-고임금", "저AIOE-저임금" 등

## 🛠️ 기술 스택

**언어 & 프레임워크:**
- Python 3.8+
- Jupyter Notebook

**핵심 라이브러리:**
- `pandas`, `numpy`: 데이터 처리
- `matplotlib`, `seaborn`: 시각화
- `scikit-learn`: 머신러닝
- `lightgbm`: Gradient Boosting

## 📚 참고 문헌

1. **Felten, E., Raj, M., & Seamans, R. (2023)**
   *How will Language Modelers like ChatGPT Affect Occupations and Industries?*
   arXiv:2303.01157

2. **Felten, E., Raj, M., & Seamans, R. (2021)**
   *Occupational, industry, and geographic exposure to artificial intelligence*
   Strategic Management Journal, 42(12), 2195-2217

## 🤝 기여

이 프로젝트는 교육 목적으로 제작되었습니다. 개선 제안이나 버그 리포트는 Issue를 통해 제출해주세요.

## 📝 라이선스

MIT License

## 👤 작성자

- 연구 기반: Felten et al. (2023)
- 구현: LeoLAB

## 🙏 감사의 말

- O*NET Database (U.S. Department of Labor)
- Bureau of Labor Statistics (BLS)
- Felten, Raj, Seamans 연구팀

---

**💡 Tip:** 프로젝트에 대한 자세한 설명은 `notebooks/00_AIOE_intro.ipynb`를 참고하세요!


