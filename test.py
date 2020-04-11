import csv
import operator

ls = {}
ans = []


class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None


class List:
    def __init__(self):
        self.head = None


with open('test.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        ls[row['friend']] = float(row['money'])


def optz_splitter(num_splitter, prize, num_voucher):
    is_even = (number_voucher % 2) == 0
 #   if (is_even and num_spliiter ):

def dp(rem, sol, idx, data, prize_ls, size, curr_ptr):
 #   if (len(sol) > 21):
 #       print(sol)
 #       print("data_length:", len(data))
 #       print("index:", idx)
    if rem < 0:
        return
    if rem == 0 and (len(sol) == 23):
        print(sol)
        exit(0)
        curr_ptr = 0
    if curr_ptr == len(prize_ls):
        curr_ptr = 0
    for i in range(idx, len(data)):
        if i > idx and data[i-1][1] == data[i][1]:
            continue
        if (prize_ls[curr_ptr] * data[i][1]) > rem:
            break
#        if i == 22:
#            print("curr_ptr:", curr_ptr)
        if (curr_ptr < len(prize_ls)):
            prize = prize_ls[curr_ptr] * data[i][1]
            remainder = rem - prize
            dp(remainder, sol + [(data[i], prize_ls[curr_ptr], prize, remainder)], i + 1, data, prize_ls, size, curr_ptr + 1)


def main():

    # sort
    sorted_tup = sorted(ls.items(), key=operator.itemgetter(1))

    # print(sorted_tup)
    expected_val = float(input("Enter the value you want: "))

    # Get possible list
    sorted_list = list(sorted_tup)
    
    sample_prize = [100, 80, 50, 10, 10, 10, 10, 10, 10,
                    10, 10, 10, 10, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]

    for counter in range(0, len(sample_prize)):
        print(sample_prize)
        dp(expected_val, [], 0, sorted_list, sample_prize, len(sample_prize), 0)
        temp = sample_prize.pop(0)
        sample_prize.append(temp)

    for element in ans:
        print(element)


if __name__ == "__main__":
    main()
