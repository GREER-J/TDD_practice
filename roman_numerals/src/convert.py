def convert(num: int) -> str:
    roman_map = {4: 'IV', 5: 'V'}
    rv = ''
    if num in roman_map.keys():
        rv = roman_map[num]
    else:
        rv += num * 'I'
    return rv
