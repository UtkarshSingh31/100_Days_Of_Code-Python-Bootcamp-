class QuizBrain:
    def __init__(self,question_list):
        self.score=0
        self.question_numbers=0
        self.list=question_list

    def still_has_question(self):
        return self.question_numbers < len(self.list)

    def next_question(self):
        current_ques=self.list[self.question_numbers]
        self.question_numbers +=1
        user_answer=input(f"Q.{self.question_numbers}:{current_ques.user_text} (True/False): ")
        self.check_answer(user_answer,current_ques.user_ans)

    def check_answer(self,user_answer,correct_ans):
        if user_answer.lower()==correct_ans.lower():
            print("You got it right!")
            self.score +=1
        else:
            print("You got it wrong")
        print(f"The correct answer was: {correct_ans}")
        print(f"Your current score is: {self.score}/{self.question_numbers}")
        print("\n")


