class QuizBrain:
    def __init__(self, question_bank):
        self.question_number = 0
        self.score = 0
        self.question_bank = question_bank

    def next_question(self):
        while self.question_number <= (len(self.question_bank) - 1):
            current_question = self.question_bank[self.question_number]
            if input(
                    f"Q{self.question_number + 1} {current_question.text} (True/False) ").title() == current_question.answer:
                print("Correct")
                self.question_number += 1
                self.score += 1

            else:
                print("Wrong")
                self.question_number += 1
        print(f"You got {self.score}")