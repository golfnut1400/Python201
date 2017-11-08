


"""Define and use tf_quiz() function¶
tf_quiz() has 2 parameters which are both string arguments
question: a string containg a T/F question like "Should save your notebook after edit?(T/F): "
correct_ans: a string indicating the correct answer, either "T" or "F"
tf_quiz() returns a string: "correct" or "incorrect"
Test tf_quiz(): create a T/F question (or several!) to call tf_quiz()"""



# [ ] Create the program, run tests
def tf_quiz(question, correct_ans):
    if correct_ans == 'T':
        return 'correct'
    elif correct_ans == 'F':
        return 'incorrect'
    else:
        return 'Try again (T/F)'



question = input("Should save your notebook after edit (T/F)?").upper()
correct_ans = question

print(tf_quiz(question, correct_ans))
