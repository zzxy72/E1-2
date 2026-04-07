# QuizGame 클래스를 가져와서 메인 파일에서 게임을 실행할 수 있게 준비합니다.
from quiz_game import QuizGame  # quiz_game.py에 들어 있는 QuizGame 클래스를 사용합니다.


def main() -> None:  # main 함수는 프로그램이 시작될 때 가장 먼저 실행할 내용을 모아 둡니다.
    game = QuizGame()  # QuizGame 객체를 만들어 게임에 필요한 데이터와 기능을 준비합니다.
    game.run()  # 준비된 게임 객체의 run 메서드를 호출해 실제 게임을 시작합니다.


if __name__ == "__main__":  # 이 파일을 직접 실행했을 때만 아래 코드를 실행하겠다는 뜻입니다.
    main()  # main 함수를 호출해 프로그램 실행을 시작합니다.
