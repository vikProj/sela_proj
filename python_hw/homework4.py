from __future__ import annotations


class Date:
    """
        Class Date represents date object that contains day, month, year as int's
        Supports compare functions
    """
    __days_per_month = {1: {"days": 31, "name": "January"},
                        2: {"days": 28, "name": "February"},
                        3: {"days": 31, "name": "March"},
                        4: {"days": 30, "name": "April"},
                        5: {"days": 31, "name": "May"},
                        6: {"days": 30, "name": "June"},
                        7: {"days": 31, "name": "July"},
                        8: {"days": 31, "name": "August"},
                        9: {"days": 30, "name": "September"},
                        10: {"days": 31, "name": "October"},
                        11: {"days": 30, "name": "November"},
                        12: {"days": 31, "name": "December"}}

    def __init__(self, day: int, month: int, year: int):
        """
        Date initialization, receives day, month and year as int values.
            Day should be between 1 and 31 \n
            Month should be between 1 and 12 \n
            Year should be 4-digit number \n

        Validate input values for valid date \n
        Raise exception if the date is invalid \n

        :param day: int value
        :param month: int value
        :param year: int value
        """

        if day < 1 or day > 31 or not isinstance(day, int):
            raise ValueError("Day should be int value between 1 and 31")
        if month < 1 or month > 13:
            raise ValueError("Month should be int value between 1 and 12")
        if year < 1000 or year > 9999:
            raise ValueError("Year should be int value and includes 4 digits")

        self.__day = day
        self.__month = month
        self.__year = year
        self.__isLeap = False

        self.__isLeap = self._is_leap_year(self.__year)

        is_valid, msg = self.is_valid()
        if not is_valid:
            raise ValueError(msg)


    def _is_leap_year(self, year) -> bool:
        """
        This method Determines whether a year is a leap year

        :return: True/False - whether a year is a leap year
        """

        return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

    def is_valid(self) -> (bool, str):
        """
        The method checks whether the date is correct.
        It means that: \n
            (1) it contains day, month, year \n
            (2) value of a day is valid for the selected month and year. \n

        :return: tuple with 2 values:
                 bool - if date is valid,
                 str - error message in case of invalid date

        """
        valid = True
        msg = f""

        if not (self.__day or self.__month or self.__year):
            valid = False
            msg = "Date should contain day, month and year"

            return valid, msg

        if self.__month == 2:

            if self.__isLeap and self.__day > (Date.__days_per_month[self.__month]["days"] + 1):
                valid = False
                msg = f"Number of days in February in year {self.__year} should be between 1 and 29"

            elif not self.__isLeap and self.__day > Date.__days_per_month[self.__month]["days"]:
                valid = False
                msg = f"Number of days in February in year {self.__year} should be between 1 and 28"

        elif self.__day > Date.__days_per_month[self.__month]['days']:
            valid = False
            msg = f"Number of days in {Date.__days_per_month[self.__month]['name']} should be between 1 and {Date.__days_per_month[self.__month]['days']}"

        return valid, msg

    def __str__(self):
        return f"{Date.__days_per_month[self.__month]['name']} {self.__day}, {self.__year}"

    def get_next_day(self) -> Date:
        """
        The method returns next date for the given date
        :return: Date - value of the next date
        """
        next_month_flag = False

        next_day = self.__day
        next_month = self.__month
        next_year = self.__year

        if self.__month == 2:
            if self.__isLeap and self.__day == (Date.__days_per_month[self.__month]['days'] + 1):
                next_day = 1
                next_month_flag = True
            elif not self.__isLeap and self.__day == Date.__days_per_month[self.__month]['days']:
                next_day = 1
                next_month_flag = True
            else:
                next_day += 1

        else:
            if self.__day == Date.__days_per_month[self.__month]['days']:
                next_day = 1
                next_month_flag = True
            else:
                next_day += 1

        if next_month_flag:
            if self.__month == 12:
                next_month = 1
                next_year += 1
            else:
                next_month += 1

        return Date(next_day, next_month, next_year)

    def get_next_days(self, days_to_add: int) -> Date:
        """
        The method returns date after days to add \n

        :param days_to_add: numbers to add to the current date \n

        :return: Date - date after days to add
        """
        future_day = self.__day
        future_month = self.__month
        future_year = self.__year

        while days_to_add > 0:

            days_delta = Date.__days_per_month[future_month]['days'] - future_day

            if future_month == 2 and self.__isLeap:
                days_delta += 1

            if days_delta < days_to_add:
                future_day = 1

                if future_month == 12:
                    future_year += 1
                    future_month = 1
                else:
                    future_month += 1

                days_to_add -= days_delta + 1

            else:
                future_day += days_to_add
                days_to_add -= days_to_add

        return Date(future_day, future_month, future_year)

    def _if_not_instanse_of(self, obj):
        """
        The method checks if the input object is instance of type Date otherwise raises exception
        :param obj:  input Object
        :return: None
        """
        if not isinstance(obj, Date):
            raise TypeError("Object should be of type Date")

    def __lt__(self, other) -> bool:
        """
        The method describes less than operator(<) \n
        It means - compares between two objects of type Date \n
        and return boolean value. \n
        If one of the objects is not of type Date - raised exception

        :param other: Date object to compare
        :return: True - in case of self object less than other object,
                 False - in case of self object greater than other object
        """
        self._if_not_instanse_of(other)

        if self.__year > other.__year:
            return False
        elif self.__month > other.__month:
            return False
        elif self.__day > other.__day:
            return False
        else:
            return True

    def __le__(self, other) -> bool:
        """
        The method descries less than or equal to (<=) \n
        It means - compares between two objects of type Date \n
        and return boolean value. \n
        If one of the objects is not of type Date - raised exception

        :param other: Date object to compare
        :return: True - in case of self object less than or equal to other object,
                 False - in case of self object greater than other object
        """
        return self.__lt__(other) or self.__eq__(other)

    def __gt__(self, other) -> bool:
        """
        The method describes greater than operator (>) \n
        It means - compares between two objects of type Date \n
        and return boolean value. \n
        If one of the objects is not of type Date - raised exception

        :param other: Date object to compare
        :return: True - in case of self object greater than other object,
                 False - in case of self object less than other object
        """
        self._if_not_instanse_of(other)

        if self.__year < other.__year:
            return False
        elif self.__month < other.__month:
            return False
        elif self.__day < other.__day:
            return False
        else:
            return True

    def __ge__(self, other) -> bool:
        """
        The method describes greater than or equal to (>=) \n
        It means - compares between two objects of type Date \n
        and return boolean value. \n
        If one of the objects is not of type Date - raised exception

        :param other: Date object to compare
        :return: True - in case of self object greater than or equal to other object,
                 False - in case of self object less than other object
        """
        return self.__gt__(other) or self.__eq__(other)

    def __eq__(self, other) -> bool:
        """

        The method describes equality operator(==) \n
        It means - compares between two objects of type Date \n
        and return boolean value. \n
        If one of the objects is not of type Date - raised exception

        :param other: Date object to compare
        :return: True - in case of self and other  objects are equal,
                 False - in case of self and other  objects are not equal
        """
        self._if_not_instanse_of(other)

        if self.__year == other.__year and self.__month == other.__month and self.__day == other.__day:
            return True
        else:
            return False

    def __ne__(self, other) -> bool:
        """

        The method describes not equal to operator(!=) \n
        It means - compares between two objects of type Date \n
        and return boolean value. \n
        If one of the objects is not of type Date - raised exception

        :param other: Date object to compare
        :return: True - in case of self and other objects are not equal,
                 False - in case of self and other objects are equal
        """
        self._if_not_instanse_of(other)

        if self.__year != other.__year or  self.__month != other.__month or self.__day != other.__day:
            return True
        else:
            return False

    def __sub__(self, other) -> int:
        """
        This method returns a difference in days between a given date and another date

        :param other: Date object
        :return: int - difference in days between two given days
        """
        self._if_not_instanse_of(other)

        year_delta = abs(self.__year - other.__year)
        days_delta = 0
        start_obj = None
        end_obj = None

        if year_delta > 0:
            if self.__year < other.__year:
                start_obj = self
                end_obj = other
            else:
                start_obj = other
                end_obj = self

        if year_delta > 1:
            days_delta = (year_delta - 1) * 365

            leap_years = list(filter(self._is_leap_year, range(start_obj.__year + 1, end_obj.__year)))
            print("leap_years =", leap_years)

            if len(leap_years) > 0:
                days_delta += len(leap_years)

        if self.__year != other.__year:
            days_delta += self._count_days(start_obj, True)
            days_delta += self._count_days(end_obj, False)

        else:
            if self.__month < other.__month:
                month_count = self.__month
                start_obj = self
                end_obj = other

            else:
                month_count = other.__month
                start_obj = other
                end_obj = self

            while month_count <= end_obj.__month:
                if month_count == start_obj.__month:
                    days_delta += Date.__days_per_month[month_count]['days'] - start_obj.__day

                elif month_count == end_obj.__month:
                    days_delta += end_obj.__day
                else:
                    days_delta += Date.__days_per_month[month_count]['days']

                month_count += 1

            if start_obj.__isLeap and (not (start_obj.__month == 2 and start_obj.__day == 29) or not (
                    end_obj.__month == 2 and end_obj.__day == 29)):
                if (start_obj.__month <= 2) or end_obj.__month >= 2:
                    days_delta += 1

        return days_delta

    def _count_days(self, obj: Date, increase_flag: bool) -> int:
        """
        The method calculates number of days between given date to the end or to the start of the year
        and return number of the days

        :param obj: Date - provided date
        :param increase_flag: True - calculates number of days from the given date to the end of the year,
                              False - calculates number of days from start of the year to the given date
        :return: int - number of days
        """

        days_delta = 0
        count = obj.__month
        if increase_flag:
            stop = 13
        else:
            stop = 0

        while count != stop:
            if obj.__month == count:
                if increase_flag:
                    days_delta += Date.__days_per_month[count]['days'] - obj.__day
                else:
                    days_delta += obj.__day
            else:
                days_delta += Date.__days_per_month[count]['days']

            if increase_flag:
                count += 1
            else:
                count -= 1
        if obj.__isLeap and not (obj.__day == 29 and obj.__month == 2):
            if increase_flag:
                if obj.__month <= 2:
                    days_delta += 1
            else:
                if obj.__month >= 2:
                    days_delta += 1

        return days_delta




