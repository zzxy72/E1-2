# json 모듈은 파이썬 데이터를 JSON 파일로 저장하거나 다시 읽어 올 때 사용합니다.
import json  # state.json 파일을 읽고 쓰기 위해 사용합니다.
from pathlib import Path  # 파일 경로를 객체처럼 다루기 위해 사용합니다.

# Quiz 클래스는 퀴즈 한 문제를 표현하므로 게임 전체에서 꼭 필요합니다.
from quiz import Quiz  # quiz.py에 정의한 Quiz 클래스를 가져옵니다.


# QuizGame 클래스는 메뉴, 점수, 저장 상태를 관리합니다.
class QuizGame: 
    # 주요 메서드:
    #  - run(): 메인 루프, 사용자 메뉴 입력과 기능 처리
    #  - play_quiz(): 퀴즈를 출제하고 채점 결과를 정리
    #  - add_quiz(): 사용자가 새 퀴즈를 추가
    #  - list_quizzes(): 현재 퀴즈 목록을 화면에 출력
    #  - show_best_score(): 최고 점수와 플레이 횟수 확인
    #  - save_state(): 현재 상태를 state.json에 저장
    #  - load_state(): state.json에서 이전 상태를 불러오기

    STATE_FILE = Path(__file__).resolve().parent / "state.json"  # src/state.json을 사용합니다.

    def __init__(self) -> None:  # 객체가 처음 만들어질 때 기본값과 저장 데이터를 준비합니다.
        self.quizzes: list[Quiz] = []  # 퀴즈 목록을 담을 빈 리스트를 먼저 준비합니다.
        self.best_score = 0  # 최고 점수는 처음에는 0점으로 시작합니다.
        self.play_count = 0  # 몇 번 플레이했는지 세는 값도 0으로 시작합니다.
        self.is_running = True  # 게임 루프를 계속 돌릴지 결정하는 값은 처음에 True입니다.
        self.load_state()  # 저장된 파일이 있으면 불러오고, 없으면 기본 퀴즈를 준비합니다.
# 5.기본 퀴즈 데이터 
    def get_default_quizzes(self) -> list[Quiz]:  # 파일이 없거나 손상되었을 때 사용할 기본 퀴즈를 만듭니다.
        return [  # 아래에 Quiz 객체 5개를 넣은 리스트를 반환합니다.
            Quiz(  
                question="Python에서 문자열 자료형의 이름은 무엇인가요?",  
                choices=["str", "int", "list", "bool"],  
                answer=1, 
            ),  
            Quiz(  
                question="if 문은 주로 어떤 상황에서 사용하나요?", 
                choices=["조건에 따라 다른 동작을 할 때", "무조건 같은 동작만 할 때", "파일만 읽을 때", "주석만 작성할 때"], 
                answer=1,  
            ),  
            Quiz(  
                question="list 자료형의 특징으로 가장 알맞은 것은 무엇인가요?", 
                choices=["순서가 있고 여러 값을 저장할 수 있다", "항상 숫자만 저장할 수 있다", "반드시 4개 값만 들어간다", "한 번 만들면 바꿀 수 없다"], 
                answer=1, 
            ), 
            Quiz( 
                question="for 문은 보통 무엇을 반복할 때 사용하나요?", 
                choices=["정해진 횟수나 목록을 차례대로 처리할 때", "컴퓨터를 종료할 때", "정답을 무조건 맞힐 때", "파일 이름을 바꿀 때만"], 
                answer=1, 
            ),  
            Quiz(  
                question="JSON 파일을 이 프로젝트에서 사용하는 가장 큰 이유는 무엇인가요?", 
                choices=["프로그램을 다시 실행해도 데이터를 남기기 위해", "화면 색을 바꾸기 위해", "파이썬 설치를 대신하기 위해", "키보드를 연결하기 위해"], 
                answer=1, 
            ),  
        ] 
############## 기본 퀴즈 데이터 끝 ######################

