import sys
import os


def main():
    print("This will do something later...")
    print(f"Arguments: {sys.argv}")

    semester = 4
    year = 2023
    cookie = os.getenv("EPI_USER_COOKIE")

    if len(sys.argv) != 3:
        print(
            f"{sys.argv[0]}: Bad usage -> {sys.argv[0]} SEMESTER YEAR", file=sys.stderr
        )
        return 1

    if cookie is None:
        print(
            "EPI_USER_COOKIE has not been set, it is necessary to fetch content from the intranet",
            file=sys.stderr,
        )
        return 1

    try:
        semester = int(sys.argv[1])
        year = int(sys.argv[2])
    except ValueError:
        print(
            "Could not get semester or year value, are they numbers?", file=sys.stderr
        )
        return 1

    print(f"{semester=} {year=} {cookie=}")
