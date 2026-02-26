import json
import sys


def summarize_test_scores(files):
    summary = {}
    for file in files:
        with open(file, "r") as json_file:
            scores = json.load(json_file)
            for key in scores:
                summary.setdefault(
                    key, {"total": 0, "count": 0, "min": None, "max": None}
                )
                min_value = summary[key]["min"]
                max_value = summary[key]["max"]
                summary[key]["total"] += scores[key]
                summary[key]["count"] += 1
                if min_value is None or min_value > scores[key]:
                    summary[key]["min"] = scores[key]

                if max_value is None or max_value < scores[key]:
                    summary[key]["max"] = scores[key]

    for key in summary:
        summary[key]["average"] = summary[key]["total"] / summary[key]["count"]

    return summary


if __name__ == "__main__":
    if len(sys.argv) > 1:
        print(summarize_test_scores(sys.argv[1:]))
