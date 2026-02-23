def parse_timing(timing):
    if timing:
        try:
            return float(timing)
        except ValueError:
            return None


def run_timing():
    total = 0.0
    times = 0
    while timing := parse_timing(input("Enter 10KM run time: ")):
        total += timing
        times += 1

    return (total / times, times)


if __name__ == "__main__":
    mean, times = run_timing()
    print(f"Average of {mean}, over {times} runs")
