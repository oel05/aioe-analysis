# AI Occupational Exposure (AIOE) 분석 프로젝트

<div align="center">

**"내 직업이 AI에 얼마나 노출될까?"**

*데이터로 답하는 AI 시대의 직업 전망*

[![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange.svg)](https://jupyter.org/)
[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-Educational-green.svg)]()

</div>

---

## 🎯 프로젝트 소개

ChatGPT, Claude, Gemini... AI가 우리 일상에 깊숙이 들어온 지금, 많은 사람들이 궁금해합니다:

> "AI가 내 직업을 대체하게 될까?"
> "어떤 직업이 AI의 영향을 많이 받을까?"
> "나는 어떤 능력을 개발해야 할까?"

이 프로젝트는 **Princeton University와 NYU의 연구진이 개발한 AIOE(AI Occupational Exposure) 방법론**을 활용하여, **894개 직업**이 **AI 기술(특히 언어 모델)**에 얼마나 노출되는지를 **데이터 기반으로 분석**합니다.

### 왜 이 분석이 필요한가?

- 📊 **객관적 지표**: 추측이나 의견이 아닌, 데이터에 기반한 측정
- 🔍 **직업별 세부 분석**: 894개 직업 각각의 AI 노출도 계산
- 💡 **능력 기반 접근**: 각 직업이 요구하는 52개 능력을 AI가 얼마나 잘 수행하는지 평가
- 🎓 **검증된 방법론**: Strategic Management Journal 게재 논문의 분석 방법 재현

---

## 📚 무엇을 배우나요?

이 프로젝트를 통해 다음을 경험할 수 있습니다:

### 1. 데이터 과학 실전 스킬
- 📂 **데이터 전처리**: 여러 출처의 데이터를 하나로 병합하고 정제
- 🧮 **복잡한 지표 계산**: 정규화, 가중 평균, Z-score 표준화
- 📊 **탐색적 데이터 분석**: 시각화를 통한 인사이트 도출

### 2. 실제 연구 논문 재현
- 📄 Felten et al. (2021) 논문의 방법론을 직접 구현
- 🔬 연구 방법의 이해와 한계 인식
- 📈 결과 해석과 비판적 사고

### 3. AI 시대에 대한 통찰
- 🤖 AI가 잘하는 것 vs 못하는 것
- 💼 직업의 미래와 변화 방향
- 🎯 개인의 커리어 전략 수립

---

## 📊 데이터 소개

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

## 🧮 AIOE는 어떻게 계산하나?

### 핵심 아이디어

```
AIOE = (AI가 도와줄 수 있는 능력들의 가중치 합) / (전체 능력의 가중치 합)
```

### 계산 과정

1. **정규화**: Importance(1-5)와 Level(0-7)을 0-1 범위로 변환
2. **Scalar 계산**: `Scalar = Normalized_Level × Normalized_Importance`
3. **가중 영향도**: `Weighted_Impact = Scalar × Beta` (AI가 잘하는 능력일수록 높음)
4. **직업별 집계**: 52개 능력의 가중 영향도를 합산
5. **표준화**: Z-score로 변환하여 상대적 위치 파악

자세한 수식과 코드는 `02_AIOE_Calculation.ipynb` 참조

---

## 📈 주요 결과 예시

### TOP 10 직업 (AI 노출도 높음)

| 순위 | 직업 | AIOE Z-score |
|------|------|--------------|
| 1 | Interpreters and Translators | 2.85 |
| 2 | Survey Researchers | 2.71 |
| 3 | Poets, Lyricists and Creative Writers | 2.43 |
| 4 | Sociologists | 2.35 |
| 5 | Animal Scientists | 2.32 |

### BOTTOM 10 직업 (AI 노출도 낮음)

| 순위 | 직업 | AIOE Z-score |
|------|------|--------------|
| 1 | Meat, Poultry, and Fish Cutters | -1.84 |
| 2 | Outdoor Power Equipment Operators | -1.76 |
| 3 | Dredge Operators | -1.73 |
| 4 | Slaughterers and Meat Packers | -1.68 |
| 5 | Fence Erectors | -1.67 |

