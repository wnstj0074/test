# training_models.py

from pydantic import BaseModel, Field
from typing import List, Literal

# '판결문' 관련 작업을 위한 Pydantic 모델 (doc_class = 1)
class PrecedentTemplate(BaseModel):
    """판결문(Precedent) 데이터 검증용 템플릿"""
    task_type: Literal
    case_number: str
    summary_or_answer: str
    #... 판결문 템플릿의 나머지 필드들

# '법령' 관련 작업을 위한 Pydantic 모델 (doc_class = 2)
class StatuteTemplate(BaseModel):
    """법령(Statute) 데이터 검증용 템플릿"""
    task_type: Literal['QA']
    article_number: str
    answer: str
    #... 법령 템플릿의 나머지 필드들
