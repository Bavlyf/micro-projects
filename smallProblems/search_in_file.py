file_path = input("Please enter file path:\n")
search_word = input("Please enter word you want to search in file:")
def search_in_file(file_path,search_word):
    with open(file_path) as f:
        content = f.read()
    if search_word.lower() in content.lower():
        num_of_times=content.lower().count(search_word.lower())
        return f"the file contains {search_word} {num_of_times} time(s)."
    else:
        return "word does not exist"

print(search_in_file(file_path,search_word))
