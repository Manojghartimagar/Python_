'''
day = 3

match day:
    case 1:
        print("Sunday")
    case 2:
        print("Monday")
    case 3:
        print("Tuesday")
    case _:
        print("Invalid day")

'''


def http_status(status: int) -> str:
    match(status):
        case 200:
            return "Ok"
        case 404:
            return "Not Found"
        case 500:
            return "Internet Server Error"
        case _:
            return "Unknow Status"
        
print(http_status(404))