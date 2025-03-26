def count_chars(text):
    char_dict = {}
    splitText = list(text)
    
    for char in splitText:
        char = char.lower()
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1

    return char_dict


def sort_on(dictionary):
    return dictionary["count"]


def sort_dictionary(dictionary):
    dict_list = [];

    for key, value in dictionary.items():
        if key.isalpha():
            dict_list.append({'char': key, 'count': value})

    dict_list.sort(reverse=True, key=sort_on)
    return dict_list



