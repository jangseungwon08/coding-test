def solution(nums):
    take = len(nums) // 2
    phone_dict = {}
    for i in nums:
        phone_dict[i] = 1
    if take <= len(phone_dict):
        return take
    return len(phone_dict)