# state.json 파일 처리 관련.
    def build_state_data(self) -> dict[str, object]:  # 현재 게임 상태를 저장용 딕셔너리로 만드는 메서드입니다.
        return {  # 아래 구조가 state.json 
            "quizzes": [quiz.to_dict() for quiz in self.quizzes],  # 모든 Quiz 객체를 딕셔너리로 바꿔 quizzes 키에 담습니다.
            "best_score": self.best_score,  # 현재 최고 점수.
            "play_count": self.play_count,  # 총 플레이 횟수.
        } 

    def load_state(self) -> None:  # state.json 파일에서 저장된 데이터를 읽어 오는 메서드입니다.
        if not self.STATE_FILE.exists():  # 저장 파일이 아직 없다면.
            self.quizzes = self.get_default_quizzes()  # 기본 퀴즈 5개를 메모리에 준비합니다.
            self.best_score = 0  # 최고 점수, 플레이 기록 아직 없으므로 0으로 둡니다.
            self.play_count = 0  
            print("\n[안내] 저장 파일이 없어 기본 퀴즈로 시작합니다.")
            self.save_state()  # 바로 state.json 파일을 만들어 다음 실행에서도 사용할 수 있게 합니다.
            return 
        try:  # 파일 읽기 과정에서 생길 수 있는 오류를 안전하게 처리하기 위해 try를 시작.
            with self.STATE_FILE.open("r", encoding="utf-8") as file:  # UTF-8 방식으로 state.json 파일을 엽니다.
                data = json.load(file)  # 파일 안의 JSON 내용을 파이썬 딕셔너리로 읽어 옵니다.
            raw_quizzes = data.get("quizzes", [])  # quizzes 키에서 퀴즈 목록을 가져오고 없으면 빈 리스트를 사용합니다.
            if not isinstance(raw_quizzes, list):  
                raise ValueError("quizzes 값은 리스트여야 합니다.")  # 키는 있는데 데이터 형식이 잘못된 경우 (위험)
            self.quizzes = [Quiz.from_dict(item) for item in raw_quizzes]  # 읽어 온 각 퀴즈 딕셔너리를 Quiz 객체로 바꿉니다.
            self.best_score = int(data.get("best_score", 0))  
            self.play_count = int(data.get("play_count", 0))  
            if not self.quizzes:  # 파일은 있었지만 퀴즈가 하나도 없는 경우를 따로 처리합니다.
                print("\n[주의] 저장된 퀴즈가 없어 기본 퀴즈를 다시 준비합니다.")  # 기본 퀴즈로 복구함을 안내합니다.
                self.quizzes = self.get_default_quizzes()  # 기본 퀴즈를 다시 메모리에 채워 넣습니다.
                self.save_state()  # 복구된 내용을 다시 파일에 저장합니다.
                return  # 복구가 끝났으므로 메서드를 마칩니다.
            print(f"\n[안내] 저장된 데이터를 불러왔습니다. (퀴즈 {len(self.quizzes)}개, 최고 점수 {self.best_score}점)")  # 정상적으로 로드했음을 알려 줍니다.
        except (json.JSONDecodeError, OSError, TypeError, ValueError):  # 파일 손상이나 형식 오류 같은 문제를 한 번에 처리합니다.
            print("\n[주의] 저장 파일을 읽는 중 문제가 발생했습니다. 기본 퀴즈로 복구합니다.")  # 복구 메시지를 사용자에게 보여 줍니다.
            self.quizzes = self.get_default_quizzes()  # 문제가 생긴 경우에도 게임이 동작하도록 기본 퀴즈를 넣습니다.
            self.best_score = 0  # 잘못된 점수 데이터는 버리고 0부터 다시 시작합니다.
            self.play_count = 0  # 플레이 횟수도 0부터 다시 시작합니다.
            self.save_state()  # 복구된 내용을 state.json 파일에 다시 저장합니다.

    def save_state(self) -> None:  # 현재 게임 상태를 state.json 파일에 저장하는 메서드입니다.
        state_data = self.build_state_data()  # 먼저 저장할 데이터를 딕셔너리 형태로 정리합니다.
        try:  # 파일 저장 중 문제가 생겨도 프로그램이 갑자기 죽지 않도록 try를 사용합니다.
            with self.STATE_FILE.open("w", encoding="utf-8") as file:  # state.json 파일을 쓰기 모드와 UTF-8로 엽니다.
                json.dump(state_data, file, ensure_ascii=False, indent=4)  
                # 한글, 들여쓰기 4 설정.
        except OSError:  # 디스크 문제나 권한 문제처럼 파일 저장 실패 상황.
            print("\n[주의] state.json 파일 저장에 실패했습니다.")  
############## state.json 파일 처리 관련 끝 ##############

