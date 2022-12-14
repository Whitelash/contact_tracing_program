#!/usr/bin/env python3


import sys
import os.path
from format_list import format_list


def file_exists(file_name):
   # verify whether the file exists using os.path
    isFile = os.path.isfile(file_name)
    return isFile


def parse_file(file_name):
    # create an empty list each for the keys and values
    keys = []
    values = []

    # open the file
    file = open(file_name)

    # using the split function to separate the contacts into a list
    Lines = file.readlines()

    for line in Lines:
        key = line.split(',')[0]
        keys.append(key)
        value = line.split(',')[1:]
        values.append(value)

    # use zip where an iterator of tuples where the first item in each passed iterator is paired together,
    # and then the second item in each passed iterator are paired together
    zipped = zip(keys, values)
    D = dict(zipped)
    return D


def find_patients_zero(contacts_dic):
    # create empty lists each for the keys, values and patients_zero
    keyList = []
    valueList = []
    patients_zero = []

    # iterate through each key in the dictionary
    for i in contacts_dic.keys():
        # add the names to the list
        keyList.append(i)

    # iterate through each key in the dictionary
    for i in contacts_dic.values():
        # add the names to the list
        valueList.append(i)

    # flatten the list to one dimension
    flat_list = [item for sublist in valueList for item in sublist]

    res = []
    for sub in flat_list:
        res.append(sub.replace("\n", ""))

    # iterate through the keylist and check for names that only appear once
    for each in keyList:
        if each not in res:
            # add the names to the patients_zero_list
            patients_zero.append(each)

    return patients_zero


def find_potential_zombies(contacts_dic):
    # create empty lists each for keys, values and potential zombies
    keyList = []
    valueList = []
    potential_zombies = []

    # iterate though each key in the dictionary
    for i in contacts_dic.keys():
        # add the keys to the empty list created
        keyList.append(i)

    # iterate though each values in the dictionary
    for i in contacts_dic.values():
        # add the values to the empty list created
        valueList.append(i)

    # flatten the list to one dimension
    flat_list = [item for sublist in valueList for item in sublist]


    res = []
    for sub in flat_list:
        res.append(sub.replace("\n", ""))

    # iterate through the ietms in the list
    for each in res:
        # add names of the names not in the keylist to the potential zombie list
        if each not in keyList:
            potential_zombies.append(each)

    mylist = list(dict.fromkeys(potential_zombies))

    return mylist


def find_not_zombie_nor_zero(contacts_dic, patients_zero_list, zombie_list):
    # create an empty list
    not_zombie_nor_zero = []

    # iterate through each contact name in the dictionary
    for i in contacts_dic:
        # check whether the name is a patient zero or zombie
        if i not in patients_zero_list and zombie_list:
            # add name to the list
            not_zombie_nor_zero.append(i)

    # return the list
    return not_zombie_nor_zero


def find_most_viral(contacts_dic):
    # first find the maximum length
    most_viral_list = max(len(v) for v in contacts_dic.values())

    # return all keys that reference a list with the maximum length
    return [k for k, v in contacts_dic.items() if len(v) == most_viral_list]


def find_most_contacted(contacts_dic):
    # import python module
    from collections import Counter

    # create empty lists each for keys and values
    keyList = []
    valueList = []

    # iterate through each contact in the dictionary and add the keys to the list
    for i in contacts_dic.keys():
        keyList.append(i)

    # iterate through each contact in the dictionary and add the values to the list
    for i in contacts_dic.values():
        valueList.append(i)

    # flatten the list to one dimension
    flat_list = [item for sublist in valueList for item in sublist]

    res = []
    for sub in flat_list:
        res.append(sub.replace("\n", ""))

    # check for the most common values and keys in the list
    Counter = Counter(res)
    max_count = Counter.most_common(1)[0][1]
    z = [word for word, count in Counter.items() if count == max_count]

    return (z)


def find_maximum_distance_from_zombie(contacts_dic, zombie_list):
    # A small Dictionary comprehension to remove the trailing \n in the dictionary values
    contacts_dic = {k: [v.rstrip('\n') for v in vs] for k, vs in contacts_dic.items()}

    # create an empty dictionary
    max_dist = {}

    # iterate through each contact in the contacts_dic dictionary
    for person in contacts_dic:
        # set maximum distance to zero
        max_dist[person] = 0

    # iterate through each name in the zombie_list
    for zombie in zombie_list:
        # set maximum distance to zero
        max_dist[zombie] = 0

    # set changed to true
    changed = True

    # use a while loop
    while changed:
        changed = False
        for person in contacts_dic:
            for contact in contacts_dic[person]:
                if max_dist[person] <= max_dist[contact]:
                    max_dist[person] = max_dist[contact] + 1
                    changed = True
    return max_dist


