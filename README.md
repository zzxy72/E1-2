# E1-2. Git과 함께하는 Python 첫 발자국

이 저장소는 터미널에서 실행하는 퀴즈 게임 과제를 위한 프로젝트입니다.  
프로그램은 `state.json` 파일에 퀴즈 목록, 최고 점수, 플레이 횟수를 저장하고 다시 실행해도 같은 데이터를 이어서 사용합니다.

## 프로젝트 개요

- Python으로 퀴즈 게임을 만들고, Git으로 변경 이력을 관리합니다.
- 사용자는 퀴즈 풀기, 퀴즈 추가, 퀴즈 목록 확인, 최고 점수 확인, 종료 기능을 사용할 수 있습니다.
- 저장 데이터는 `state.json`에 UTF-8로 보관합니다.

## 퀴즈 주제 선정 이유

이 프로젝트의 퀴즈 주제는 `Python 기초 문법과 JSON 저장`입니다.
문자열, 리스트, 조건문, 반복문처럼 파이썬을 처음 배울 때 꼭 익혀야 하는 개념을 문제로 만들면
프로그램을 직접 구현하는 과정과 퀴즈를 푸는 경험이 자연스럽게 연결된다고 생각했습니다.
또한 이 프로젝트의 핵심 기능 중 하나가 `state.json` 파일을 이용한 데이터 저장이기 때문에,
JSON을 왜 사용하는지도 함께 퀴즈에 포함해 학습 내용과 프로그램 기능이 이어지도록 구성했습니다.

## 실행 방법

프로젝트 루트에서 아래 명령을 실행합니다.

```bash
python src/main.py
```

## 파일 구조

```text
E1-2/
├─ README.md
├─ docs/
│  └─ system-architecture.md
├─ src/
│  ├─ main.py
│  ├─ quiz.py
│  ├─ quiz_game.py
│  └─ state.json
└─ 요구사항/
   └─ Readme.md
```

## 핵심 파일 역할

- `src/main.py`: 프로그램 시작점
- `src/quiz.py`: 개별 퀴즈를 표현하는 `Quiz` 클래스
- `src/quiz_game.py`: 게임 흐름과 저장 로직을 담당하는 `QuizGame` 클래스
- `src/state.json`: 퀴즈 목록, 최고 점수, 플레이 횟수를 저장하는 데이터 파일
- `docs/system-architecture.md`: 시스템 구조와 실행 흐름 설명 문서
- `요구사항/Readme.md`: 과제 원문 문서

## 데이터 파일 설명

`src/state.json`은 프로그램이 저장하는 상태 파일입니다.

- 경로: `./src/state.json`
- 인코딩: UTF-8
- 역할: 퀴즈 목록, 최고 점수, 플레이 횟수 저장

예상 스키마 예시는 아래와 같습니다.

```json
{
  "quizzes": [
    {
      "question": "Python의 창시자는?",
      "choices": ["Guido", "Linus", "Bjarne", "James"],
      "answer": 1
    }
  ],
  "best_score": 3,
  "play_count": 1
}
```

## 구현 기능 (기능 목록)

- 퀴즈 풀기
- 퀴즈 추가
- 퀴즈 목록 확인
- 최고 점수 확인
- 종료 시 상태 저장
- 잘못된 입력 처리

## 비고

- 퀴즈 게임 파일 기준 경로를 사용하므로, `src/quiz_game.py`는 `src/state.json`을 직접 읽고 씁니다.
- 문서와 소스는 UTF-8 기준으로 저장되어 한글이 깨지지 않도록 관리합니다.
