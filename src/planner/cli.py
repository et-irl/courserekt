import argparse
from planner.url_generator import generate_url


def parse_year(year_str):
    year_str = year_str.replace("/", "-")  # Replace "/" with "-" if present
    if len(year_str) == 4:  # if input is like "2223"
        year_str = year_str[:2] + "-" + year_str[2:]  # Insert "-" to become "22-23"
    if len(year_str) == 5:  # if input is like "22-23"
        year_str = "20" + year_str  # Prepend "20" to become "2022-2023"
    return year_str


def parse_whitelist(whitelist_str):
    whitelist = {}
    for item in whitelist_str:
        key, value = item.split(":")
        whitelist[key.upper()] = [val.strip().upper() for val in value.split(',')]
    return whitelist


def parse_and_generate_url(acad_year, semester_no, courses, whitelist):
    return generate_url(
            parse_year(acad_year),
            int(semester_no),
            [course.upper() for course in courses],
            parse_whitelist(whitelist))


def main():
    parser = argparse.ArgumentParser(description="Generate NUSMods URL.")

    parser.add_argument('-y', '--year', type=str, default='2022-2023',
                        help='The academic year, e.g., "2022-2023", "22-23", "22/23", "2223".')
    parser.add_argument('-s', '--semester', type=int, required=True,
                        help='The semester number (1 or 2).')
    parser.add_argument('-c', '--courses', type=str, nargs='+', required=True,
                        help='The course codes, e.g., -c "LAJ2201" "CS2100".')
    parser.add_argument('-w', '--whitelist', type=str, nargs='+', default=[],
                        help='The whitelist as a series of "COURSE:TYPE" strings, e.g., -w "CS2100:LEC,TUT" "LAJ2201:LEC".')

    args = parser.parse_args()

    print(parse_and_generate_url(args.year, args.semester, args.courses, args.whitelist))


if __name__ == "__main__":
    main()