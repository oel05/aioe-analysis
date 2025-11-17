#!/usr/bin/env python3
"""
Create practice versions of AIOE notebooks by replacing solution code with TODOs
"""

import json
import sys

def create_practice_notebook_01(input_path, output_path):
    """Create practice version of 01_AIOE_Data_Preprocessing.ipynb"""

    with open(input_path, 'r', encoding='utf-8') as f:
        nb = json.load(f)

    # Define which cells to replace with practice exercises
    practice_cells = {
        '4': {
            'source': [
                "# TODO: Language Modeling 응용 프로그램의 Beta 값을 추출하세요\n",
                "#\n",
                "# 힌트 1: mturk 데이터프레임에서 applications 컬럼이 'language modeling'인 행을 필터링\n",
                "# 힌트 2: iloc[0, 2:]를 사용하여 첫 번째 행의 3번째 컬럼부터 끝까지 선택\n",
                "# 힌트 3: .to_dict()로 딕셔너리로 변환\n",
                "#\n",
                "# 변수명: lang_model_row, beta_values\n",
                "\n",
                "# 여기에 코드를 작성하세요\n",
                "\n"
            ]
        },
        '7': {
            'source': [
                "# TODO: Importance (IM)와 Level (LV) 데이터를 분리하세요\n",
                "#\n",
                "# 힌트 1: onet_abil 데이터프레임에서 'Scale ID' 컬럼이 'IM'인 행만 필터링\n",
                "# 힌트 2: .copy()를 사용하여 복사본 만들기\n",
                "# 힌트 3: Level도 동일한 방법으로 'LV' 필터링\n",
                "#\n",
                "# 변수명: onet_abil_im, onet_abil_lv\n",
                "\n",
                "# 여기에 코드를 작성하세요\n",
                "\n"
            ]
        },
        '9': {
            'source': [
                "# TODO: 능력명을 통일하는 함수를 만들고 적용하세요\n",
                "#\n",
                "# 힌트 1: 함수는 문자열을 입력받아 소문자로 변환하고 공백/하이픈/언더스코어 제거\n",
                "# 힌트 2: .lower(), .replace(' ', ''), .replace('-', ''), .replace('_', '') 사용\n",
                "# 힌트 3: .apply() 메서드로 'Element Name' 컬럼에 함수 적용\n",
                "#\n",
                "# 함수명: unify_ability_name\n",
                "# 새 컬럼명: abil_unified\n",
                "\n",
                "# 여기에 코드를 작성하세요\n",
                "\n"
            ]
        },
        '3y6a69zvnmp': {
            'source': [
                "# TODO: Importance와 Level 데이터를 병합하세요\n",
                "#\n",
                "# 힌트 1: onet_abil_im.merge() 사용\n",
                "# 힌트 2: onet_abil_lv에서 'O*NET-SOC Code', 'Element Name', 'Data Value' 컬럼만 선택\n",
                "# 힌트 3: on=['O*NET-SOC Code', 'Element Name']로 조인 키 지정\n",
                "# 힌트 4: suffixes=('_importance', '_level')로 컬럼명 구분\n",
                "# 힌트 5: how='inner'로 내부 조인\n",
                "#\n",
                "# 변수명: onet_merged\n",
                "\n",
                "# 여기에 코드를 작성하세요\n",
                "\n"
            ]
        },
        '14': {
            'source': [
                "# TODO: Beta 값을 추가하세요\n",
                "#\n",
                "# 힌트 1: onet_merged의 'abil_unified' 컬럼에 .map() 메서드 사용\n",
                "# 힌트 2: beta_values 딕셔너리를 map의 인자로 전달\n",
                "# 힌트 3: 결과를 'beta'라는 새 컬럼에 저장\n",
                "#\n",
                "# 새 컬럼명: beta\n",
                "\n",
                "# 여기에 코드를 작성하세요\n",
                "\n"
            ]
        }
    }

    # Replace specified cells
    for cell in nb['cells']:
        cell_id = cell.get('id', '')
        if cell_id in practice_cells:
            cell['source'] = practice_cells[cell_id]['source']
            # Remove outputs if present
            if 'outputs' in cell:
                cell['outputs'] = []
            if 'execution_count' in cell:
                cell['execution_count'] = None

    # Save practice notebook
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(nb, f, ensure_ascii=False, indent=1)

    print(f"✅ Created: {output_path}")


