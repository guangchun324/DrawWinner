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


def dp(rem, sol, idx, data, prize_ls, size, curr_ptr):
    if rem < 0:
        return
    if rem == 0 and (len(sol) == 23):
        ans.append(sol)
        print(sol)
    for i in range(idx, len(data)):
        if i > idx and data[i-1][1] == data[i][1]:
            continue
        if (prize_ls[curr_ptr] * data[i][1]) > rem:
            break
        if (curr_ptr < 22):
            dp(rem - (prize_ls[curr_ptr] * data[i][1]), sol + [data[i]], i +
               1, data, prize_ls, size, curr_ptr + 1)


def main():

    # sort
    sorted_tup = sorted(ls.items(), key=operator.itemgetter(1))

    # print(sorted_tup)
    expected_val = float(input("Enter the value you want: "))

    # Get possible list
    sorted_list = list(sorted_tup)

    sample_prize = [100, 80, 50, 10, 10, 10, 10, 10, 10,
                    10, 10, 10, 10, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]

    head = ListNode(sample_prize[0])
    curr = head

    for prize in sample_prize:
        node = ListNode(prize)
        curr.next = node
        curr = curr.next

    curr.next = head
    dp(expected_val, [], 0, sorted_list, sample_prize, len(sample_prize), 0)

    for element in ans:
        print(element)


if __name__ == "__main__":
    main()
