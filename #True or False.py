#True or False

from tabnanny import check


question_data = [
    {
        "category": "Science: Computers",
        "type": "boolean",
        "difficulty": "medium",
        "question": "The HTML5 standard was published in 2014.",
        "correct_answer": "True",
        "incorrect_answers": [
            "False"
        ]
    },
    {
        "category": "Science: Computers",
        "type": "boolean",
        "difficulty": "medium",
        "question": "The first computer bug was formed by faulty wires.",
        "correct_answer": "False",
        "incorrect_answers": [
            "True"
        ]
    },
    {
        "category": "Science: Computers",
        "type": "boolean",
        "difficulty": "medium",
        "question": "FLAC stands for 'Free Lossless Audio Condenser'.",
        "correct_answer": "False",
        "incorrect_answers": [
            "True"
        ]
    },
    {
        "category": "Science: Computers",
        "type": "boolean",
        "difficulty": "medium",
        "question": "All program codes have to be compiled into an executable file in order to be run. This file can then be executed on any machine.",
        "correct_answer": "False",
        "incorrect_answers": [
            "True"
        ]
    },
    {
        "category": "Science: Computers",
        "type": "boolean",
        "difficulty": "easy",
        "question": "Linus Torvalds created Linux and Git.",
        "correct_answer": "True",
        "incorrect_answers": [
            "False"
        ]
    },
    {
        "category": "Science: Computers",
        "type": "boolean",
        "difficulty": "easy",
        "question": "The programming language 'Python' is based off a modified version of 'JavaScript'",
        "correct_answer": "False",
        "incorrect_answers": [
            "True"
        ]
    },
    {
        "category": "Science: Computers",
        "type": "boolean",
        "difficulty": "medium",
        "question": "AMD created the first consumer 64-bit processor.",
        "correct_answer": "True",
        "incorrect_answers": [
            "False"
        ]
    },
    {
        "category": "Science: Computers",
        "type": "boolean",
        "difficulty": "easy",
        "question": "'HTML' stands for Hypertext Markup Language.",
        "correct_answer": "True",
        "incorrect_answers": [
            "False"
        ]
    },
    {
        "category": "Science: Computers",
        "type": "boolean",
        "difficulty": "easy",
        "question": "In most programming languages, the operator ++ is equivalent to the statement '+= 1'.",
        "correct_answer": "True",
        "incorrect_answers": [
            "False"
        ]
    },
    {
        "category": "Science: Computers",
        "type": "boolean",
        "difficulty": "hard",
        "question": "The IBM PC used an Intel 8008 microprocessor clocked at 4.77 MHz and 8 kilobytes of memory.",
        "correct_answer": "False",
        "incorrect_answers": [
            "True"
        ]
    }
]

class question:
    def __init__(self, text, answer):
        self.text=text
        self.answer=answer

question_bank=[]

for i in range(len(question_data)):
    q_text=question_data[i]["question"]
    q_answer=question_data[i]["correct_answer"]
    q=question(q_text,q_answer)
    question_bank.append(q)

class question_brain:
    global question_bank
    def __init__(self, q_list):
        self.q_nr=0
        self.q_list=q_list
        self.score=0
    def new_q(self):
        current_q=self.q_list[self.q_nr]
        self.q_nr+=1
        ans_user=input(f"Q.{self.q_nr}: {current_q.text} (True or false?)").lower()
        self.check_ans(ans_user,current_q.answer)
    def still_has_q(self):
        if self.q_nr<len(self.q_list):
            return True
        else:
            False
    def check_ans(self,ans_user,correct_ans):
        if correct_ans.lower()==ans_user:
            print("You got it right!")
            self.score+=1
        else:
            print("That's wrong!")
        print(f"Your score: {self.score}/{self.q_nr}\n\n")
    def final_score(self):
        print(f"You completed the game! Your final score is {self.score}/{self.q_nr}!")

q_brain=question_brain(question_bank)

while q_brain.still_has_q():
    q_brain.new_q()
q_total=q_brain.final_score()
