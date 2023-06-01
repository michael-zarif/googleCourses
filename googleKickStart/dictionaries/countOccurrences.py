def count_occurrences(text_or_list):
    result = {}
    for item in text_or_list:
        if item not in result:
            result[item] = 0
        result[item] += 1

    return result

print(count_occurrences("This is a new string"))
print(count_occurrences([401, 402, 404, 403, 404, 405, 403])) # errors list