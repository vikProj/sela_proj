FEMALE_KEY = 'female'
MALE_KEY = 'male'
SEX_KEY = 'sex'
AGE_KEY = 'age'


def split_male_female(data_set: dict[int: dict]) -> (dict, dict):
    """
    Function receives data set of persons data and returns 2 data sets for males and females
    :param data_set: dictionary of dictionaries with persons data, where key is numeric sequence
    :return: tuple of dictionaries for males and females, where key is male/female and value is list of persons
    """

    if not isinstance(data_set, dict):
        raise TypeError("Parameter data_set is required to be of type dictionary")

    female_lst = []
    male_lst = []

    if data_set:
        for item in data_set.values():
            if item.get(SEX_KEY) == FEMALE_KEY:
                female_lst.append(item)
            elif item.get(SEX_KEY) == MALE_KEY:
                male_lst.append(item)

    return {MALE_KEY: male_lst}, {FEMALE_KEY: female_lst}


def print_values_above(data: dict[str: list[dict]], age: int = 0):
    """
    Receives dictionary of persons and age (optional)
    if parameter age > 0, function will print only persons that their age more than received value,
    otherwise will print received dictionary of persons

    :param data: dictionary of persons
    :param age: int parameter optional, default 0
    :return: None
    """
    if data:
        for k, v in data.items():
            print(f'{k}:')
            for item in v:
                if age > 0:
                    if item.get(AGE_KEY) > age:
                        print(f'{item}')
                else:
                    print(f'{item}')


def find_median_average(data: dict[str: list[dict]]) -> dict[str:float]:
    """
    Function receives dictionary of persons and calculates age average and median
    :param data: dictionary of persons
    :return: result - dict contains average and median values for persons per key
    """

    result = {}

    for key, value in data.items():

        sum = 0
        for dict_item in value:
            if dict_item.get(AGE_KEY):
                sum += dict_item.get(AGE_KEY)

        average = sum / len(value)

        sorted_age_list = sorted(value, key=lambda i: i.get(AGE_KEY))

        index = int(len(sorted_age_list) / 2 - 1)

        if len(sorted_age_list) % 2 != 0:
            median = sorted_age_list[len(sorted_age_list) // 2].get(AGE_KEY)
        else:
            median = (sorted_age_list[index].get(AGE_KEY) + sorted_age_list[index + 1].get(AGE_KEY)) / 2

        result[key] = {"average": average, "median": median}

    return result


def main():
    data_set = {1: {"name": "Tal", "age": 22, "sex": "male"},
                2: {"name": "Anat", "age": 57, "sex": "female", "ID": 123456789},
                3: {"name": "Gal", "age": 35, "sex": "male", "ID": 789456123},
                4: {"name": "Limor", "age": 30, "sex": "female"},
                5: {"name": "Serge", "age": 45, "sex": "male"},
                6: {"name": "Iren", "age": 27, "sex": "female"},
                7: {"name": "Karin", "age": 42, "sex": "female"},
                8: {"name": "Itay", "age": 50, "sex": "male"},
                9: {"name": "Saimon", "age": 60, "sex": "male"},
                10: {"name": "Itay", "age": 43, "sex": "male"},
                11: {"name": "Sabina", "age": 43, "sex": "female"},
                12: {"name": "Loren", "age": 43, "sex": "female"},
                13: {"name": "Lotem", "age": 33, "sex": "female"},
                }

    print('Split data for male and female:')
    res1, res2 = split_male_female(data_set)

    print_values_above(res1)
    print('=====================================================================\n')
    print_values_above(res2)
    print('=====================================================================\n\n')

    print('Calculate result of average and median for male and female:')
    print(find_median_average(res1))
    print('=====================================================================\n')
    print(find_median_average(res2))
    print('=====================================================================\n\n')

    print('Display females that age more than 30:')
    print_values_above(res2, 30)
    print('=====================================================================\n\n')

    print('Display males that age more than 40:')
    print_values_above(res1, 40)


if __name__ == '__main__':
    main()
