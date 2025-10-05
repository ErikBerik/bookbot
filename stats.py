def count_words(input_string):
    words = input_string.split()
    return len(words)

def count_characters(input_string):
    lowercase_input = input_string.lower()
    counts = {}
    for char in lowercase_input:
        counts.setdefault(char,0)
        counts[char] += 1
    return counts

def sorted_list_of_dicts(char_dict):
    def sort_on(items):
        return items["num"]
    dictlist = []
    for char,num in char_dict.items():
        dictlist.append({"char":char,"num":num})
    dictlist.sort(reverse=True, key=sort_on)
    return dictlist
    
