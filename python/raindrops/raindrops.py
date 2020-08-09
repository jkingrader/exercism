def convert(number: int = 0) -> str:
    
    raindrops_str = ""

    if number % 3 == 0:
        raindrops_str += "Pling"

    if number % 5 == 0:
        raindrops_str += "Plang"

    if number % 7 == 0:
        raindrops_str += "Plong"

    if raindrops_str == "":
        raindrops_str = str(number)

    return raindrops_str
