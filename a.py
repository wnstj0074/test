# pydantic_example.py

from pydantic import BaseModel, ValidationError
from typing import List

# Pydantic 모델(클래스)은 우리 데이터의 '설계도' 역할을 합니다.
class User(BaseModel):
    user_id: int
    name: str
    interests: List[str]

# 1. 정상적인 데이터가 들어올 경우
user_data_1 = {"user_id": 123, "name": "김철수", "interests": ["코딩", "독서"]}
user_object_1 = User(**user_data_1)
print(f"정상 데이터: {user_object_1}")

# 2. 타입이 틀렸지만, 변환 가능한 데이터가 들어올 경우
user_data_2 = {"user_id": "456", "name": "이영희", "interests": ["운동"]}
user_object_2 = User(**user_data_2)
# Pydantic이 자동으로 'user_id'를 문자열 "456"에서 정수 456으로 변환하고 검증합니다.
print(f"타입 변환 데이터의 ID: {user_object_2.user_id}")

# 3. 규칙에 맞지 않는 데이터가 들어올 경우
user_data_3 = {"user_id": "abc", "name": "박민준"} # 'interests' 필드 누락
try:
    User(**user_data_3)
except ValidationError as e:
    # Pydantic이 명확한 오류 메시지를 생성합니다.
    print(f"\n오류 발생 데이터:\n{e}")
