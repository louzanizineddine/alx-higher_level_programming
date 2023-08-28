#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    n_list = []
    for i in range(0, list_length):
        try:
            result = my_list_1[i] / my_list_2[i]
            n_list.append(result)
        except TypeError:
            print("wrong type")
            n_list.append(0)
        except ZeroDivisionError:
            print("division by 0")
            n_list.append(0)
        except IndexError:
            print("out of range")
            n_list.append(0)
        finally:
            pass
    return n_list
