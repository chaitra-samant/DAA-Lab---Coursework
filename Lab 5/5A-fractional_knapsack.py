dataset = [
    [2000, 1, 2], [485, 25, 9], [500, 1, 1], [1475, 37, 6], [290, 12, 3],
    [740, 21, 7], [1230, 9, 2], [540, 35, 8], [1550, 10, 10], [870, 29, 3],
    [295, 49, 5], [1165, 7, 6], [390, 18, 9], [785, 27, 7], [975, 45, 4],
    [1455, 8, 8], [605, 6, 2], [695, 54, 6], [615, 28, 9], [730, 4, 5],
    [1350, 11, 7], [570, 16, 8], [1120, 22, 3], [1375, 42, 10], [410, 5, 7],
    [845, 12, 4], [1215, 14, 9], [785, 11, 6], [470, 31, 9], [545, 23, 2],
    [1330, 48, 8], [605, 40, 5], [1485, 21, 7], [910, 15, 4], [765, 9, 10],
    [1345, 27, 3], [425, 46, 8], [825, 8, 6], [1295, 5, 9], [210, 50, 3],
    [1360, 18, 7], [895, 32, 5], [665, 37, 10], [765, 6, 8], [930, 17, 3],
    [1115, 14, 7], [400, 25, 4], [285, 48, 9], [835, 44, 6], [515, 3, 8],
    [1410, 20, 9], [905, 7, 4], [755, 19, 10], [1310, 16, 5], [435, 14, 7],
    [1385, 5, 9], [985, 28, 4], [735, 24, 8], [1495, 35, 3], [765, 42, 9],
    [280, 46, 6], [505, 53, 7], [1190, 55, 10], [895, 3, 6], [685, 39, 8],
    [1025, 13, 7], [780, 56, 9], [765, 16, 5], [1505, 4, 3], [725, 17, 8],
    [1395, 12, 6], [435, 45, 9], [215, 34, 2], [1175, 33, 10], [910, 29, 5],
    [695, 8, 7], [1215, 18, 9], [1325, 11, 6], [535, 52, 4], [1270, 27, 5],
    [755, 41, 8], [1430, 22, 7], [1200, 36, 10], [980, 47, 6], [1540, 34, 3],
    [870, 7, 8], [485, 9, 4], [1255, 43, 9], [735, 32, 6], [585, 13, 10],
    [1010, 50, 7], [1050, 26, 8], [505, 19, 5], [815, 36, 4], [475, 21, 7]
]




def check(items):
    """
    This function checks if the input given is valid and all conditions are satisfied

    Arguments:
    items (list): The dataset with all the information
    
    Returns:
    Errors : (if any) Will display corresponding errors else continue program execution
    """
    for ind,item in enumerate(items):
        if item[0] < 0:
            print("Price of item can't be negative")
            exit(1)
        if item[1] < 0:
            print("Weight cannot be negative")
            exit(1)
        if item[2] < 0:
            print("Shelf Life cannot be negative")
            exit(1)


def ptow_ratio(items):
    """
    This function calculates price to weight ratio for each element and appends it to the list of each element and sorts them in order of shelf life and p/w ratio
    
    Arguments:
    items (list): Dataset in which we need to implement fractional knapsack

    Returns:
    None
    """
    if not items:
        print("Dataset is Empty")
        exit(1)
    for item in items:
        if item[1] != 0:
            val = round(item[0]/item[1],2)
        else:
            val = 0
        item.append(val)

    items.sort(key=lambda item: (item[2] , -item[-1]))


def max_benefit(items,weight):
    """
    This function fills the items in the knapsack and calculates maximum benefit

    Arguments:
    items (list): Sorted Dataset of all items
    weight (int): Maximum weight of the knapsack(truck)

    Returns:
    None
    """
    benefit = 0
    
    print("Items loaded in the truck")
    for ind,item in enumerate(items):
        if item[1] <= weight:
            print(f"Weight added:{item[1]}/{item[1]}    Shelf Life:{item[2]}    P/W Ratio:{item[3]} ")
            weight -=item[1]
            benefit += item[-1]*item[1]

        else:
            benefit += weight*item[-1]
            print(f"Weight added:{weight}/{item[1]}    Shelf Life:{item[2]}    P/W Ratio:{item[3]} ")
            weight=0
        
        if weight == 0:
            break
    benefit = round(benefit,2)
    print(f"Total Benefit: {benefit}")
         

#Driver Code
capacity = 20
check(dataset)
ptow_ratio(dataset)
max_benefit(dataset,capacity)







