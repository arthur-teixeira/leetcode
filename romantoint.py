def roman_to_int(s):
    map = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }
    count, i = 0, 0
    while i < len(s):
        curr = map[s[i]]
        next_val = map[s[i+1]] if i + 1 <= len(s) - 1 else 0
        count += curr * -1 if curr < next_val else curr
        i += 1
    return count


roman_to_int("MCMXCIV")
