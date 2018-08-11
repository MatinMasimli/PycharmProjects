# 03-Function Practice Exercises

def master_yoda(text):
    mList = text.split()
    rvList = []
    for ind, word in enumerate(mList):
        rvList.append(mList[len(mList) - 1 - ind])
    print(rvList)
    return " ".join(rvList)

def has_33(nums):

    count = 1
    while count <= len(nums):
        if nums[count] == nums[count+1]:
            return True
        else:
            return False

def paper_doll(text):

    output = ''
    for ch in text:
       output = output + ch * 3

    return output

def summer_69(arr):
    sumAll = 0
    myList = []
    i = 0

    while i < len(arr):

        if arr[i] != 6:
            myList.append(arr[i])
        elif arr[i] == 6:
            while arr[i] != 9:
                i += 1
                continue
            sumAll = sum(myList) - 9
        i += 1

    sumAll = sum(myList)
    print(sumAll)
    return sumAll

def spy_game(nums):
    count = 0

    for val in nums:
        if val != 0 and val != 7:
            continue
        elif val == 0:
            count += 1
        elif val == 7:
            if count != 2:
                return False
            else:
                return True

def count_primes(num):
    count = 0
    basicPrimes = [2,3,5,7]

    for n in range(2, num):
        if n % n == 0 and n % 1 == 0 and n >= 10:
            if n % 2 != 0 and n % 3 != 0 and n % 5 != 0 and n % 7 != 0:
                count += 1
        else:
            if n in basicPrimes:
                count += 1
    return count

def print_big(letter):
    patterns = {1: '  *  ', 2: ' * * ', 3: '*   *', 4: '*****', 5: '**** ', 6: '   * ', 7: ' *   ', 8: '*   * ',
                9: '*    '}
    alphabet = {'A': [1, 2, 4, 3, 3], 'B': [5, 3, 5, 3, 5], 'C': [4, 9, 9, 9, 4], 'D': [5, 3, 3, 3, 5],
                'E': [4, 9, 4, 9, 4]}
    for pattern in alphabet[letter.upper()]:
        print(patterns[pattern])

def main():
    print("Here")
    master_yoda('I am home')
    has_33([1, 3, 3])
    print(paper_doll('Hello'))
    print(summer_69([2, 1, 6, 9, 11, 9]))
    print(spy_game([1,7,2,0,4,5,0]))
    print(count_primes(100))
    print_big('a')

if __name__== "__main__":
  main()
