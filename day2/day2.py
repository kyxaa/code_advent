import sys
import os

## We are going to fetch the information and shove it into a list with each line being converted into a tuple for later processing

def fetch_passwords(file_location):
    with open(file_location,'r') as in_file:
        lines = in_file.read().splitlines()
        tuple_list = []
        for line in lines:
            tuple_item = tuple(map(str, line.replace('-',' ').replace(':','').split(' ')))
            tuple_list.append(tuple_item)
    return tuple_list

## The items in the list of passwords will be in the format: ("8","13","r","rrldowdl")

def password_validation(password_list):
    valid_passwords = []
    for tuple_item in password_list:
        count = 0
        (min,max,character,password) = tuple_item
        for char in password:
            if char == character:
                count += 1
        if int(min) <= count <= int(max):
            valid_passwords.append(tuple_item)
    return valid_passwords

password_list = fetch_passwords(f'{sys.path[0]}\\passwords.txt')
valid_passwords = password_validation(password_list)
print(len(valid_passwords))
# print(password_list)