# 3. 공통 입력/예외 처리 기준
    def handle_input_interrupt(self) -> None:  # Ctrl+C나 EOF 입력처럼 입력이 중단되었을 때 
        print("\n[주의] 입력이 중단되었습니다. 현재 상태를 저장한 뒤 안전하게 종료합니다.")  
        self.save_state()  # 지금까지의 상태를 가능한 범위에서 파일에 저장합니다.
        self.is_running = False  # 게임 루프를 멈추도록 값을 False로 바꿉니다.

    ### 문자열 입력을 받을 때 사용하는 공통 메서드입니다.
    def get_non_empty_text(self, prompt_message: str) -> str | None:  
        while self.is_running:  # 게임이 실행 중인 동안에는 올바른 입력이 들어올 때까지 계속.
            try:  # input 함수에서 발생할 수 있는 예외를 안전하게 처리하기 위해 try를 사용합니다.
                user_input = input(prompt_message).strip()  # 입력을 받고 앞뒤 공백을 제거합니다.
            except (KeyboardInterrupt, EOFError):  # Ctrl+C나 EOF가 발생하면 이 블록으로 들어옵니다. (^D, Ctrl+Z 등)
                self.handle_input_interrupt()  # 안전 종료 처리.
                return None  # 더 이상 입력을 받을 수 없으므로 None을 반환.
            if user_input == "":  # 아무 글자도 입력하지 않고 엔터만 누른 경우를 검사합니다.
                print("[주의] 빈 입력은 사용할 수 없습니다. 다시 입력해 주세요.") 
                continue  # 올바른 값을 받을 때까지 다시 입력받습니다.
            return user_input  # 정상 문자열이면 바로 반환합니다.
        return None  # 게임이 종료 상태라면 None을 반환해 호출한 쪽이 멈출 수 있게 합니다.

    ### 일정 범위 안의 숫자 입력을 받을 때 사용하는 메서드입니다.
    def get_number_input(self, prompt_message: str, min_value: int, max_value: int) -> int | None:  
        while self.is_running:  # 게임이 실행 중인 동안에는 조건에 맞는 숫자가 들어올 때까지 반복합니다.
            text = self.get_non_empty_text(prompt_message)  # 문자열 입력을 공통 메서드로 받습니다.
            if text is None:  # 입력 중단 등으로 문자열을 받지 못했다면 종료 흐름으로 넘어갑니다.
                return None  # 숫자를 만들 수 없으므로 None을 반환합니다.
            try:  # 문자열을 숫자로 바꾸는 과정에서 오류가 날 수 있어 try를 사용합니다.
                number = int(text)  # 사용자가 입력한 문자열을 정수로 변환합니다.
            except ValueError:  # 예를 들어 abc 같은 글자를 넣으면 여기로 들어옵니다.
                print(f"[주의] 숫자를 입력해 주세요. 가능한 범위는 {min_value}부터 {max_value}까지입니다.") 
                continue  # 올바른 숫자를 다시 입력받기 위해 반복문의 처음으로 돌아갑니다.
            if number < min_value or number > max_value:  # 숫자이긴 하지만 허용 범위를 벗어난 경우를 검사합니다.
                print(f"[주의] 잘못된 입력입니다. {min_value}-{max_value} 사이의 숫자를 입력하세요.")
                continue  # 다시 입력받기 위해 반복합니다.
            return number  # 형식과 범위를 모두 통과한 숫자라면 반환합니다.
        return None  # None을 반환해 호출한 쪽이 멈출 수 있게 합니다.
############## 입력 처리 관련 끝 ##############

