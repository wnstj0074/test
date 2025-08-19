# application_model.py

from pydantic import BaseModel, Field
from typing import List

class LegalAnalysisTemplate(BaseModel):
    """사용자의 법률 사연을 분석하여 구조화된 템플릿으로 변환합니다."""
    category_classification: str = Field(description="...")
    legal_query_transformation: str = Field(description="...")
    basis_documents: List[str] = Field(description="...")
    evidence_summary: List[str] = Field(description="...")
    answer_summary: str = Field(description="...")
