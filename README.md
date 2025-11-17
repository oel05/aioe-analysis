# AI Occupational Exposure (AIOE) 분석 프로젝트

<div align="center">

**"내 직업이 AI에 얼마나 노출될까?"**

*데이터로 답하는 AI 시대의 직업 전망*

[![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange.svg)](https://jupyter.org/)
[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-Educational-green.svg)]()
[![GitHub Pages](https://img.shields.io/badge/Report-Live-success.svg)](https://oel05.github.io/aioe-analysis/)

**🔗 [📊 인포그래픽 분석 보고서 보기](https://oel05.github.io/aioe-analysis/)**

</div>

---

## 프로젝트 소개

ChatGPT, Claude, Gemini... AI가 우리 일상에 깊숙이 들어온 지금, 많은 사람들이 궁금해합니다:

> "AI가 내 직업을 대체하게 될까?"
> "어떤 직업이 AI의 영향을 많이 받을까?"
> "나는 어떤 능력을 개발해야 할까?"

이 프로젝트는 **Princeton University와 NYU의 연구진이 개발한 AIOE(AI Occupational Exposure) 방법론**을 활용하여, **894개 직업**이 **AI 기술(특히 언어 모델)**에 얼마나 노출되는지를 **데이터 기반으로 분석**합니다.

### 왜 이 분석이 필요한가?

- **객관적 지표**: 추측이나 의견이 아닌, 데이터에 기반한 측정
- **직업별 세부 분석**: 894개 직업 각각의 AI 노출도 계산
- **능력 기반 접근**: 각 직업이 요구하는 52개 능력을 AI가 얼마나 잘 수행하는지 평가
- **검증된 방법론**: Strategic Management Journal 게재 논문의 분석 방법 재현

---

## 무엇을 배우나요?

이 프로젝트를 통해 다음을 경험할 수 있습니다:

### 1. 데이터 과학 실전 스킬
- **데이터 전처리**: 여러 출처의 데이터를 하나로 병합하고 정제
- **복잡한 지표 계산**: 정규화, 가중 평균, Z-score 표준화
- **탐색적 데이터 분석**: 시각화를 통한 인사이트 도출

### 2. 실제 연구 논문 재현
- Felten et al. (2021) 논문의 방법론을 직접 구현
- 연구 방법의 이해와 한계 인식
- 결과 해석과 비판적 사고

### 3. AI 시대에 대한 통찰
- AI가 잘하는 것 vs 못하는 것
- 직업의 미래와 변화 방향
- 개인의 커리어 전략 수립

---

## 데이터 소개

### O*NET Database

- **출처**: 미국 노동부 O*NET 프로그램
- **버전**: 30.0 (2024년 7월)
- **내용**: 894개 직업의 52개 능력에 대한 중요도(Importance)와 수준(Level)
- **라이선스**: Public Domain

### MTurk AI Mapping Data

- **출처**: Felten et al. (2021) 연구
- **내용**: 10개 AI 응용 프로그램이 52개 능력을 얼마나 잘 수행하는지 평가 (Beta 값)
- **사용**: Language Modeling (ChatGPT, Claude 등 대형 언어 모델)

---

## AIOE 계산 방법

### 공식

각 직업 $j$ 의 AIOE는 다음과 같이 계산됩니다:

$$
\text{AIOE}_j = \frac{\sum_{i=1}^{52} (\text{Level}_{ij} \times \text{Importance}_{ij} \times \beta_i)}{\sum_{i=1}^{52} (\text{Level}_{ij} \times \text{Importance}_{ij})}
$$

**변수 설명:**

- $i$ : 능력 인덱스 (1~52개 능력)
- $j$ : 직업 인덱스 (1~894개 직업)
- $\text{Level}_{ij}$ : 직업 $j$ 에서 능력 $i$ 의 요구 수준 (0-7 척도, 정규화)
- $\text{Importance}_{ij}$ : 직업 $j$ 에서 능력 $i$ 의 중요도 (1-5 척도, 정규화)
- $\beta_i$ : AI(Language Modeling)가 능력 $i$ 를 수행하는 정도 (0-1, MTurk 평가)

### 계산 단계

1. **정규화**: Level(0-7), Importance(1-5)를 [0, 1] 범위로 변환
2. **Scalar 계산**: $S_{ij} = \text{Level}_{ij} \times \text{Importance}_{ij}$
3. **가중 영향도**: $W_{ij} = S_{ij} \times \beta_i$
4. **직업별 집계**: $\text{AIOE}_j = \frac{\sum W_{ij}}{\sum S_{ij}}$ (52개 능력 합산)
5. **표준화**: Z-score 변환 → 평균 0, 표준편차 1

자세한 구현은 `02_AIOE_Calculation.ipynb` 참조

---

## 프로젝트 구조

```
aioe_proj/
├── README.md                              # 프로젝트 소개
├── index.html                             # 📊 인포그래픽 분석 보고서 (GitHub Pages)
├── datas/
│   ├── raw/                               # 원본 데이터
│   │   ├── Abilities.xlsx                 # O*NET 직업별 능력 데이터 (894 직업 × 52 능력)
│   │   └── mturk_mapping_matrix.csv       # AI-능력 매핑 데이터 (10 AI × 52 능력)
│   └── processed/                         # 처리된 데이터
│       ├── preprocessed_data.csv          # 병합된 데이터
│       └── aioe_master.csv                # 최종 AIOE 점수 (894개 직업)
├── notebooks/                             # 📓 학습용 노트북
│   ├── 00_AIOE_Intro.ipynb                # 프로젝트 소개 및 배경
│   ├── 01_AIOE_Data_Preprocessing.ipynb   # 데이터 전처리
│   ├── 02_AIOE_Calculation.ipynb          # AIOE 점수 계산
│   ├── 03_AIOE_EDA.ipynb                  # 탐색적 데이터 분석
│   └── 04_AIOE_Outro.ipynb                # 결론 및 다음 단계
└── notebooks_practice/                    # 🏃 실습용 노트북 (답안 제거)
    ├── 01_AIOE_Data_Preprocessing_Practice.ipynb
    ├── 02_AIOE_Calculation_Practice.ipynb
    └── 03_AIOE_EDA_Practice.ipynb
```

---

## 시작하기

### 📊 분석 결과 먼저 보기

**[인포그래픽 보고서 바로가기](https://oel05.github.io/aioe-analysis/)** ← 프로젝트 결과를 한눈에 확인하세요!

### 📓 학습하기

#### Google Colab (추천)

1. **Google Drive에 업로드**
   - `aioe_proj` 폴더를 Google Drive **메인 화면**에 업로드
   - 경로: `내 드라이브/aioe_proj`

2. **노트북 열기**
   - Google Drive에서 `notebooks/` 폴더의 `.ipynb` 파일 우클릭
   - `연결 앱` → `Google Colaboratory` 선택

3. **순서대로 실행**
   - 00_AIOE_Intro.ipynb (소개)
   - 01_AIOE_Data_Preprocessing.ipynb (전처리)
   - 02_AIOE_Calculation.ipynb (계산)
   - 03_AIOE_EDA.ipynb (분석)
   - 04_AIOE_Outro.ipynb (결론)

4. **실습하기 (선택)**
   - `notebooks_practice/` 폴더의 연습 노트북으로 직접 코딩해보기

#### 로컬 환경

```bash
# 1. 저장소 클론
git clone https://github.com/oel05/aioe-analysis.git
cd aioe-analysis

# 2. 가상환경 생성 및 활성화
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 3. 패키지 설치
pip install pandas numpy scipy matplotlib seaborn openpyxl jupyter koreanize_matplotlib

# 4. Jupyter 실행
jupyter notebook

# 5. notebooks/ 폴더에서 노트북 순서대로 실행
#    00 → 01 → 02 → 03 → 04
```

---

## 참고 자료

### 주요 논문
- **Felten, E., Raj, M., & Seamans, R. (2021).** Occupational, industry, and geographic exposure to artificial intelligence: A novel dataset and its potential uses. *Strategic Management Journal*, 42(12), 2195-2217. [DOI](https://doi.org/10.1002/smj.3286)

- Eloundou, T., Manning, S., Mishkin, P., & Rock, D. (2023). GPTs are GPTs: An early look at the labor market impact potential of large language models. *arXiv preprint* arXiv:2303.10130. [Link](https://arxiv.org/abs/2303.10130)

### 데이터 출처
- [O*NET Database](https://www.onetcenter.org/) - 미국 노동부 직업 정보 시스템
- [O*NET Resource Center](https://www.onetcenter.org/database.html) - 데이터 다운로드 및 문서
- [AI Index](https://aiindex.stanford.edu/) - Stanford HAI AI 동향 보고서

### 추가 학습 자료
- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [Matplotlib Tutorials](https://matplotlib.org/stable/tutorials/index.html)
- [Google Colab Guide](https://colab.research.google.com/)

---

## 라이선스

### 데이터
- **O*NET Database**: Public Domain (미국 노동부)
- **MTurk Data**: Felten et al. (2021) 연구 데이터 활용

### 코드
- 본 프로젝트의 코드는 교육 목적으로 자유롭게 사용 가능합니다.
- 재사용 시 출처 표기를 권장합니다.

---

## 주요 결과

**🔗 [전체 분석 결과 보기](https://oel05.github.io/aioe-analysis/)**

### 핵심 발견

1. **화이트칼라가 AI 영향을 훨씬 더 많이 받음**
   - 화이트칼라(+0.67) vs 블루칼라(-0.92), **1.60 차이**

2. **직업군 극심한 양극화**
   - 법률직(+1.46) vs 건설/채굴(-1.38), **2.85 차이**

3. **과거와 정반대 패턴**
   - 산업혁명: 블루칼라 타격
   - AI 시대: 화이트칼라 타격

### AIOE Top 10 직업
1. 영어 및 문학 교수 (1.79)
2. 외국어 및 문학 교수 (1.75)
3. 역사학 교수 (1.75)
4. 법학 교수 (1.74)
5. 철학 및 종교학 교수 (1.73)
6. 텔레마케터 (1.72)
7. 사회학 교수 (1.70)
8. 정치학 교수 (1.70)
9. 형사사법학 교수 (1.69)
10. 사회복지학 교수 (1.68)

**공통점:** 언어/텍스트 중심, 고등교육, 글쓰기/분석

---

## 마치며

> **AIOE는 "위협"이 아닌 "이해"를 위한 도구입니다.**
>
> - 높은 AIOE = 직업이 사라진다 ❌
> - 높은 AIOE = AI와 협업할 기회가 많다 ✅
>
> AI는 우리의 생산성을 높이는 도구입니다.
> 중요한 것은 이 변화를 객관적으로 이해하고,
> 데이터 기반으로 전략적으로 준비하는 것입니다.

---

<div align="center">

**📊 [인포그래픽 보고서 보기](https://oel05.github.io/aioe-analysis/)**

*AI 시대를 살아가는 모든 이들에게*

**Made with ❤️ for Data-Driven Decision Making**

</div>
