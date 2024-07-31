#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    for k in range(len(dir(hidden_4))):
        if (dir(hidden_4)[k][:2] == "__"):
            continue
        print(dir(hidden_4)[k])
