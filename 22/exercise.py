import csv
import sys

HEADERS = ["user", "passwd", "id", "gid", "description", "home", "shell"]


def write_csv(in_file, file_obj):
    o = csv.writer(file_obj, delimiter="\t")
    o.writerow(HEADERS)
    for line in in_file:
        if not line.startswith(("#", "\n")):
            o.writerow(line.rstrip().split(":"))


def passwd_to_csv(input_file, dest_file):
    csv_contents = None
    with open(input_file, "r") as in_file:
        if dest_file:
            with open(dest_file, "w") as out_file:
                write_csv(in_file, out_file)
                output = open(dest_file, "r")
                csv_contents = output.read()
                output.close()
        else:
            write_csv(in_file, sys.stdout)

    return csv_contents


if __name__ == "__main__":
    if len(sys.argv) == 3:
        print(passwd_to_csv(sys.argv[1], sys.argv[2]))
    elif len(sys.argv) == 2:
        passwd_to_csv(sys.argv[1], None)
    else:
        passwd_to_csv(sys.stdin, None)
