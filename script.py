from requests import post, get


url = "http://127.0.0.1:8000/"
helptext = """
\nCommands:
\n  set [key] [value]
\n  history [key]
\n  get [key]
\n  q(exit)
"""


def set_key_value(key, value):
    post(url+"key/", data={"key": key, "value": value})


def get_key_value(key):
    req = get(url+"key/"+key)
    if req.status_code == 404:
        print("Not Found The Key !!")
    else:
        dct = req.json()
        print(dct["value"])


def get_key_history(key):
    req = get(url+"history/"+key)
    if req.status_code == 404:
        print("Not Found The Key !!")
    else:
        for i in req.json():
            print(i["value"], i["date"])


while True:
    try:
        inp = input(">>>").split(" ")
        command = inp[0]
        if command == "get":
            get_key_value(inp[1])
        if command == "set":
            set_key_value(inp[1], inp[2])
        if command == "history":
            get_key_history(inp[1])
        if command == "q":
            break
    except:
        print("Wrong command !!"+helptext)