def create_practice_notebook_02(input_path, output_path):
    """Create practice version of 02_AIOE_Calculation.ipynb"""

    with open(input_path, 'r', encoding='utf-8') as f:
        nb = json.load(f)

    practice_cells = {
        '8': {
            'source': [
                "# TODO: Importance와 Level을 0-1 범위로 정규화하세요\n",
                "#\n",
                "# 힌트 1: Importance는 1-5 척도이므로 5로 나누기\n",
                "# 힌트 2: Level은 0-7 척도이므로 7로 나누기\n",
                "# 힌트 3: 새 컬럼명은 scale_importance, scale_level\n",
                "#\n",
                "# 새 컬럼명: scale_importance, scale_level\n",
                "\n",
                "# 여기에 코드를 작성하세요\n",
                "\n"
            ]
        },
        '10': {
            'source': [
                "# TODO: Scalar를 계산하세요 (능력 가중치)\n",
                "#\n",
                "# 힌트: Scalar = scale_level × scale_importance\n",
                "#\n",
                "# 새 컬럼명: scalar\n",
                "\n",
                "# 여기에 코드를 작성하세요\n",
                "\n"
            ]
        },
        '12': {
            'source': [
                "# TODO: 가중 영향도를 계산하세요\n",
                "#\n",
                "# 힌트: 가중 영향도 = scalar × beta\n",
                "#\n",
                "# 새 컬럼명: wtd_element_impact\n",
                "\n",
                "# 여기에 코드를 작성하세요\n",
                "\n"
            ]
        },
        '14': {
            'source': [
                "# TODO: 직업별로 집계하고 AIOE 기본 점수를 계산하세요\n",
                "#\n",
                "# 힌트 1: df.groupby(['soc_code', 'title']) 사용\n",
                "# 힌트 2: .agg()로 집계 - wtd_element_impact는 sum, scalar도 sum, ability는 count\n",
                "# 힌트 3: .reset_index()로 인덱스 리셋\n",
                "# 힌트 4: 새 컬럼명: total_weighted_impact, ability_base, n_abilities\n",
                "#\n",
                "# 변수명: results_df\n",
                "\n",
                "# 여기에 코드를 작성하세요\n",
                "\n"
            ]
        },
        'b63570e1': {
            'source': [
                "# TODO: AIOE 기본 점수를 계산하세요\n",
                "#\n",
                "# 힌트: ability_base_impact = total_weighted_impact ÷ ability_base\n",
                "#\n",
                "# 새 컬럼명: ability_base_impact\n",
                "\n",
                "# 여기에 코드를 작성하세요\n",
                "\n"
            ]
        },
        '16': {
            'source': [
                "# TODO: Z-score로 표준화하고 순위를 계산하세요\n",
                "#\n",
                "# 힌트 1: stats.zscore()를 ability_base_impact에 적용\n",
                "# 힌트 2: .rank(ascending=False, method='min')로 순위 계산\n",
                "# 힌트 3: .astype(int)로 정수형 변환\n",
                "#\n",
                "# 새 컬럼명: aioe, rank\n",
                "\n",
                "# 여기에 코드를 작성하세요\n",
                "\n"
            ]
        }
    }

    # Replace specified cells
    for cell in nb['cells']:
        cell_id = cell.get('id', '')
        if cell_id in practice_cells:
            cell['source'] = practice_cells[cell_id]['source']
            if 'outputs' in cell:
                cell['outputs'] = []
            if 'execution_count' in cell:
                cell['execution_count'] = None

    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(nb, f, ensure_ascii=False, indent=1)

    print(f"✅ Created: {output_path}")


