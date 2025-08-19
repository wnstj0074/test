# data_processor.py

import json
from training_models import PrecedentTemplate, StatuteTemplate

def process_raw_data_for_training(raw_data_list: List[dict]) -> List[dict]:
    validated_data =
    for item in raw_data_list:
        info = item.get('info', {})
        doc_class = info.get('doc_class')
        output_label = item.get('output_label', {})

        try:
            if doc_class == 1:
                PrecedentTemplate(**output_label) # 판결문 템플릿으로 검증
            elif doc_class == 2:
                StatuteTemplate(**output_label) # 법령 템플릿으로 검증
            #... 다른 doc_class에 대한 처리 추가...

            validated_data.append(item) # 검증 성공 시 데이터 추가
        except Exception as e:
            print(f"데이터 검증 실패: {item.get('id')}, 오류: {e}")

    return validated_data
