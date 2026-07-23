#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4

    names = sorted([n for n in dir(hidden_4) if not n.startswith("__")])
    for name in names:
        print(name)
