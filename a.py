# fine_tuning_example.py

# 1. 학습용 데이터(JSONL)는 이런 형식으로 생성됩니다.
# AI의 답변(assistant)은 텍스트가 아니라, '어떤 도구를 호출했는지'에 대한 정보입니다.
"""
{"messages":}
]}
"""

# 2. 훈련된 모델을 사용하는 방법
from langchain_openai import ChatOpenAI
from models import PrecedentTemplate, StatuteTemplate

# 훈련이 완료된 우리만의 전문가 모델 ID
fine_tuned_model_id = "ft:gpt-3.5-turbo:my-org:multi-tool-legal-expert-v1"

# LangChain을 사용하여 모델과 우리가 정의한 '도구'들을 연결
llm = ChatOpenAI(model=fine_tuned_model_id)
llm_with_tools = llm.bind_tools()

# 새로운 사용자 질문
user_input = "근로기준법 23조에 대해 알려줘."

# 모델 호출
ai_msg = llm_with_tools.invoke(user_input)

# 모델이 어떤 도구를 호출했는지 확인
if ai_msg.tool_calls:
    for tool_call in ai_msg.tool_calls:
        print(f"AI가 선택한 도구: {tool_call['name']}")
        print(f"도구에 전달된 내용: {tool_call['args']}")
        # 출력 예시:
        # AI가 선택한 도구: StatuteTemplate
        # 도구에 전달된 내용: {'task_type': 'QA', 'article_number': '근로기준법 제23조', 'answer': '...'}
