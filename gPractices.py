# imports


def funcA(i: int = 0):
    print("This is func A - " + str(i))


def funcB(tmp: str) -> None:
    print("This is func B - " + tmp)


def run():
    try:
        funcA()
        funcB(0)
    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    run()