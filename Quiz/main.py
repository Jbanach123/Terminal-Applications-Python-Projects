from question_model import Question
from data import question_data, question_computer, question_animals
from quiz_brain import QuizBrain


# Create a list of Question objects from the question data
question_bank = []
for q_dict in question_animals:
    question_text = q_dict["question"]
    question_answer = q_dict["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
# Run the quiz until there are no more questions
while quiz.still_has_questions():
    quiz.next_question()

# Display final results
print("You've completed the quiz")
print(f"Your final score was:{quiz.score}/{len(question_bank)} ")
