def is_question(sentence):
    questions = ("how","what","who","why","which","when","where","whom","is","are","have","did","do")
    if sentence.lower().startswith(questions):
        return sentence.capitalize() + "?"
    else:
        return sentence.capitalize() + "."
sentence_list = []
while True:
    user_input = input("Say somthing: ")
    if user_input == "\\end":
        break
    else:
        sentence_list.append(is_question(user_input))

print(" ".join(sentence_list))