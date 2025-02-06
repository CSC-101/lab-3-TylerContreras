more = [x + 1 for x in [1,2,3,4]]     # [1+1=2, 2+1=3, 3+1=4, 4+1=5]
print()                               # [2,3,4,5]


def square(n:int) -> int:
    return n * n                           # 1 -> 1*1=1, 2 -> 2*2 = 4, 3 -> 3*3=9, 4 -> 4*4=16



squares = [square(x) for x in [1,2,3,4]]   # [1, 4, 9, 16] When the n's above is ran through the function, it will multiply it by itself essentially squaring n
print()

def check(n:int) -> bool:
    return n > 2                             # [1 -> False, 2 -> False, 3 -> True, 4 -> True]


answer = [x for x in range(5) if check(x)]   # What is the value of answer?
print()


def inc(m:int) -> int:
    return m + 1                             # [inc(3) = 4, inc(4) = 5]

def check(n:int) -> bool:
    return n > 2                             # [check(0) = False, check(1) = False, check(2) = False, check(3) = True, check(4) = True]


answer = [inc(x) for x in range(5) if check(x)]   # answer = [4, 5]
print()

def tally(nums:list[int]) -> int:
    total = 0
    for num in nums:                #     num  total
        total = total + num         # 1st	4	4
                                    # 2nd	9	13
                                    # 3rd	2	15
                                    # 4th	1	16
    return total

result = tally([4, 9, 2, 1])   # result = 16


def copy(nums:list[int]) -> list[int]:
    new_list = []
    for idx in range(len(nums)): #   Iteration  idx    new_list
        new_list.append(nums[idx])      # 1st	0		[4]
                                        # 2nd	1		[4, 9]
                                        # 3rd	2		[4, 9, 2]
                                        # 4th	3		[4, 9, 2, 1]
    return new_list                    # tally computes the sum of elements while copy creates a new list identical to nums.
                                       # tally uses an integer while copy uses a list.

result = copy([4, 9, 2, 1])



def increment_all(nums:list[int]) -> list[int]:
    new_list = []
    for value in nums:                #iteration   value    new_list
        new_list.append(value + 1)      # 1st	   4  		[5]
                                        # 2nd	   9	  	[5, 10]
                                        # 3rd	   2		[5, 10, 3]
                                        # 4th	   1		[5, 10, 3, 2]

result = increment_all([4, 9, 2, 1])
