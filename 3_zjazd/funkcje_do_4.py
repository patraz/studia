def make_split(text:str, separator: str=' ') -> list:
    return text.split(separator)

def clean_text(text:str) -> str:
    signs_to_delete = '.,:;?\"\'(){}[]\\'
    for sign in signs_to_delete:
        text = text.replace(sign, '')
    text = text.lower()
    return text

def no_of_words(text:list) -> int:
    return len(text)

def no_of_unique_words(text:list) -> int:
    return len(set(text))

def reps_of_words(content:list):
    reps =  {}
    for word in content:
        if word in reps.keys():
            reps[word] += 1
        else:
            reps[word] = 1
    return reps