# from main import question_bank
class QuizBrain:

    def __init__(self,q_list):
        self.score = 0
        self.question_no=0
        self.question_list = q_list

    def next_question(self):
        score = 0
        user_answer = input(f"Q.{self.question_no +1} {self.question_list[self.question_no].text} (True/False)? ")
        self.check_answer(user_answer, self.question_list[self.question_no].answer)

    def check_answer(self, user_answer, original_answer):
        if user_answer == original_answer:
            self.score += 1
            print("You got it right!")
            print(f"The correct answer is {user_answer}")
            print(f"your current score is {self.score}/{self.question_no + 1}")
            self.question_no += 1
            print("\n")
        else:
            print(f"Wrong Answer, Your current score: {self.score}/{self.question_no + 1}")
            self.question_no += 1
            print("\n")

    def still_has_questions(self):
        return self.question_no < len(self.question_list)

