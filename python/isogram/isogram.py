def is_isogram(string):
    # lower_string = string.lower()
    # for idx in range(len(lower_string)):
    #     if lower_string[idx] != " " and lower_string[idx] != "-":
    #         if lower_string.count(lower_string[idx]) > 1:
    #             return False
    # return True
    
    lower_string = string.lower().replace(" ","").replace("-","")
    
    return len(lower_string) == len(set(lower_string))
    
