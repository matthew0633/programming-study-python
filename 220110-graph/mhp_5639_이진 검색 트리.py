"""
idea : 
- 전위순회 결과에서 루트보다 큰 노드 발견 시 Tree 분할
- 분할된 Tree에서 후위순회(왼->오->root) 반복

* 전위순회(preorder) : root -> left -> right
* 중위순회(inorder) : left -> root -> right
* 후위순회(postorder) : left -> right -> root 


참고 : 
https://rccode.tistory.com/entry/Python-%EB%B0%B1%EC%A4%80-5639%EB%B2%88-%EC%9D%B4%EC%A7%84-%EA%B2%80%EC%83%89-%ED%8A%B8%EB%A6%AC
"""

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def get_postorder(nums):

    """
    CASE : 3가지

    1) left, right, root : right node 필수 포함 (tree 분할) 
        -> get_postorder(LEFT_TREE) + get_postorder(RIGHT_TREE) + ROOT
    2) left, root : right node 없음 (tree 분할X) 
        -> get_postorder(LEFT_TREE) + ROOT
    3) root : left, right node 모두 없음 (leaf node)
        -> ROOT 
    """
    
    # CASE 3
    if len(nums)<=1:
        return nums

    # CASE 1 
    for i in range(1, len(nums)):
        if nums[0]<nums[i]:
            # tree 분할
            return get_postorder(nums[1:i]) + get_postorder(nums[i:]) + [nums[0]]
    
    # CASE 2
    return get_postorder(nums[1:]) + [nums[0]]

nums = []
while True:
    try:
        nums.append(int(input()))
    except:
        break

nums = get_postorder(nums)
print('\n'.join(map(str, nums)))