def create_practice_notebook_03(input_path, output_path):
    """Create practice version of 03_AIOE_EDA.ipynb"""

    with open(input_path, 'r', encoding='utf-8') as f:
        nb = json.load(f)

    practice_cells = {
        'cell-9': {
            'source': [
                "# TODO: AIOE 분포를 시각화하세요\n",
                "#\n",
                "# 힌트 1: fig, axes = plt.subplots(1, 2, figsize=(14, 5))로 서브플롯 생성\n",
                "# 힌트 2: 왼쪽(axes[0]): 히스토그램 - axes[0].hist(df['aioe'], bins=30)\n",
                "# 힌트 3: 오른쪽(axes[1]): 박스플롯 - axes[1].boxplot(df['aioe'])\n",
                "# 힌트 4: plt.tight_layout(), plt.show() 호출\n",
                "\n",
                "# 여기에 코드를 작성하세요\n",
                "\n"
            ]
        },
        'cell-16': {
            'source': [
                "# TODO: SOC 대분류를 추출하고 한글 이름을 매핑하세요\n",
                "#\n",
                "# 힌트 1: df['soc_code'].str[:2]로 앞 2자리 추출\n",
                "# 힌트 2: .map(soc_major_names)로 한글 이름 매핑\n",
                "# 힌트 3: 새 컬럼명: soc_major, soc_major_name\n",
                "\n",
                "# 여기에 코드를 작성하세요\n",
                "\n"
            ]
        },
        'cell-17': {
            'source': [
                "# TODO: 직업군별 통계를 계산하세요\n",
                "#\n",
                "# 힌트 1: df.groupby('soc_major_name')['aioe'] 사용\n",
                "# 힌트 2: .agg(['count', 'mean', 'std'])로 집계\n",
                "# 힌트 3: .sort_values('mean', ascending=False)로 정렬\n",
                "#\n",
                "# 변수명: major_stats\n",
                "\n",
                "# 여기에 코드를 작성하세요\n",
                "\n"
            ]
        },
        'cell-20': {
            'source': [
                "# TODO: 직업군별 평균 AIOE를 막대 그래프로 시각화하세요\n",
                "#\n",
                "# 힌트 1: plt.figure(figsize=(12, 8))로 그림 크기 설정\n",
                "# 힌트 2: plt.barh()로 가로 막대 그래프 생성\n",
                "# 힌트 3: 양수는 빨강, 음수는 청록색으로 색상 지정\n",
                "# 힌트 4: plt.axvline(0)으로 기준선 추가\n",
                "\n",
                "# 여기에 코드를 작성하세요\n",
                "\n"
            ]
        }
    }

    # Replace specified cells
    for cell in nb['cells']:
        cell_id = cell.get('id', '')
        if cell_id in practice_cells:
            cell['source'] = practice_cells[cell_id]['source']
            if 'outputs' in cell:
                cell['outputs'] = []
            if 'execution_count' in cell:
                cell['execution_count'] = None

    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(nb, f, ensure_ascii=False, indent=1)

    print(f"✅ Created: {output_path}")


if __name__ == '__main__':
    base_path = '/Users/yongha-m3/dev_ws/project/aioe_proj'

    # Create practice notebooks
    create_practice_notebook_01(
        f'{base_path}/notebooks/01_AIOE_Data_Preprocessing.ipynb',
        f'{base_path}/notebooks_실습용/01_AIOE_Data_Preprocessing_Practice.ipynb'
    )

    create_practice_notebook_02(
        f'{base_path}/notebooks/02_AIOE_Calculation.ipynb',
        f'{base_path}/notebooks_실습용/02_AIOE_Calculation_Practice.ipynb'
    )

    create_practice_notebook_03(
        f'{base_path}/notebooks/03_AIOE_EDA.ipynb',
        f'{base_path}/notebooks_실습용/03_AIOE_EDA_Practice.ipynb'
    )

    print("\n✅ All practice notebooks created successfully!")