# date = Date(15, 8, 2003)
# # print(date.is_valid())
# print(date)
# next_date = date.get_dext_day()
# print("next_date is", next_date)


# date = Date(15, 8, 2003)
# print(date)
# next_date = date.get_dext_day()
# print("next_date is", next_date)

# date1 = Date(31, 12, 2003)

# print(date1)
# next_date1 = date1.get_dext_day()
# print("next_date is", next_date1)
#
# date2 = Date(29, 2, 2016)
#
# print(date2)
# next_date2 = date2.get_dext_day()
# print("next_date is", next_date2)
#
# date3 = Date(30, 4, 2003)
#
# print(date3)
# next_date3 = date3.get_next_day()
# print("next_date is", next_date3)


# date4 = Date(22, 4, 2003)
#
# print(date4)
# next_date4 = date4.get_next_day()
# print("next_date is", next_date4)



# date5 = Date(12, 2, 2016)
# print(date5.is_valid())
# print(date5)
# future_date5 = date5.get_next_days(8)
# print("future date = ", future_date5)

from datetime import date


# date4 = Date(12, 12, 2021)
#
# print(date4)
# future_date4 = date4.get_next_days(60)
# print("future date = ", future_date4)


# date1 = Date(18, 6, 2022)
# date2 = Date(16, 7, 2026)
#
# print("delta.days = ", date2 - date1)
#
# d0 = date(2022, 6, 18)
# d1 = date(2026, 7, 16)
# delta = d1 - d0
# print("delta.days = ", delta.days)
#
# print("************************************\n\n")

# date3 = Date(18, 2, 2016)
# date4 = Date(16, 7, 2017)
#
# print("delta.days = ", date4 - date3)
#
# d2 = date(2016, 2, 18)
# d3 = date(2017, 7, 16)
# delta1 = d3 - d2
# print("delta.days = ", delta1.days)

# print("************************************\n\n")
#
# date5 = Date(18, 2, 2016)
# date6 = Date(16, 7, 2016)
#
# print("delta1.days = ", date6 - date5)
#
# d4 = date(2016, 2, 18)
# d5 = date(2016, 7, 16)
# delta2 = d5 - d4
# print("delta2.days = ", delta2.days)
#
# print("************************************\n\n")
#
# date5 = Date(29, 2, 2016)
# date6 = Date(16, 7, 2016)
#
# print("delta1.days = ", date6 - date5)
#
# d4 = date(2016, 2, 29)
# d5 = date(2016, 7, 16)
# delta2 = d5 - d4
# print("delta2.days = ", delta2.days)


# date4 = Date(22, 4, 2003)
# print(date4)
#
# date5 = Date(25, 7, 2003)
# print(date5)
#
# date4_1 = Date(22, 4, 2003)
# print(date4_1)
#
# print(date5 != date4)
#
# print(date4_1 != date4)
