lower_eng_char, upper_eng_char = [], []
    for i in range(1040, 1072):
        if i - 975 <= 90:
            upper_eng_char.append(chr(i - 975))
            lower_eng_char.append(chr(i - 943))