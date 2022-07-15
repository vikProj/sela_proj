import json
import re
import sys

from typing import List


def validate_password(psw: str) -> (bool, List[str]):
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


def print_func(validate_flag: bool, msgs: list):
    """
    This method prints provided messages in green when provided flag is True and in red when provided flag is Red
    :param validate_flag: bool
    :param msgs: list of messages to print
    :return:
    """
    if validate_flag:
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


def read_file_key(file_name: str, key: str) -> (str, str):

    """
    This method reads key from provided file name. File name should be in json format. \n

    :param file_name: provided file name in json format to read
    :param key: a key to retrieve from a file
    :return: tuple of:
        1. password - the read value of the password from the file.
        2. messages - message in case of failure of file reading

    """

    msg = ""
    variables = {}
    psw = ""

    try:
        with open(file_name) as f:
            variables = json.load(f)

    except OSError as err:
        msg = f"Can't read provided file {file_name},\n {err}"

    try:
        if variables:
            psw = variables[key]

    except KeyError as e:
        msg = f"Can't read password from provided file"

    return psw, msg


def main():
    """
    This method retrieves provided file name as input arguments and invokes password validation functionality. \n
    Please provide argument and run script in following way: \n
    python ./password_validator.py -f '/mypath/password.txt'\n

    File should be provided in json format. \n
    Initialize exit code for 0 in case of valid password and exit code for 1 in case of invalid password. \n

    Color the output green if it passed the validation and red if it didn’t. \n

    :return: exit code for 0 in case of valid password and exit code for 1 in case of invalid password
        """

    if len(sys.argv) < 3 or sys.argv[1] != "-f":
        pr_red("File Name is not provided. Please provide next argument -f 'fileName'")
        sys.exit(1)

    file_name = sys.argv[2]
    key = "password"

    password, msg = read_file_key(file_name, key)

    if msg:
        pr_red(msg)
        sys.exit(1)

    flag, msgs = validate_password(password)

    print_func(flag, msgs)

    if not flag:
        sys.exit(1)
    else:
        sys.exit(0)


if __name__ == '__main__':
    main()
