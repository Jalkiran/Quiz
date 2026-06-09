quiz={
    "What is the largest organ in the human body?":"Skin",
    'Which planet in our solar system is known as the "Red Planet"?':"Mars",
    "What is the capital of Japan":"Tokyo",
    "Which artist painted the Mona Lisa?":" Leonardo da Vinci",
    "How many rings in the Olympics?":"5",
    "Who was the first man on the moon?":"Neil Armstrong"
}
score=0
for ques,ans in quiz.items():
    print(ques)
    answer=input("Answer:").title().strip()
    if ans==answer:
        print("Correct✅")
        score+=1
    else:
        print("Wrong❌")
print(f"Your score:{score}/{len(quiz)}")
percentage=(score/len(quiz))*100
print(f"You scored{percentage}%")
if percentage>=80:
    print("Excellent!")
elif percentage>=50:
    print("Good!")
else:
    print("Keep Practicing.")
