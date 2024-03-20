import json
import sys
import os
import requests


def create_proj_from_acti(acti):
    return {
        "module": " - ".join(acti["module_title"].split(" - ")[1:]),
        "project": acti["acti_title"].replace("Back To The Future", "BTTF"),
        "start": acti["begin"].split()[0],
        "end": acti["end"].split()[0],
        "bttf": "Back To The Future" in acti["acti_title"],
    }


def main():
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

    print(f"{semester=} {year=}", file=sys.stderr)

    url = f"https://intra.epitech.eu/annuel/instance?format=json&semester={semester}&year={year}"
    fetched_data = requests.get(url, cookies={"user": cookie}).json()

    # No more error handling here, if something crashes after that point good luck

    planning = fetched_data["planning"]
    projects = []
    for key_unit, value_unit in planning.items():
        if "ADM" in key_unit:
            continue
        for acti in value_unit:
            if acti["type_code"] != "proj":
                continue
            projects.append(create_proj_from_acti(acti))

    export = {
        "promo": year + 5 - ((semester - 1) // 2),
        "semester": semester,
        "projects": projects,
    }
    print(json.dumps(export, indent=4))
