#creating a simple function
def my_function(fname, lname):
  print(f"{fname} {lname}")

my_function("Trenisha", "Goslee")

def getting_to_the_money(rich):
  print(rich + "Min")

getting_to_the_money("money")


def feel_better(name):
  print (f"You're doing a great job, {name}")

feel_better("Adah")
feel_better("Trenisha")

def mergeSortTwoLists(list1, list2):
    sorted = []
    i = j = 0
    while i < len(list1) and j < len(list2): 
        if list1[i] < list2[j]:
            sorted.append(list1[i])
            i += 1
        else:
            sorted.append(list2[j])
            j += 1
    if i < len(list1):
        sorted += list1[i:]
    elif j < len(list2):
        sorted += list2[j:]
    return sorted