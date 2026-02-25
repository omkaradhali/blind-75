"""

Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

Example 1:
Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Example 2:
Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]

"""

def main(arr: list) -> list:
    result = []

    left = 1
    left_prod = [1]
    print(left_prod)
    # [1,1,2,6,24]

    right = 1
    right_prod = [1] 
    print(right_prod)
    # [24, 24,12, 4, 1]

    # left to right
    for idx, item in enumerate(arr):
        left = left * item
        left_prod.append(left)
    
    print(left_prod)

    for idx in range(len(arr) - 1, -1, -1):
        right = right * arr[idx]
        right_prod.insert(0, right)
    
    print(right_prod)

    for idx, item in enumerate(arr):
        result.append(left_prod[idx] * right_prod[idx+1])

    print(result)
    return result


# Creating just the result array and then calculating inplace.
# Instead of creating an array of prefix and postfix calculate prefix and postfix and assign it to a variable. 
# While calculating prefix (left to right) result will be prefix and then you update prefix for next step. 
# while calculating postfix we need to multiply postfix with current element in arr to get product, then update the post fix by postifx * actual item in array
def main2(arr: list) -> list:
    result = [1] * len(arr)
    
    prefix = 1
    # adding prefix product for each entry
    # For input [1,2,3,4] the prefix array should be [1, 1, 2, 6]
    for i in range(len(arr)):
        # add the calculated prefix in previous step to index
        result[i] = prefix
        
        # Calculate new prefix for next position
        prefix = prefix * arr[i]
    
    postfix = 1
    for i in range(len(arr) - 1, -1, -1):
        
        # multiply previously calculated postfix in previous step to current item in result so that you multiple prefix and postfix.
        result[i] = postfix * result[i]
        
        # Calculate new postfix for next position
        postfix = postfix * arr[i]
    
    print(result)

if __name__ == "__main__":
    # main2([1,2,3,4])
    main([-1,1,0,-3,3])