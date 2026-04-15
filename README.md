# E1-2. Git과 함께하는 Python 첫 발자국

터미널에서 실행하는 콘솔 퀴즈 게임입니다.  
문제를 풀고, 문제를 추가하고, 목록을 확인하고, 점수와 게임 기록을 저장할 수 있습니다.

## 프로젝트 개요

- Python으로 만든 콘솔 기반 퀴즈 게임입니다.
- 퀴즈 데이터, 최고 점수, 플레이 횟수, 게임 기록은 `state.json`에 저장됩니다.
- 프로그램을 다시 실행해도 이전에 추가한 퀴즈와 기록을 이어서 사용할 수 있습니다.

## 퀴즈 주제와 선정 이유

퀴즈 주제는 `Python 기초 문법과 JSON 저장`입니다.

- 문자열, 리스트, 조건문, 반복문 같은 입문 핵심 문법을 중심으로 구성했습니다.
- 직접 만든 프로그램으로 배운 문법을 바로 확인할 수 있어 이해가 쉽습니다.
- 파일 저장과 불러오기를 통해 JSON이 왜 필요한지도 자연스럽게 연결됩니다.

## 실행 방법

프로젝트 루트에서 아래 명령을 실행합니다.

```bash
python main.py
```

## 기능 목록

- 퀴즈 풀기
- 퀴즈 풀기 시 문제 수 선택
- 퀴즈 풀기 시 문제 순서 랜덤 출제
- 퀴즈 풀기 중 힌트 보기
- 퀴즈 추가
- 퀴즈 목록 확인
- 퀴즈 삭제
- 점수 확인
- 점수 확인 시 게임 기록 확인
- 종료 시 현재 상태 저장
- 입력 중단 또는 잘못된 입력 처리

## 파일 구조

```text
E1-2/
├─ README.md
├─ main.py
├─ quiz.py
├─ quiz_game.py
├─ state.json
├─ docs/
│  ├─ system-architecture.md
│  ├─ 설명팁.md
│  └─ screenshots/
└─ 요구사항/
   └─ Readme.md
```

## 데이터 파일 설명

`state.json`은 게임 상태를 저장하는 파일입니다.

- 경로: 프로젝트 루트 `state.json`
- 역할: 퀴즈 목록, 최고 점수, 플레이 횟수, 게임 기록 저장
- 인코딩: UTF-8

`quiz_game.py`에서는 `Path(__file__).resolve().parent / "state.json"`으로 이 파일을 찾습니다.  
즉, 실행 위치가 어디든 프로젝트 루트 기준으로 저장과 불러오기가 이루어집니다.

스키마는 아래 구조를 따릅니다.

```json
{
  "quizzes": [
    {
      "question": "문제 문장",
      "choices": ["선택지 1", "선택지 2", "선택지 3", "선택지 4"],
      "answer": 1,
      "hint": "풀이 중 볼 수 있는 힌트"
    }
  ],
  "best_score": 0,
  "play_count": 0,
  "score_history": [
    {
      "played_at": "2026-04-14 15:30:00",
      "question_count": 3,
      "correct_count": 2,
      "hint_count": 1,
      "score": 18
    }
  ]
}
```

- `quizzes`: `Quiz` 객체 목록
- `question`: 문제 문장
- `choices`: 4개의 선택지 목록
- `answer`: 정답 번호, `1`부터 `4`까지의 정수
- `hint`: 풀이 중 보여 줄 힌트
- `best_score`: 최고 점수
- `play_count`: 누적 플레이 횟수
- `score_history`: 모든 게임 기록 목록

## 실행 화면 스크린샷 위치
- `docs/screenshots/play.png`
- `docs/screenshots/python-version.png`

## Git 정리 방식

커밋 메시지는 규칙에 맞춰 `feat:`, `fix:`, `docs:`, `refactor:`, `test:` 형태로 정리했습니다.

- 기능 추가는 `feat`
- 버그 수정은 `fix`
- 문서 수정은 `docs`
- 기능 변화 없는 구조 정리는 `refactor`
- 실행 확인은 `test`

히스토리 정리 과정에서는 기존 커밋 메시지를 규칙에 맞게 다시 쓰고, 최종적으로 원격 저장소에 반영했습니다.

- `git log --oneline --graph` 결과 스크린샷 : docs/screenshots/git-log.png

