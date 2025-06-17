# Write your solution here
def list_sum(a, b : list):
    new_list = []
    counter = 0

    while counter < len(a):
        new_list.append(a[counter] + b[counter])
        counter += 1
        
    return new_list

if __name__ == "__main__":
    a = [1, 2, 3]
    b = [7, 8, 9]
    print(list_sum(a, b)) # [8, 10, 12]

