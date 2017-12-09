'''
leetcode : 739

'''


class Solution(object):
    def dailyTemperatures(self, arr):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        s = self.createStack()
        element = 0
        next = 0
        l = [0 for i in arr]

        self.push(s, [arr[0], 0])

        for i in range(1, len(arr), 1):
            next = arr[i]
            if self.isEmpty(s) == False:
                [element, index] = self.pop(s)
                while element < next:
                    l[index] = (i - index)
                    if self.isEmpty(s) == True:
                        break
                    [element, index] = self.pop(s)

                if element >= next:
                    self.push(s, [element, index])

            self.push(s, [next, i])

        while self.isEmpty(s) == False:
            [element, index] = self.pop(s)
            l[index] = 0

        return l

    def createStack(self):
        stack = []
        return stack

    def isEmpty(self, stack):
        return len(stack) == 0

    def push(self, stack, x):
        stack.append(x)

    def pop(self, stack):
        if self.isEmpty(stack):
            return (0, 0)
        else:
            return stack.pop()