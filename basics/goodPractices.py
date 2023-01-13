"""
Python Good Practises
"""


def taskA(i: int = 0) -> None:
    """Description of task A

    Args:
        i (int, optional): this is the i description. Defaults to 0.
    """

    print("This is func A - " + str(i))


def taskB(tmp: str) -> str:
    """Description of task A

    Args:
        tmp (str): Description of tmp

    Returns:
        str: Description of the return
    """

    print("This is func B - " + tmp)

    return "Sucess"


def run():
    """Description of run
    """

    try:
        taskA()
        a = taskB(tmp="0")
        print(a)
    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    run()
