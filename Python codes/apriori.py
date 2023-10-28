from itertools import combinations
# test case 1(3)
sample = {
    'TID' : 'ITEMSKO',
    't1' : ['M','O','N', 'K', 'E', 'Y'],
    't2' : ['D','O','N', 'K', 'E', 'Y'],
    't3' : ['M', 'A', 'K', 'E'],
    't4' : ['M', 'U', 'C', 'K', 'Y'],
    't5' : ['C', 'O', 'O', 'K', 'I', 'E'],
    '' : ''
} # for now it is hard coded then it will be gathered as input
# min_support = int(input())

#test case 2(2)
# sample = {'t1' : ['1', '3', '4'],'t2' : ['2', '3', '5'],'t3' : ['1', '2', '3', '5'],'t4' : ['2', '5'],'t5' : ['1', '3', '5']}
# test case 3(3)
# sample = {
#     't1' : ['i1', 'i2', 'i3'],
#     't2' : ['i2', 'i3', 'i4'],
#     't3' : ['i4', 'i5'],
#     't4' : ['i1', 'i2', 'i4'],
#     't5' : ['i1', 'i2', 'i3', 'i5'],
#     't6' : ['i1', 'i2', 'i3', 'i4']
# }
# test case 4(2)|(3)
# sample = {
#     't1' : ['Milk', 'Onion', 'Nutmeg', 'Kidney Beans', 'Eggs', 'Yogurt'],
#     't2' : ['Dill', 'Onion', 'Nutmeg', 'Kidney Beans', 'Eggs', 'Yogurt'],
#     't3' : ['Milk', 'Apple', 'Kidney Beans', 'Eggs'],
#     't4' : ['Milk', 'Unicorn', 'Corn', 'Kidney Beans', 'Yogurt'],
#     't5' : ['Corn', 'Onion', 'Onion', 'Ice cream', 'Eggs']
# }

# test case 5(2)
# sample = {
#     't100' : ['i1', 'i2', 'i5'],
#     't200' : ['i2', 'i4'],
#     't300' : ['i2', 'i3'],
#     't400' : ['i1', 'i2', 'i4'],
#     't500' : ['i1', 'i3'],
#     't600' : ['i2', 'i3'],
#     't700' : ['i1', 'i3'],
#     't800' : ['i1', 'i2', 'i3', 'i5'],
#     't900' : ['i1', 'i2', 'i3']
# }

# test case 6(2)
# sample = {
#     '10' : ['A', 'C', 'D'],
#     '20' : ['B', 'C', 'E'],
#     '30' : ['A', 'B', 'C', 'E'],
#     '40' : ['B', 'E']
# }
min_support = 3 # minimum support count of the problem
allFrequencyTables = dict()
allCandidateTables = dict()
full = ''
another = False # boolean value to navigate the frequency table
noOfCombination = 2 # to combine the item set - initially it is 2 (for every problem)

def pruningData(data):
    for key, value in data.items():
        if key != '' and type(value) == list:
            data[key] = list(dict.fromkeys(value)) # removing the repeated data occuring for the same transaction
    return data # returning the new pruned data


sample = pruningData(sample) # reassigning it to the sample data for testing


def generateFrequencyTable(data, newData = None): # parameters are raw or input data and newData which is the combined list from the candidate table
    frequency_table = dict()
    global another
    if not another: # for first frequency table this condition will get executed only once because it is only for the generation of first frequency table
        for key, value in data.items(): # calculating frequency for first table
            for item in value:
                if item not in frequency_table.keys():
                    frequency_table[item] = 1
                else:
                    frequency_table[item] += 1
        another = True
       
        return frequency_table # returning the first frequency table
    if another: # this will not get executed for first time but it will for remaining of all frequency table
        for values in newData:
            for items in data.values():
                if all(value in tuple(items) for value in values): # checking all the combined itemsets are occuring in a single transaction
                    if values not in frequency_table.keys():
                        frequency_table[values] = 1
                    else:
                        frequency_table[values] += 1
    return frequency_table # return this frequency table except first



def candidateGeneration(data : dict) -> dict: # parametes is getting the data which is a frequency table which is generarted from generateFrequencyTable() function
    global min_support
    candidate_table = dict()
    for key, value in data.items():
        if value < min_support: # checking each value supports the minimum threshold value if it isn't just ignore it
            continue
        candidate_table[key] = value
    return candidate_table # returning the generated candidate table


