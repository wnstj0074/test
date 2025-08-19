# run_analysis.py

from analysis_engine import analyze_user_story

# 예시 1: 이혼 관련 사연
story_1 = "남편이 외도를 했는데, 제가 위자료를 받을 수 있나요? 카톡 증거랑 사진도 있어요."
analysis_result_1 = analyze_user_story(story_1)

if analysis_result_1:
    print("--- [예시 1] 이혼 사연 분석 결과 ---")
    # Pydantic 객체를 JSON으로 예쁘게 출력
    print(analysis_result_1.model_dump_json(indent=2, ensure_ascii=False))
