# Write your solution here
def longest_series_of_neighbours(words : list):
    current_streak = 1
    max_streak = 1

    for x in range(len(words) - 1):
        if abs(words[x] - words[x + 1]) == 1:
            current_streak += 1
        else:
            current_streak = 1
            
        max_streak = max(max_streak, current_streak)


    return max_streak

if __name__ == "__main__":
    my_list = [1, 3, 5, 7, 10, 11, 14, 15, 19, 20, 21, 22, 23, 24, 25]
    print(longest_series_of_neighbours(my_list))