# simple_calendar.py 
# A fully self-contained calendar utility implemented without using
# the 'calendar' or 'datetime' modules.
# Computes the day name of any given historical or future date.
# Designed to run cleanly in PyCharm.
# Aligned to ISO 8601: Weeks start on Monday. 

DAYS_IN_MONTH = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# Monday-start weekday order
DAY_NAMES = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

def is_leap_year(year: int) -> bool:
    """
    Leap year rule under the proleptic Gregorian calendar:
    - Years divisible by 4 are leap years,
    - Except years divisible by 100 (not leap years),
    - Except years divisible by 400 (leap years again).
    """
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def days_in_month(year: int, month: int) -> int:
    """Return the number of days in the given month of the given year."""
    if month == 2:
        return 29 if is_leap_year(year) else 28
    return DAYS_IN_MONTH[month - 1]

def validate_date(day: int, month: int, year: int) -> None:
    """Validate the date; raise ValueError if invalid."""
    if year <= 0:
        raise ValueError("Year must be >= 1.")
    if not (1 <= month <= 12):
        raise ValueError("Month must be between 1 and 12.")
    dim = days_in_month(year, month)
    if not (1 <= day <= dim):
        raise ValueError(f"Day must be between 1 and {dim} for {month}/{year}.")

def day_of_week(year: int, month: int, day: int) -> int:
    """
    Tomohiko Sakamoto's algorithm.
    Returns weekday index with Monday = 0.
    Original Sakamoto output: 0=Sunday,1=Monday,...6=Saturday.
    I convert it to ISO order: Monday=0,...,Sunday=6. 
    """
    # Sakamoto offset table
    t = [0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4]
    y = year
    m = month
    if m < 3:
        y -= 1

    # Original Sakamoto result (0 = Sunday)
    w = (y + y//4 - y//100 + y//400 + t[m-1] + day) % 7

    # Convert Sunday-start -> Monday-start
    # ISO index: Monday=0, Tuesday=1, ... Sunday=6
    iso_w = (w + 6) % 7
    return iso_w

def get_day_name_for_date(day: int, month: int, year: int) -> str:
    """Validate date, compute day index, and return the day name."""
    validate_date(day, month, year)
    w = day_of_week(year, month, day)
    return DAY_NAMES[w]

def print_month_calendar(year: int, month: int) -> None:
    """
    Print a simple ASCII monthly calendar for the given month.
    Now aligned to ISO 8601 Monday-first format.
    """
    validate_date(1, month, year)
    dim = days_in_month(year, month)
    first_w = day_of_week(year, month, 1)  # Monday=0

    month_names = [
        "January","February","March","April","May","June",
        "July","August","September","October","November","December"
    ]

    header = f"{month_names[month-1]} {year}"
    print(header.center(20))
    print("Mo Tu We Th Fr Sa Su")  # Monday-first format

    current = 0
    line = []

    # Leading blanks before day 1
    for _ in range(first_w):
        line.append("  ")
        current += 1

    # Print days of the month
    for d in range(1, dim + 1):
        line.append(f"{d:2d}")
        current += 1
        if current == 7:
            print(" ".join(line))
            line = []
            current = 0

    if line:
        print(" ".join(line))

def parse_date_str(date_str: str):
    """
    Parse dates in the format DD/MM/YYYY or D/M/YYYY.
    Only '/' is accepted as a separator.
    """
    parts = date_str.strip().split("/")
    if len(parts) != 3:
        raise ValueError("Date format must be DD/MM/YYYY.")
    d, m, y = map(int, parts)
    return d, m, y

def main():
    print("Simple Calendar — Determine the day name of any given date.")
    print("Enter a date (format: DD/MM/YYYY). Example: 13/03/2057")
    s = input("Date: ").strip()
    try:
        d, m, y = parse_date_str(s)
        day_name = get_day_name_for_date(d, m, y)
        print(f"{d:02d}/{m:02d}/{y} -> {day_name}")
        print()
        print("Monthly calendar for this date:")
        print_month_calendar(y, m)
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
