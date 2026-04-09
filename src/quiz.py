# dataclass는 데이터를 담는 클래스를 더 간단하게 만들 수 있게 도와줍니다.
from dataclasses import dataclass  # Quiz 클래스를 짧고 깔끔하게 정의하기 위해 가져옵니다.
# Any는 다양한 형태의 데이터를 받을 수 있음을 타입 힌트로 표현할 때 사용합니다.
from typing import Any  # JSON에서 읽어 온 여러 형태의 값을 다룰 수 있도록 가져옵니다.


@dataclass  # 아래 Quiz 클래스에 기본 생성자 등을 자동으로 만들어 주는 장식자입니다.
class Quiz:  # Quiz 클래스는 퀴즈 한 문제의 정보를 하나로 묶어 관리합니다.
    question: str  # question에는 문제 문장을 문자열로 저장합니다.
    choices: list[str]  # choices에는 4개의 선택지를 리스트 형태로 저장합니다.
    answer: int  # answer에는 정답 번호를 1부터 4 사이의 숫자로 저장합니다.

    def __post_init__(self) -> None:  # 객체가 만들어진 직후 데이터가 올바른지 확인하는 메서드입니다.
        self.question = self.question.strip()  # 문제 문장 앞뒤의 불필요한 공백을 제거합니다.
        self.choices = [str(choice).strip() for choice in self.choices]  # 모든 선택지를 문자열로 바꾸고 공백도 정리합니다.
        if self.question == "":  # 문제 문장이 비어 있으면 정상적인 퀴즈가 아니므로 검사합니다.
            raise ValueError("문제는 비어 있을 수 없습니다.")  # 잘못된 문제 데이터라는 사실을 오류로 알려 줍니다.
        if len(self.choices) != 4:  # 과제 요구사항에 따라 선택지는 반드시 4개여야 합니다.
            raise ValueError("선택지는 반드시 4개여야 합니다.")  # 선택지 개수가 잘못되었음을 오류로 알려 줍니다.
        for choice in self.choices:  # 선택지 하나하나가 비어 있지 않은지 차례대로 확인합니다.
            if choice == "":  # 비어 있는 선택지가 있으면 사용자가 문제를 풀 수 없으므로 검사합니다.
                raise ValueError("선택지는 비어 있을 수 없습니다.")  # 선택지에 빈 값이 있음을 오류로 알려 줍니다.
        if self.answer not in (1, 2, 3, 4):  # 정답 번호는 1부터 4까지만 허용하므로 범위를 검사합니다.
            raise ValueError("정답 번호는 1부터 4 사이여야 합니다.")  # 정답 번호가 범위를 벗어났음을 오류로 알려 줍니다.

    def display(self, number: int | None = None) -> None:  # 화면에 퀴즈 내용을 보기 좋게 출력하는 메서드입니다.
        if number is not None:  # 문제 번호를 함께 받았다면 몇 번째 문제인지 먼저 출력합니다.
            print(f"[문제 {number}]")  # 예를 들어 [문제 1] 같은 형식으로 표시합니다.
        print(self.question)  # 실제 문제 문장을 화면에 출력합니다.
        for index, choice in enumerate(self.choices, start=1):  # 선택지에 1번부터 번호를 붙여 하나씩 꺼냅니다.
            print(f"{index}. {choice}")  # 번호와 선택지 문장을 함께 출력합니다.    
        # 왜 enumerate를 권장? 코드 간결, 실수 방지( x = 1, ... x += 1 ) 
        # index = 1  # start=1 설정
        # for choice in self.choices:
        #   루프 몸체
        #    print(f"{index}: {choice}")
        #    index += 1  # 매 반복마다 인덱스를 직접 증가시킴

    def is_correct(self, user_answer: int) -> bool:  # 사용자가 고른 번호가 정답인지 확인하는 메서드입니다.
        return user_answer == self.answer  # 사용자의 입력값과 정답 번호가 같으면 True를 반환합니다.

    def get_correct_choice_text(self) -> str:  # 정답 번호에 해당하는 실제 선택지 문장을 돌려주는 메서드입니다.
        return self.choices[self.answer - 1]  # 리스트는 0부터 시작하므로 answer에서 1을 빼서 찾습니다.

    def to_dict(self) -> dict[str, Any]:  # Quiz 객체를 JSON으로 저장하기 쉬운 딕셔너리 형태로 바꿉니다.
        return {  # 아래 중괄호 안에 저장할 데이터 구조를 만듭니다.
            "question": self.question,  # 문제 문장을 question 키로 저장합니다.
            "choices": list(self.choices),  # 선택지 리스트를 choices 키로 복사해 저장합니다.
            "answer": self.answer,  
        }  # 완성된 딕셔너리를 반환합니다.

    @classmethod  # 클래스 메서드는 객체가 없어도 클래스 이름으로 호출할 수 있는 메서드입니다.
    def from_dict(cls, data: dict[str, Any]) -> "Quiz":  # 딕셔너리 데이터를 Quiz 객체로 바꾸는 메서드입니다.
        if not isinstance(data, dict):  # 전달받은 값이 딕셔너리가 아니면 정상적인 퀴즈 데이터가 아닙니다.
            raise ValueError("퀴즈 데이터는 딕셔너리여야 합니다.")  # 데이터 형식이 잘못되었음을 오류로 알려 줍니다.
        question = str(data.get("question", "")).strip()  # question 키에서 문제 문장을 가져오고 문자열로 정리합니다.
        raw_choices = data.get("choices", [])  # choices 키에서 선택지 목록을 가져오고 없으면 빈 리스트를 사용합니다.
        if not isinstance(raw_choices, list):  # 선택지 데이터가 리스트가 아니면 잘못된 형식입니다.
            raise ValueError("choices 값은 리스트여야 합니다.")  # 선택지 형식 오류를 알려 줍니다.
        choices = [str(choice).strip() for choice in raw_choices]  # 선택지 하나하나를 문자열로 바꾸고 공백을 정리합니다.
        answer = int(data.get("answer", 0))  # answer 키에서 정답 번호를 가져와 정수로 변환합니다.
        return cls(question=question, choices=choices, answer=answer)  # 정리된 값들로 새 Quiz 객체를 만들어 반환합니다.
