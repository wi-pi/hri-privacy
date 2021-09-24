from data.metadata import control1, control2, control3, control4, control5, control6, control7
from data.metadata import control8, control9, control10, control11, control12, control13, control14
from data.metadata import control15, control16, control17, control18, control19, control20, control21
from data.metadata import control22, control23, control24, control25, control26, control27, control28
from data.metadata import control29, control30, control31, control32, control33, control34, control35
from data.metadata import control36, control37, control38, control39, control40, control41, control42
from data.metadata import scenario1, scenario2, scenario3, scenario4, scenario5, scenario6, scenario7
from data.metadata import scenario8, scenario9, scenario10, scenario11, scenario12, scenario13, scenario14
from data.metadata import scenario15, scenario16
from random import randrange


def store(module, topics, privacy, realistic, location):
    topics.append(module.topics)
    privacy.append(module.mean_label)
    realistic.append(module.realistic_label)
    location.append(module.location)
    return topics, privacy, realistic, location

topics = []
privacy = []
realistic = []
location = []

# topics, privacy, realistic, location = store(control1, topics, privacy, realistic, location)
# topics, privacy, realistic, location = store(control2, topics, privacy, realistic, location)
# topics, privacy, realistic, location = store(control3, topics, privacy, realistic, location)
# topics, privacy, realistic, location = store(control4, topics, privacy, realistic, location)
# topics, privacy, realistic, location = store(control5, topics, privacy, realistic, location)
# topics, privacy, realistic, location = store(control6, topics, privacy, realistic, location)
# topics, privacy, realistic, location = store(control7, topics, privacy, realistic, location)
# topics, privacy, realistic, location = store(control8, topics, privacy, realistic, location)
# topics, privacy, realistic, location = store(control9, topics, privacy, realistic, location)
# topics, privacy, realistic, location = store(control10, topics, privacy, realistic, location)
# topics, privacy, realistic, location = store(control11, topics, privacy, realistic, location)
# topics, privacy, realistic, location = store(control12, topics, privacy, realistic, location)
# topics, privacy, realistic, location = store(control13, topics, privacy, realistic, location)
# topics, privacy, realistic, location = store(control14, topics, privacy, realistic, location)
# topics, privacy, realistic, location = store(control15, topics, privacy, realistic, location)
# topics, privacy, realistic, location = store(control16, topics, privacy, realistic, location)
# topics, privacy, realistic, location = store(control17, topics, privacy, realistic, location)
# topics, privacy, realistic, location = store(control18, topics, privacy, realistic, location)
# topics, privacy, realistic, location = store(control19, topics, privacy, realistic, location)
# topics, privacy, realistic, location = store(control20, topics, privacy, realistic, location)
# topics, privacy, realistic, location = store(control21, topics, privacy, realistic, location)
# topics, privacy, realistic, location = store(control22, topics, privacy, realistic, location)
# topics, privacy, realistic, location = store(control23, topics, privacy, realistic, location)
# topics, privacy, realistic, location = store(control24, topics, privacy, realistic, location)
# topics, privacy, realistic, location = store(control25, topics, privacy, realistic, location)
# topics, privacy, realistic, location = store(control26, topics, privacy, realistic, location)
# topics, privacy, realistic, location = store(control27, topics, privacy, realistic, location)
# topics, privacy, realistic, location = store(control28, topics, privacy, realistic, location)
# topics, privacy, realistic, location = store(control29, topics, privacy, realistic, location)
# topics, privacy, realistic, location = store(control30, topics, privacy, realistic, location)
# topics, privacy, realistic, location = store(control31, topics, privacy, realistic, location)
# topics, privacy, realistic, location = store(control32, topics, privacy, realistic, location)
# topics, privacy, realistic, location = store(control33, topics, privacy, realistic, location)
# topics, privacy, realistic, location = store(control34, topics, privacy, realistic, location)
# topics, privacy, realistic, location = store(control35, topics, privacy, realistic, location)
# topics, privacy, realistic, location = store(control36, topics, privacy, realistic, location)
# topics, privacy, realistic, location = store(control37, topics, privacy, realistic, location)
# topics, privacy, realistic, location = store(control38, topics, privacy, realistic, location)
# topics, privacy, realistic, location = store(control39, topics, privacy, realistic, location)
# topics, privacy, realistic, location = store(control40, topics, privacy, realistic, location)
# topics, privacy, realistic, location = store(control41, topics, privacy, realistic, location)
# topics, privacy, realistic, location = store(control42, topics, privacy, realistic, location)
topics, privacy, realistic, location = store(scenario1, topics, privacy, realistic, location)
topics, privacy, realistic, location = store(scenario2, topics, privacy, realistic, location)
topics, privacy, realistic, location = store(scenario3, topics, privacy, realistic, location)
topics, privacy, realistic, location = store(scenario4, topics, privacy, realistic, location)
topics, privacy, realistic, location = store(scenario5, topics, privacy, realistic, location)
topics, privacy, realistic, location = store(scenario6, topics, privacy, realistic, location)
topics, privacy, realistic, location = store(scenario7, topics, privacy, realistic, location)
topics, privacy, realistic, location = store(scenario8, topics, privacy, realistic, location)
topics, privacy, realistic, location = store(scenario9, topics, privacy, realistic, location)
topics, privacy, realistic, location = store(scenario10, topics, privacy, realistic, location)
topics, privacy, realistic, location = store(scenario11, topics, privacy, realistic, location)
topics, privacy, realistic, location = store(scenario12, topics, privacy, realistic, location)
topics, privacy, realistic, location = store(scenario13, topics, privacy, realistic, location)
topics, privacy, realistic, location = store(scenario14, topics, privacy, realistic, location)
topics, privacy, realistic, location = store(scenario15, topics, privacy, realistic, location)
topics, privacy, realistic, location = store(scenario16, topics, privacy, realistic, location)
# print(topics, privacy, realistic, location)
randoms = []
for i in range(0, 3):
    new_random_number = randrange(0, 16)
    while new_random_number in randoms:
        new_random_number = randrange(0, 16)
    randoms.append(new_random_number)
    print(topics[new_random_number], privacy[new_random_number], realistic[new_random_number], location[new_random_number], new_random_number)