*상세한 분석과 시각화는 `03_AIOE_EDA.ipynb` 참조*

---

## 💡 이 프로젝트의 의의

### 학술적 의의
- ✅ 실제 연구 논문(Strategic Management Journal 게재)의 방법론 재현
- ✅ 재현 가능한 투명한 분석 과정
- ✅ 데이터 기반 의사결정의 사례

### 교육적 의의
- 📚 실전 데이터 과학 프로젝트 경험
- 🧠 비판적 사고와 데이터 해석 능력 향상
- 💻 Python, Pandas, Matplotlib 실무 활용

### 사회적 의의
- 🌍 AI 시대의 직업 변화에 대한 객관적 이해
- 🎯 개인의 커리어 전략 수립에 도움
- 🤝 AI를 위협이 아닌 도구로 인식

---


## 🗂️ 프로젝트 구조

```
aioe_proj/
├── README.md                          # 프로젝트 소개
├── datas/
│   ├── raw/                           # 원본 데이터
│   │   ├── Abilities.xlsx             # O*NET 직업별 능력 데이터 (894 직업 × 52 능력)
│   │   └── mturk_mapping_matrix.csv   # AI-능력 매핑 데이터 (10 AI × 52 능력)
│   └── processed/                     # 처리된 데이터
│       ├── preprocessed_data.csv      # 병합된 데이터
│       └── aioe_master.csv            # 최종 AIOE 점수
└── notebooks/
    ├── 00_AIOE_Introduction.ipynb     # 프로젝트 소개 및 배경
    ├── 01_AIOE_Data_Preprocessing.ipynb  # 데이터 전처리
    ├── 02_AIOE_Calculation.ipynb      # AIOE 점수 계산
    ├── 03_AIOE_EDA.ipynb              # 탐색적 데이터 분석
    └── 04_AIOE_Conclusion.ipynb       # 결론 및 인사이트
```

---

## 🚀 시작하기

### Google Colab (추천)

1. **Google Drive에 업로드**
   - `aioe_proj` 폴더를 Google Drive **메인 화면**에 업로드
   - 경로: `내 드라이브/aioe_proj`

2. **노트북 열기**
   - Google Drive에서 `.ipynb` 파일 우클릭
   - `연결 앱` → `Google Colaboratory` 선택

3. **순서대로 실행**
   - 00 → 01 → 02 → 03 → 04 순서로 실행

### 로컬 환경

```bash
# 1. 저장소 클론
git clone https://github.com/your-username/aioe-analysis.git
cd aioe_proj

# 2. 가상환경 생성 및 활성화
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 3. 패키지 설치
pip install pandas numpy scipy matplotlib seaborn openpyxl jupyter koreanize_matplotlib

# 4. Jupyter 실행
jupyter notebook

# 5. notebooks/ 폴더에서 노트북 순서대로 실행
```

---

## 🔗 참고 자료

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

## 📝 라이선스

### 데이터
- **O*NET Database**: Public Domain (미국 노동부)
- **MTurk Data**: Felten et al. (2021) 연구 데이터 활용

### 코드
- 본 프로젝트의 코드는 교육 목적으로 자유롭게 사용 가능합니다.
- 재사용 시 출처 표기를 권장합니다.

---

## 📌 드리고 싶은 말씀

> **AIOE는 "위협"이 아닌 "이해"를 위한 도구입니다.**
>
> - ❌ 높은 AIOE = 직업이 사라진다 (X)
> - ✅ 높은 AIOE = AI와 협업할 기회가 많다 (O)
>
> AI는 우리의 생산성을 높이는 도구입니다.
> 중요한 것은 이 변화를 객관적으로 이해하고,
> 우리가 나아갈 방향을 함께 찾는 것입니다.

---

<div align="center">

**Made with 📊 Data & 💡 Insights**

*AI 시대를 살아가는 모든 이들에게*

</div>
