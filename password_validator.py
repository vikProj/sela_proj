import re
import sys


def validate_password(psw: str) -> (bool, list[str]):
    """
    The method validates provided password, return True/False and list of messages if case of invalid password. \n
    Password validation rules: \n

        *1. Length – minimum of 10 characters. \n
        *2. Contain both alphabet and number. \n
        *3. Include both the small and capital case letters. \n

    :param psw: str - Provided password
    :return: tuple of:
        1. flag - True/False for Valid/Invalid password.
        2. list of messages in case of invalid password

    """
    msgs = []
    flag = True

    if len(psw) < 10:
        msgs.append("Password must be at least 10 characters")
    if not re.search('', psw):
        msgs.append("Password must include at least one lower case letter")
    if not re.search('[A-Z]', psw):
        msgs.append("Password must include at least one upper case letter")
    if not re.search('[0-9]', psw):
        msgs.append("Password must include at least one digit")
    if re.search("\s", psw):
        msgs.append("Password can't include spaces")

    if len(msgs) > 0:
        flag = False

    return flag, msgs


def print_func(validated_flag: bool, msgs: list):
    """
    This method prints provided messages in green when provided flag is True and in red when provided flag is Red
    :param validated_flag: bool
    :param msgs: list of messages to print
    :return:
    """
    if validated_flag:
        pr_green("Provided password is valid!")
    else:
        pr_red("Provided password is not valid!\n")
        for i in msgs:
            pr_red(i)


def pr_green(text: str):
    """
    Prints provided message in green

    :param text: str provided message
    :return: None
    """
    print(f"\033[92m {text}\033[00m")


def pr_red(text: str):
    """
    Prints provided message in red

    :param text: str provided message
    :return: None
    """
    print(f"\033[91m {text}\033[00m")


def main():
    """
    This method retrieves password from provided input arguments and invokes password validation functionality.
    Initialize exit code for 0 in case of valid password and exit code for 1 in case of invalid password.

    Color the output green if it passed the validation and red if it didn’t.

    :return: None
    """
    if len(sys.argv) < 2:
        pr_red("Password is not provided")
        sys.exit(1)

    psw = sys.argv[1]
    flag, msgs = validate_password(psw)

    print_func(flag, msgs)

    if not flag:
        sys.exit(1)
    else:
        sys.exit(0)


if __name__ == '__main__':
    main()




