def passwd_to_dict(filename):
    passwdz = {}
    with open(filename, "r") as file:
        for line in file:
            if not line.startswith(("#", "\n")):
                user_name, passwd, uid, gid, description, home, shell = (
                    line.strip().split(":")
                )
                passwdz[user_name] = {
                    "password": passwd,
                    "id": uid,
                    "gid": gid,
                    "description": description,
                    "home": home,
                    "shell": shell,
                }
    return passwdz


print(passwd_to_dict("/etc/passwd"))
