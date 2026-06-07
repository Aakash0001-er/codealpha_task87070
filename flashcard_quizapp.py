flashcards ={
    "what is the capital of France":"'Paris",
    "what is 5+7 =":"12",
    "who wrote 'To kill a mockingbird":"Harper Lee",
    "what is chemical symbol of water?":"H2O",
    "which planet is known as the red planet":"Mars"
}

import random
def start_quiz():
    score=0
    total_questions=len(flashcards)

    #shuffle the questions
    questions=list(flashcards.keys())
    random.shuffle(questions)

    for question in questions:
        print("\n"+question)
        user_answer=input("your answer: ").strip()

        if user_answer.lower()==flashcards[question].lower():
            print("Correct Answer")
            score=+1
        else:
            print(f"Incorrect,The correct answer is{flashcards[question]}")
    print(f"\n you got {score} out of {total_questions} correct!")
#call the function
start_quiz()

def main():
    while True:
        play_again=input("\n Do you want to play again?(yes/no: ").strip().lower()
        if play_again !='yes':
            print("Thanks for playing! see you next time !")
            break
main()
