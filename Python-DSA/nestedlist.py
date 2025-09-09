if __name__ == '__main__':
    name_hashmap = {}

    for _ in range(int(input())):
        name = input()
        score = float(input())
        # store names in list for each score
        if score not in name_hashmap:
            name_hashmap[score] = [name]  # create list with first name
        else:
            name_hashmap[score].append(name)  # append more names

    # sort the scores
    sorted_scores = sorted(name_hashmap.keys())
    second_score = sorted_scores[1]

    
    result = sorted(name_hashmap[second_score])

    for name in result:
        print(name)
