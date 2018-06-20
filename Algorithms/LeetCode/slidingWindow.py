'''
Given an list of nums, there is a sliding window of size k which is moving from the very left of the array to the very right.

A window of k size is put against this numbers. Each time the sliding window moves right by one position.

For example,
nums = [2,4,10,9,8,5,2,7], k= 5
result = [10,10,10,9]

'''

class maxQueue(object) :
    def __init__(self):
        '''
            creates an empty queue and a list to store maximum values
        '''
        self.queue = []
        self.maximum_vals = []

    def append_to_queue(self,num):
        '''
        It takes a number as input and append it to the queue and maximum_vals
        Also, pop all the elements that are less than current number
        :param num: number to be added into the queue
        :return: None
        '''
        self.queue.append(num)

        # remove all the elements from the last that are less than the current number
        # append element to the last
        while len(self.maximum_vals) != 0 and self.maximum_vals[-1] < num :
            self.maximum_vals.pop()

        # append current val at the end
        self.maximum_vals.append(num)

    def pop_from_queue(self):
        '''
            remove the element from the queue
        :return: None
        '''
        if self.queue[0] == self.maximum_vals[0] :
            del self.maximum_vals[0]

        del self.queue[0]

    def get_max(self):
        '''
        Time O(1)
        :return: maximum number from the current list
        '''
        return self.maximum_vals[0]

def slidingWindow(nums, k):
    # edge cases
    if len(nums) == 0 :
        return []
    elif len(nums) < k :
        return [max(nums)]
    elif k == 1 :
        return nums

    mq = maxQueue()
    result = []

    # first window
    for i in range(k):
        mq.append_to_queue(nums[i])
    result.append(mq.get_max())

    # rest of the windows
    for i in range(k, len(nums)):
        mq.pop_from_queue()
        mq.append_to_queue(nums[i])
        result.append(mq.get_max())

    return result

# Test Cases
import unittest
class MyTest(unittest.TestCase):
    def test_compare_window(self):
        self.assertEqual(slidingWindow([1,4,10,5,9,8,11,10,17],5), [10, 10, 11, 11, 17])
    def test_1_k(self):
        self.assertEqual(slidingWindow([1, 4, 10, 5, 9], 1), [1, 4, 10, 5, 9])
    def test_window_greater_than_list(self):
        self.assertEqual(slidingWindow([1, 4, 10, 5, 9, 8, 11, 10, 17], 10), [17])

if __name__ == '__main__':
    MyTest.test_compare_window(unittest.main())
    MyTest.test_1_k(unittest.main())
    MyTest.test_window_greater_than_list(unittest.main())
