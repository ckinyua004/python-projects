class QuizBrain():
    def __init__(self,  question_list):
        self.question_number = 0
        self.question_list = input
        pass

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        return f"Q.{self.question_number}: {current_question.text} (True/False): "
    
    def still_has_questions(self):
        return self.question_number < len(self.question_list)
    
    def check_answer(self, user_answer):
        current_question = self.question_list[self.question_number - 1]
        if user_answer.lower() == current_question.answer.lower():
            print("You got it right!")
            return True
        else:
            print(f"That's wrong. The bcorrect answer is {current_question.answer}.")
            return False
    