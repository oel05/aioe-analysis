# ChatGPT와 언어 모델링이 직업 및 산업에 미치는 영향

## 논문 정보
- **제목**: How will Language Modelers like ChatGPT Affect Occupations and Industries?
- **저자**: Ed Felten (Princeton), Manav Raj (University of Pennsylvania), Robert Seamans (New York University)
- **발행일**: 2023년 3월 18일
- **키워드**: artificial intelligence, ChatGPT, language modeling, occupation, technology

---

## 연구 개요

### 연구 배경
- ChatGPT(2022년 말 출시)를 비롯한 AI 언어 모델링 기술의 급격한 발전
- 언어 모델이 경제와 노동 시장에 미치는 영향에 대한 관심 증가
- Microsoft의 OpenAI에 100억 달러 투자, Google의 Bard 공개 등 기업들의 적극적 대응

### 연구 목적
직업, 산업, 지역이 AI 언어 모델링 기술 발전에 얼마나 노출되어 있는지 체계적으로 평가

---

## 연구 방법론

### AIOE (AI Occupational Exposure) 측정 방식

#### 1. 기본 구조
- **데이터 소스**:
  - AI 응용 분야: Electronic Frontier Foundation (EFF) 데이터
  - 인간 능력: O*NET 데이터베이스 (미국 노동부)
- **분석 대상**:
  - 10개 AI 응용 분야
  - 52개 인간 능력
  - 800개 이상의 직업

#### 2. 언어 모델링 특화 조정
원래 AIOE는 10개 AI 응용 분야에 동일한 가중치를 부여했으나, 이 연구에서는:
- **언어 모델링만 가중치 1 부여**
- 나머지 9개 응용 분야는 가중치 0

#### 3. 계산 공식

**능력 수준 노출도 계산:**
```
A_ij = Σ(α_i × x_ij)
```
- i: AI 응용 분야 인덱스
- j: 직업 능력 인덱스
- α_i: 각 AI 응용 분야의 가중치
- x_ij: 응용 분야와 능력 간 관련성 점수

**직업별 AIOE 계산:**
```
AIOE_k = Σ(A_ij × L_jk × I_jk) / Σ(L_jk × I_jk)
```
- k: 직업 인덱스
- L_jk: 직업 내 능력의 보편성 (prevalence)
- I_jk: 직업 내 능력의 중요도 (importance)

---

## 주요 연구 결과

### 1. 언어 모델링에 가장 노출된 직업 TOP 20

| 순위 | 직업명 | AIOE 점수 |
|------|--------|-----------|
| 1 | Telemarketers (텔레마케터) | 1.926 |
| 2 | English Language and Literature Teachers, Postsecondary (대학 영어/문학 교수) | 1.857 |
| 3 | Foreign Language and Literature Teachers, Postsecondary (대학 외국어/문학 교수) | 1.814 |
| 4 | History Teachers, Postsecondary (대학 역사 교수) | 1.813 |
| 5 | Law Teachers, Postsecondary (대학 법학 교수) | 1.802 |
| 6 | Philosophy and Religion Teachers, Postsecondary (대학 철학/종교 교수) | 1.800 |
| 7 | Sociology Teachers, Postsecondary (대학 사회학 교수) | 1.770 |
| 8 | Political Science Teachers, Postsecondary (대학 정치학 교수) | 1.770 |
| 9 | Criminal Justice and Law Enforcement Teachers, Postsecondary (대학 형사사법 교수) | 1.754 |
| 10 | Sociologists (사회학자) | 1.747 |
| 11 | Social Work Teachers, Postsecondary (대학 사회복지 교수) | 1.739 |
| 12 | Psychology Teachers, Postsecondary (대학 심리학 교수) | 1.716 |
| 13 | Communications Teachers, Postsecondary (대학 커뮤니케이션 교수) | 1.702 |
| 14 | Political Scientists (정치학자) | 1.687 |
| 15 | Area, Ethnic, and Cultural Studies Teachers, Postsecondary (대학 지역/문화 연구 교수) | 1.669 |
| 16 | Arbitrators, Mediators, and Conciliators (중재자, 조정자) | 1.647 |
| 17 | Judges, Magistrate Judges, and Magistrates (판사, 치안판사) | 1.646 |
| 18 | Geography Teachers, Postsecondary (대학 지리학 교수) | 1.629 |
| 19 | Library Science Teachers, Postsecondary (대학 도서관학 교수) | 1.626 |
| 20 | Clinical, Counseling, and School Psychologists (임상/상담/학교 심리학자) | 1.626 |

### 2. 언어 모델링에 가장 노출된 산업 TOP 20

