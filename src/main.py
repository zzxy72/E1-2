# QuizGame 클래스를 가져와서 게임을 실행할 수 있게 준비.
from quiz_game import QuizGame  # quiz_game.py에 들어 있는 QuizGame 클래스를 사용합니다.


def main() -> None:  # 리턴값 없음..
    game = QuizGame()  # QuizGame 객체를 만듭니다.
    game.run()  # 준비된 게임 객체의 run 메서드를 호출해 시작.

# 파일명이 무엇이든 python 파일명.py로 직접 실행하면 __name__은 "__main__"이 되고, 
# 이 조건이 참일 때 아래에서 호출한 함수가 실행된다.
if __name__ == "__main__":      
    main() 
