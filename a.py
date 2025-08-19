# models.py

from pydantic import BaseModel, Field
from typing import List

class LegalAnalysisTemplate(BaseModel):
    """사용자의 법률 사연을 분석하여 구조화된 템플릿으로 변환합니다."""

    category_classification: str = Field(
        description="입력된 사연이 속하는 법률 카테고리 (예: 민법 – 재판상 이혼 사유 및 위자료 청구)"
    )

    legal_query_transformation: str = Field(
        description="사용자의 일상적인 질문을 공식적인 법률 용어로 변환한 질의"
    )

    basis_documents: List[str] = Field(
        description="법률적 판단의 근거가 되는 법 조항이나 판례 목록"
    )

    evidence_summary: List[str] = Field(
        description="사용자의 이야기에서 언급되거나, 일반적으로 필요한 증거 자료 목록"
    )

    answer_summary: str = Field(
        description="법률적 근거에 기반하여 사용자의 질문에 대한 핵심 내용을 요약한 답변"
    )