# 2. 메뉴 기능 관련
    def show_menu(self) -> None:  # 메인 메뉴 화면을 출력하는 메서드입니다.
        print("\n========================================") 
        print("         나만의 퀴즈 게임")  
        print("========================================") 
        print("1. 퀴즈 풀기") 
        print("2. 퀴즈 추가") 
        print("3. 퀴즈 목록") 
        print("4. 점수 확인")  
        print("5. 종료")  
        print("========================================") 

    def run(self) -> None:  # 프로그램 전체를 반복 실행하는 메인 루프 메서드입니다.
        print("\n[시작] 퀴즈 게임을 시작합니다.")  
        while self.is_running:  # 종료를 선택하기 전까지 메뉴를 계속 보여 주기 위해 반복.
            self.show_menu()  # 현재 사용할 수 있는 메뉴를 화면에 출력합니다.
            choice = self.get_number_input("선택: ", 1, 5)  # 메뉴 번호를 1부터 5 사이의 숫자로 입력.
            if choice is None:  # 입력 중단 등으로 메뉴 번호를 받지 못한 경우.
                continue  # while 조건이 False가 되면 루프가 끝나고, 아니면 다시 메뉴로 돌아갑니다.
            self.handle_menu_choice(choice)  # 사용자가 고른 번호에 맞는 기능을 실행합니다.

    def handle_menu_choice(self, choice: int) -> None:  # 메뉴 번호에 따라 어떤 기능을 실행할지 결정하는 메서드입니다.
        if choice == 1:  
            self.play_quiz()  # 퀴즈를 실제로 푸는 메서드를 호출합니다.
        elif choice == 2:  
            self.add_quiz()  # 새 퀴즈를 등록하는 메서드를 호출합니다.
        elif choice == 3: 
            self.list_quizzes()  # 현재 저장된 퀴즈 목록을 출력합니다.
        elif choice == 4:  
            self.show_best_score()  # 최고 점수와 플레이 횟수를 출력합니다.
        elif choice == 5: 
            self.exit_program()  # 저장 후 종료하는 메서드를 호출합니다.
###################### 메뉴 기능 관련 끝 ######################

# 6. 퀴즈 풀기
    def play_quiz(self) -> None:  # 저장된 퀴즈를 순서대로 출제하는 메서드입니다.
        if not self.quizzes:  # 퀴즈가 하나도 없으면 게임을 진행할 수 없으므로 먼저 검사합니다.
            print("\n[주의] 등록된 퀴즈가 없어 퀴즈를 시작할 수 없습니다.")  
            return 
        print(f"\n[퀴즈] 퀴즈를 시작합니다. (총 {len(self.quizzes)}문제)") 
        score = 0  # 이번 라운드에서 맞힌 문제 수를 저장할 변수를 0으로 시작합니다.
        for index, quiz in enumerate(self.quizzes, start=1):  # 퀴즈 목록을 앞에서부터 하나씩 꺼내며 번호도 함께 만듭니다.
            print("\n----------------------------------------")  
            quiz.display(index)  # 현재 문제 번호와 문제 내용을 화면에 출력합니다.
            answer = self.get_number_input("정답 입력 (1-4): ", 1, 4)  
            if answer is None:  # 입력 중단으로 답을 받지 못했다면 안전하게 현재 기능을 마칩니다.
                return  # 이후 처리는 하지 않고 메서드를 종료합니다.
            if quiz.is_correct(answer):  # 사용자의 답이 정답인지 확인합니다.
                score += 1  # 정답이라면 점수를 1 올립니다.
                print("[정답] 맞았습니다.")  
            else:  # 정답이 아닌 경우 이 블록이 실행됩니다.
                correct_text = quiz.get_correct_choice_text()  # 정답 번호에 해당하는 선택지 문장을 가져옵니다.
                print(f"[오답] 정답은 {quiz.answer}번: {correct_text}") 
        self.finish_round(score, len(self.quizzes))  # 모든 문제를 다 풀었다면 결과를 정리하고 저장합니다.

    # 한 번의 퀴즈 풀이가 끝났을 때 결과를 정리하는 메서드입니다.
    def finish_round(self, score: int, total_questions: int) -> None:  
        self.play_count += 1  # 퀴즈를 끝까지 한 번 완료했으므로 플레이 횟수를 1 늘립니다.
        print("\n========================================") 
        print(f"[결과] {total_questions}문제 중 {score}문제 정답") 
        print("========================================")  
        if score > self.best_score:  
            self.best_score = score  # 더 높은 점수라면 최고 점수를 새 값으로 갱신합니다.
            print("[기록] 새로운 최고 점수입니다.") 
        else:  # 기존 최고 점수를 넘지 못한 경우 이 블록이 실행됩니다.
            print(f"현재 최고 점수는 {self.best_score}점입니다.") 
        self.save_state()  # 바뀐 최고 점수와 플레이 횟수를 파일에 저장합니다.
####################### 퀴즈 풀기 관련 끝 ######################

