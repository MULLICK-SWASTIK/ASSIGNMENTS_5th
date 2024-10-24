def unique_permutations(string):
    result = set()
    permute(string, "", result)
    return sorted(result)


def permute(remaining, current_permutation, result):
    if len(remaining) == 0:
        result.add(current_permutation)
    else:
        for i in range(len(remaining)):
            new_permutation = current_permutation + remaining[i]
            # print(remaining[:i], remaining[i + 1 :], new_permutation)
            new_remaining = remaining[:i] + remaining[i + 1 :]
            permute(new_remaining, new_permutation, result)
    # print("iteration")


if __name__ == "__main__":
    input_string = input("Enter a string: ")
    unique_perms = unique_permutations(input_string)
    print(f"Unique permutations of the string '{input_string}':")
    print(unique_perms)

'''
OUTPUT
Enter a string: abc
Unique permutations of the string 'abc':
['abc', 'acb', 'bac', 'bca', 'cab', 'cba']
'''