def combineItemsets(data : dict) -> list: # to combine the item to itemset data as a parameter which is a candidate table which is generated from candidateGeneration() function
    newList = list()
    global noOfCombination
    listTOCombine = [key for key in data] # this is enough for the first time (single data set)
    if noOfCombination >= 3: # from the second time to combine the itemset
        for itemset in listTOCombine:
            for item in itemset:
                if item in newList:
                    continue
                newList.append(item)
        listTOCombine = newList
    combinedList = list(combinations(listTOCombine, noOfCombination)) # here all the item are get combined by the combination(without repitition)
    noOfCombination += 1 # incrementing the no of items to get combined it will get increment by 1 each time
    return combinedList # retuirning the combined items set as a list of tuples

frequencyTable = generateFrequencyTable(sample) # first frequiency table
allFrequencyTables['F1'] = frequencyTable
full += 'Frequency Table 1 : \n' + str(frequencyTable) + '\n\n'
f,c = 2, 1

while True:# loop until break
    candidateTable = candidateGeneration(frequencyTable) # generate candidate table
    full += 'Candidate Table {} : \n'.format(c) + str(candidateTable) + '\n\n'
    if len(candidateTable.keys()) < 1 or all(i < min_support for i in candidateTable.values()): # checking is there no more possible way to combine or to support the minimum support value
        break # if it is then break out of the loop else continue the process
    combinedItemsets = combineItemsets(candidateTable) # getting the combined itemset ad store it in combinedITemset
    frequencyTable = generateFrequencyTable(sample, combinedItemsets) # generate frequency table from f2 until last
    full += 'Frequency Table {} : \n'.format(f) + str(frequencyTable) + '\n\n'
    finalCandidateTable = candidateTable # it will store the previously stored candidate table if the loop break out to see the output whether is it correct or not
    allFrequencyTables['F{}'.format(f)] = frequencyTable
    allCandidateTables['C{}'.format(c)] = candidateTable
    f += 1
    c += 1
print(finalCandidateTable, 'final')# showing the final output
# print(full)

# print(allCandidateTables)
"""
to do list
candidate generation function:
    In that we check frequent item sets with min_support and it should be greater
combinating function : 
    in this from candidate table we generate in a new itemset by combinating them
calculating frequency of an item:
    to create a frequency table for each itemsets
do this until the all the value of frequent itemset should equal to min_support afer candidate generation
save this all this into a file
"""
def nonEmptySubset(arr: tuple) -> list:
    subsets = []
    [subsets.extend(list(combinations(arr,n))) for n in range(1, len(arr))]
    return subsets
# subset = []
# [subset.extend(nonEmptySubset(s)) for s in finalCandidateTable.keys()]
# print(subset)


def support(setToFind : tuple) -> int:
    length = len(setToFind)
    if length == 1:
        for i in setToFind:
            supportValue = allFrequencyTables['F1'][i]
    if length > 1:
        try:
            supportValue = allFrequencyTables['F{}'.format(str(length))][setToFind]
        except KeyError:
            supportValue = allFrequencyTables['F{}'.format(str(length))][setToFind[::-1]]
    return supportValue

# for set1 in subset:
#     for set2 in subset:
#         if set(set1).issubset(set(set2)) or len(set1) == len(set2) or set(set2).issubset(set(set1)):
#             continue
#         rules['{}'.format(i)] = [set1, set2]
#         i += 1
#         support(set1)
#         print('i', i)

def associationRule(subset : dict) -> dict:
    i = 1
    wholeRules = {}
    # rules = {}
    for key, value in subset.items():
        rules ={}
        if len(key) == 2:
            for set1 in value:
                for set2 in value:
                    if set(set1).issubset(set(set2)) or set(set2).issubset(set(set1)):
                        continue
                    main_support = finalCandidateTable[key]
                    divider = support(set1)
                    validRule = (main_support / divider) * 100
                    rules['{}'.format(i)] = [str(set(set1)) + '->' + str(set(set2)) + ' = {:.4f}%'.format(validRule)]
                    i += 1
                    print('i', i)
            wholeRules[key] = rules
        if len(key) > 2:
            for set1 in value:
                for set2 in value:
                    if set(set1).issubset(set(set2)) or len(set1) == len(set2) or set(set2).issubset(set(set1)):
                        continue
                    main_support = finalCandidateTable[key]
                    divider = support(set1)
                    validRule = (main_support / divider) * 100
                    rules['{}'.format(i)] = [str(set(set1)) + '->' + str(set(set2)) + ' = {:.4f}%'.format(validRule)]
                    i += 1
                    # print('i', i)
            wholeRules[key] = rules
    return wholeRules
subset = {}
for key in finalCandidateTable.keys():
    subset[key] = nonEmptySubset(key)
print(subset, 'sub')
allAssocaitionRules = associationRule(subset)
print(allAssocaitionRules)