# 7. 퀴즈 추가 : 사용자가 새 퀴즈를 직접 입력해 추가하는 메서드입니다.
    def add_quiz(self) -> None: 
        print("\n[추가] 새로운 퀴즈를 추가합니다.")  
        question = self.get_non_empty_text("문제를 입력하세요: ")  
        if question is None:  # 입력 중단으로 문제 문장을 받지 못한 경우를 검사합니다.
            return  # 현재 기능을 멈추고 메뉴로 돌아갑니다.
        choices: list[str] = []  # 4개의 선택지를 차례대로 담을 빈 리스트를 만듭니다.
        for index in range(1, 5):  # 1번부터 4번까지 선택지를 하나씩 입력받기 위해 반복합니다.
            choice = self.get_non_empty_text(f"선택지 {index}: ")  # 현재 번호의 선택지를 입력받습니다.
            if choice is None:  # 입력 중단으로 선택지를 받지 못한 경우를 검사합니다.
                return  # 현재 기능을 멈추고 메뉴로 돌아갑니다.
            choices.append(choice)  # 정상적으로 받은 선택지를 리스트에 추가합니다.
        answer = self.get_number_input("정답 번호 (1-4): ", 1, 4)  # 정답 번호를 1~4 사이 숫자로 입력받습니다.
        if answer is None:  # 입력 중단으로 정답 번호를 받지 못한 경우를 검사합니다.
            return  # 현재 기능을 멈추고 메뉴로 돌아갑니다.
        try:  # Quiz 객체를 만드는 과정에서 값 검증 오류가 날 수 있으므로 try를 사용합니다.
            new_quiz = Quiz(question=question, choices=choices, answer=answer)  # 입력받은 값으로 새 Quiz 객체를 만듭니다.
        except ValueError as error:  # 빈 문제나 잘못된 선택지처럼 검증 실패가 발생하면 여기로 들어옵니다.
            print(f"\n[주의] 퀴즈를 만드는 중 문제가 발생했습니다: {error}")  # 왜 추가에 실패했는지 쉽게 알려 줍니다.
            return  # 잘못된 데이터는 저장하지 않고 메서드를 끝냅니다.
        self.quizzes.append(new_quiz)  # 검증을 통과한 새 퀴즈를 전체 퀴즈 목록에 추가합니다.
        self.save_state()  # 추가된 퀴즈를 state.json 파일에 바로 저장합니다.
        print("[완료] 퀴즈가 추가되었습니다.")
####################### 퀴즈 추가 관련 끝 ######################

    def list_quizzes(self) -> None:  # 현재 저장된 퀴즈 목록을 화면에 출력하는 메서드입니다.
        if not self.quizzes:  # 퀴즈가 하나도 없으면 목록을 보여 줄 수 없으므로 먼저 검사합니다.
            print("\n[주의] 아직 등록된 퀴즈가 없습니다.")  # 빈 목록 상태를 사용자에게 알려 줍니다.
            return  # 더 출력할 내용이 없으므로 메서드를 끝냅니다.
        print(f"\n[목록] 등록된 퀴즈 목록 (총 {len(self.quizzes)}개)")  # 전체 퀴즈 수를 함께 보여 줍니다.
        print("----------------------------------------")  
        for index, quiz in enumerate(self.quizzes, start=1):  # 퀴즈를 하나씩 꺼내면서 번호를 붙입니다.
            print(f"[{index}] {quiz.question}") 
        print("----------------------------------------")  

    def show_best_score(self) -> None:  # 최고 점수와 플레이 정보를 확인하는 메서드입니다.
        if self.play_count == 0:  # 아직 한 번도 퀴즈를 끝까지 푼 적이 없는지 확인합니다.
            print("\n[안내] 아직 퀴즈를 완료한 기록이 없습니다.") 
            return  # 표시할 점수가 없으므로 메서드를 끝냅니다.
        print(f"\n[점수] 최고 점수: {self.best_score}점")  # 현재까지 저장된 최고 점수를 출력합니다.
        print(f"총 플레이 횟수: {self.play_count}회") 

    def exit_program(self) -> None:  # 프로그램을 정상적으로 종료할 때 사용하는 메서드입니다.
        self.save_state()  # 종료 전에 현재 상태를 state.json 파일에 저장합니다.
        print("\n프로그램을 종료합니다.")  
        self.is_running = False  # while 루프가 멈추도록 값을 False로 바꿉니다.