def spreader_zombie(contacts_dic, potential_zombies):
    # A spreader zombie is sick person that only has had contact with potential zombies
    # A small Dictionary comprehension to remove the trailing \n in the dictionary values
    contacts_dic = {k: [v.rstrip('\n') for v in vs] for k, vs in contacts_dic.items()}

    # Create a list to store the names of the people who only had contact with potential_zombie
    spreader_zombies = []

    # Loop through each person in contact_dic
    for name, contacts in contacts_dic.items():
        # Check if the person only had contact with the people in potential_zombie
        if all(contact in potential_zombies for contact in contacts):
            # If the person only had contact with the people in potential_zombie , add their name to the list
            spreader_zombies.append(name)

    # Return the list of names
    return spreader_zombies


def find_regular_zombies(contacts_dic, potential_Zombies, spreaders):
    # A regular zombie is a sick person that has had contact with both potential zombies
    # and people who are already sick.
    # A small Dictionary comprehension to remove the trailing \n in the dictionary values
    contacts_dic = {k: [v.rstrip('\n') for v in vs] for k, vs in contacts_dic.items()}

    regular_zombies = []

    # Iterate through the keys and values in the dataset
    for person, contacts in contacts_dic.items():
        # Check if the person has had contact with both potential and spreader zombies
        if set(contacts).intersection(potential_Zombies) and set(contacts).intersection(spreaders):
            # Add the person to the list of regular zombies
            regular_zombies.append(person)

    # Return the list of regular zombies
    return regular_zombies



def find_zombie_predators(contacts_dic):
    # A zombie predator is a person that only has contact with people who are sick.
    # A small Dictionary comprehension to remove the trailing \n in the dictionary values
    contacts_dic = {k: [v.rstrip('\n') for v in vs] for k, vs in contacts_dic.items()}

    list_of_sick = []
    for each in contacts_dic:
        list_of_sick.append(each)

    only_sick_contacts = []

    # Iterate through the sick people
    for sick_person in list_of_sick:
        # Get the contacts of the sick person from the dataset
        contacts = contacts_dic.get(sick_person, [])

        # Check if all the contacts are also in the list of sick people
        if all(contact in contacts_dic for contact in contacts):
            # If all contacts are sick, add the sick person to the list of people with only sick contacts
            only_sick_contacts.append(sick_person)

    # Return the list of people with only sick contacts
    return only_sick_contacts


def main():
    filename = ""
    # Get the file name from the command line or ask the user for a file name
    args = sys.argv[1:]
    if len(args) == 0:
        filename = input("Please enter the name of the file: ")
    elif len(args) == 1:
        filename = args[0]
    else:
        print("""\n\nUsage\n\tTo run the program type:
        \tpython contact.py infile
        where infile is the name of the file containing the data.\n""")
        sys.exit()

    # Check that the file exists
    if not file_exists(filename):
        print("File does not exist, ending program.")
        sys.exit()

    # Create contacts dictionary from the file
    contacts_dic = parse_file(filename)

    # Print contact records
    for key, value in contacts_dic.items():
        print(key, " had contact with ", format_list(value))

    # Identify the possible patients zero
    patients_zero_list = find_patients_zero(contacts_dic)
    print("Patients zero(s) ", format_list(patients_zero_list))

    # Find potential zombies
    zombie_list = find_potential_zombies(contacts_dic)
    print("Potential Zombies ", format_list(zombie_list))

    # Find people who are neither patient zero(s) nor potential zombies.
    not_zombie_nor_zero = find_not_zombie_nor_zero(contacts_dic,
                                                   patients_zero_list, zombie_list)
    print("Neither Patient Zero or Potential Zombie: ", format_list(not_zombie_nor_zero))

    # Find the most viral people.
    most_viral_list = find_most_viral(contacts_dic)
    print("Most Viral People: ", format_list(most_viral_list))

    # Find most contacted.
    most_contacted = find_most_contacted(contacts_dic)
    print("Most contacted: ", format_list(most_contacted))

    # Maximum Distance from Zombie
    heights_dic = find_maximum_distance_from_zombie(contacts_dic, zombie_list)
    for key, value in heights_dic.items():
        print(key, ":", value)

    #  Find Spreader zombies
    spreaders = spreader_zombie(contacts_dic, zombie_list)
    if len(spreaders) == 0:
        print('Spreader zombies: (None)')
    else:
        print("Spreader zombies: ", format_list(spreaders))

    # Find regular zombies
    regular_zombies = find_regular_zombies(contacts_dic, zombie_list, spreaders)
    if len(regular_zombies) == 0:
        print('Regular zombies: (None)')
    else:
        print("Regular zombies: ", format_list(regular_zombies))

    # Find predator zombies
    predators = find_zombie_predators(contacts_dic)
    if len(predators) == 0:
        print('Predator zombies: (None)')
    else:
        print("Predator zombies: ", format_list(predators))


if __name__ == "__main__":
    main()
