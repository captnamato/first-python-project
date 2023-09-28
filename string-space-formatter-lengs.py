def format_string(string, length):
    if len(string) >= length:
        return string
    else:
        num_space = (length - len(string)) // 2
        for i in range(num_space):
            string = " " + string
        return string
