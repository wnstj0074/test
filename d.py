# analysis_engine.py

from langchain_nvidia_ai_endpoints import ChatNVIDIA
from application_model import LegalAnalysisTemplate

def analyze_user_story(story: str) -> LegalAnalysisTemplate | None:
    """사용자의 사연을 분석하여 구조화된 LegalAnalysisTemplate 객체를 반환합니다."""
    # 1. 로컬에서 서비스 중인 '미세조정된' 모델을 지정합니다.
    llm = ChatNVIDIA(model="our_finetuned_legal_expert_v1")

    # 2. 최종 목표 템플릿을 LLM이 사용할 '도구'로 바인딩합니다.
    structured_llm = llm.with_structured_output(LegalAnalysisTemplate)

    # 3. 시스템 프롬프트를 통해 AI의 역할과 임무를 명확히 부여합니다.
    prompt = f"""
    당신은 유능한 법률 보조원입니다. 사용자의 법률 사연을 듣고 변호사를 위해 핵심 내용을 명확하게 정리해야 합니다.
    사연에서 법적으로 중요한 사실, 사건, 증거, 핵심 질문을 추출하여 제공된 LegalAnalysisTemplate 형식에 맞춰 구조화된 답변을 생성하세요.
    ---
    사용자 사연: "{story}"
    ---
    """
    try:
        result = structured_llm.invoke(prompt)
        return result
    except Exception as e:
        print(f"LLM 호출 또는 파싱 중 오류 발생: {e}")
        return None
