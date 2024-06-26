def swap_commas_and_dots(input_string):
    swapped_string = ""
 
    for char in input_string:
        if char == ',':
            swapped_string += '.'
        elif char == '.':
            swapped_string += ','
        else:
            swapped_string += char
 
    return swapped_string
 
# Test the function
sentence = "This is a test, and it has some numbers: 1.23, 4.56, and 7.89."
result = swap_commas_and_dots(sentence)
print(result)
  # type: ignore