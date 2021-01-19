Sentence = ""
def is_question(sentence):
    questions = ("how","what","who","why","which","when","where","whom","is","are","have","did","do")
    if sentence.lower().startswith(questions):
        return sentence.capitalize() + "?"
    else:
        return sentence.capitalize() + "."
while True:
    user_input = input("Say somthing: ")
    if user_input == "\\end":
        break
    Sentence = Sentence + " " + is_question(user_input)
print(Sentence)