| 순위 | 산업명 | 특징 |
|------|--------|------|
| 1 | Legal Services (법률 서비스) | 문서 작성, 법률 리서치 |
| 2 | Securities, Commodity Contracts, and Other Financial Investments (증권, 상품 및 금융 투자) | 분석 보고서, 투자 자문 |
| 3 | Agencies, Brokerages, and Other Insurance Related Activities (보험 중개 및 관련 활동) | 보험 상담, 문서 처리 |
| 4 | Insurance and Employee Benefit Funds (보험 및 복리후생 기금) | 고객 커뮤니케이션 |
| 5 | Nondepository Credit Intermediation (비예금 신용 중개) | 신용 평가, 대출 심사 |
| 6 | Agents and Managers for Artists, Athletes, Entertainers, and Other Public Figures (에이전트 및 매니저) | 계약 협상, 홍보 |
| 7 | Insurance Carriers (보험사) | 보험금 청구 처리 |
| 8 | Other Investment Pools and Funds (기타 투자 풀 및 펀드) | 투자 전략 분석 |
| 9 | Accounting, Tax Preparation, Bookkeeping, and Payroll Services (회계, 세무, 급여 서비스) | 재무 보고, 세무 자문 |
| 10 | Business Support Services (비즈니스 지원 서비스) | 고객 서비스, 문서 관리 |

### 3. 원래 AIOE와 언어 모델링 AIOE 비교

#### 상관관계
- **상관계수: 0.979** (매우 높은 상관관계)
- 대부분의 직업에서 비슷한 패턴을 보이지만, 특정 직업군에서 차이 발생

#### 주요 차이점
- **교육 분야**: 언어 모델링 AIOE에서 순위가 크게 상승
- **고등교육 인접 산업**: Junior colleges, Grantmaking services 등이 상위권 진입
- **기술직**: 원래 AIOE에서는 높았으나 언어 모델링에서는 상대적으로 낮음

### 4. 임금과의 관계

#### 주요 발견
- **임금이 높은 직업일수록 언어 모델링 노출도가 높음**
- 평균 임금과 중위 임금 모두에서 강한 양의 상관관계 확인
- 이는 기존 자동화 기술과 다른 패턴:
  - 과거: 저임금 육체노동이 주로 영향
  - 현재: 고임금 지식노동이 더 큰 영향

#### 그래프 분석
- 직업을 AIOE 점수로 20개 구간으로 나눔
- AIOE 점수 증가 → 평균/중위 임금 증가 (선형 관계)
- 고숙련 화이트칼라 직업이 주로 영향받음

---

## 핵심 발견 및 시사점

### 1. 교육 분야에 대한 영향

#### ChatGPT와 교육의 관계
- **과제 부여 방식 변화**: 에세이, 리포트 등 전통적 과제의 재검토 필요
- **부정행위 감지**: AI 작성 텍스트 판별의 어려움
- **교재 개발 지원**: 교수들이 AI를 활용한 교재 및 강의 자료 제작
- **개인화 교육**: 학생별 맞춤형 피드백 및 학습 지원

#### 대학 교수직의 노출도
- 인문학 교수(영어, 외국어, 역사, 철학) → 가장 높은 노출도
- 사회과학 교수(사회학, 정치학, 심리학) → 높은 노출도
- 이공계 교수 → 상대적으로 낮은 노출도

### 2. 텔레마케터 직업의 높은 노출도

#### 두 가지 가능한 시나리오

**시나리오 1: 보완(Augmentation)**
- 고객 응답을 실시간으로 언어 모델에 입력
- AI가 맞춤형 응답 제안
- 텔레마케터의 생산성 향상

**시나리오 2: 대체(Substitution)**
- AI 기반 음성 봇이 텔레마케팅 수행
- 인간 텔레마케터의 일자리 감소
- 완전 자동화된 고객 응대 시스템

### 3. 법률 및 금융 산업의 변화

#### 법률 서비스
- **계약서 검토 및 작성**: AI가 표준 계약서 초안 작성
- **법률 리서치**: 판례 및 법령 검색의 자동화
- **소송 문서 작성**: 소장, 답변서 등의 초안 생성

#### 금융 서비스
- **투자 보고서 작성**: 시장 분석 및 투자 권고안 생성
- **고객 상담**: 금융 상품 설명 및 자문
- **리스크 분석**: 신용 평가 및 위험 분석 보고서

### 4. 노동 시장에 대한 함의

#### 기존 자동화와의 차이
| 구분 | 기존 자동화 | AI 언어 모델링 |
|------|-------------|----------------|
| 영향 받는 직업 | 저숙련, 육체노동 | 고숙련, 지식노동 |
| 임금 수준 | 저임금 | 고임금 |
| 대체 방식 | 기계가 물리적 작업 대체 | AI가 인지적 작업 대체 |
| 주요 산업 | 제조업, 서비스업 | 전문직, 금융, 법률 |

