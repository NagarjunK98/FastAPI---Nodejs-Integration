import datetime

def calculate_days(dob : str) -> str :
    current_date = datetime.date.today()
    dob = dob.split("-")
    dob = datetime.date(int(dob[0]), int(dob[1]), int(dob[2]))
    result = current_date - dob
    return result
