from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for i in question_data:
    q_text = i["question"]
    q_ans = i["correct_answer"]
    new_q = Question(q_text,q_ans)
    question_bank.append(new_q)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print(f"Your final score: {quiz.score}/{quiz.question_no}")