#### 예상되는 변화
- **직업 재설계**: 많은 직업에서 업무 내용과 방식이 변화
- **기술 보완**: AI를 활용할 수 있는 능력이 중요해짐
- **새로운 직업**: AI 관련 새로운 직업군 등장 가능
- **소득 불평등**: 고임금 직업의 변화가 소득 분배에 미치는 영향

---

## 연구의 의의 및 한계

### 연구의 강점

#### 1. 체계적 방법론
- 주관적 판단이 아닌 데이터 기반 분석
- 재현 가능하고 검증 가능한 방법론
- GitHub에 코드 및 데이터 공개

#### 2. 유연성
- AI 기술 발전에 따라 가중치 조정 가능
- 다른 AI 응용 분야(예: 이미지 생성)에도 적용 가능
- 직업별, 산업별, 지역별 분석 모두 가능

#### 3. 정책적 활용
- 학자, 실무자, 정책입안자에게 유용한 정보 제공
- 노동 시장 정책 수립의 기초 자료
- 교육 및 재교육 프로그램 설계에 활용

### 연구의 한계

#### 1. 노출도 ≠ 실제 영향
- AIOE는 "노출도"만 측정
- 실제로 일자리가 줄어들지, 생산성이 높아질지는 미지수
- 대체(substitution)와 보완(augmentation) 구분 불가

#### 2. 시간적 제약
- 2023년 3월 시점의 기술 수준 반영
- AI 기술은 계속 발전 중
- 장기적 영향 예측의 어려움

#### 3. 지역적 한계
- 미국 O*NET 데이터 기반
- 다른 국가의 직업 구조는 다를 수 있음
- 문화적, 제도적 차이 미반영

#### 4. 간접 효과 미고려
- 직접적인 업무 노출도만 측정
- 산업 간 연쇄 효과 미포함
- 새로운 직업 창출 가능성 미반영

---

## 후속 연구 제안

### 1. 실증 연구
- 실제 기업에서 ChatGPT 도입 후 생산성 변화 측정
- 고용 변화 추적 연구
- 임금 변화 분석

### 2. 국제 비교 연구
- 다양한 국가의 직업 구조 비교
- 문화적, 제도적 차이가 미치는 영향
- 정책 대응 방안 비교

### 3. 장기 영향 연구
- AI 기술 발전에 따른 노출도 변화 추적
- 세대별 영향 분석
- 교육 시스템의 적응 과정 연구

### 4. 정책 연구
- 재교육 프로그램 설계
- 사회 안전망 강화 방안
- 윤리적, 법적 규제 방안

---

## 결론

### 핵심 메시지
1. **ChatGPT와 같은 언어 모델은 고임금 지식 노동자에게 더 큰 영향을 미칠 것**
2. **교육, 법률, 금융 분야가 특히 높은 노출도를 보임**
3. **기존 자동화 기술과는 다른 패턴의 노동 시장 변화 예상**
4. **"노출"이 반드시 일자리 감소를 의미하지는 않음 (보완 가능성도 존재)**

### 시사점
- **개인 차원**: AI 활용 능력 개발의 중요성
- **기업 차원**: AI 도입 전략 및 인력 재배치 계획 필요
- **정부 차원**: 재교육 프로그램 및 사회 안전망 강화
- **학계 차원**: 지속적인 모니터링 및 연구 필요

### 미래 전망
AI 언어 모델링 기술은 계속 발전하고 있으며, 그 영향은 더욱 확대될 것으로 예상됩니다. 이에 대한 체계적인 모니터링과 적절한 정책 대응이 필요한 시점입니다.

---

## 참고문헌

### 주요 관련 연구
- Felten, E., Raj, M., & Seamans, R. (2021). Occupational, industry, and geographic exposure to artificial intelligence: A novel dataset and its potential uses. *Strategic Management Journal*, 42(12), 2195-2217.
- Brynjolfsson, E., Mitchell, T., & Rock, D. (2018). What can machines learn, and what does it mean for occupations and the economy? *AEA Papers and Proceedings*, 108, 43-47.
- Frey, C. B., & Osborne, M. A. (2017). The future of employment: How susceptible are jobs to computerisation? *Technological Forecasting and Social Change*, 114, 254-280.

### 데이터 및 코드
- **논문 링크**: [Wiley Online Library](https://onlinelibrary.wiley.com/doi/full/10.1002/smj.3286)
- **GitHub 저장소**: [AIOE-Data/AIOE](https://github.com/AIOE-Data/AIOE)
- **O*NET 데이터베이스**: [www.onetcenter.org](https://www.onetcenter.org)
- **BLS 임금 데이터**: [www.bls.gov/oes](https://www.bls.gov/oes/)

---

*문서 작성일: 2025년 10월 23일*
*원본 논문 발행일: 2023년 3월 18일*
