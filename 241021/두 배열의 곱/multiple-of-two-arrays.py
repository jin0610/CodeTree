nums1 = [list(map(int, input().split())) for _ in range(3)]
blank = input()
nums2 = [list(map(int, input().split())) for _ in range(3)]

for i in range(3):
    result = [i*j for i,j in zip(nums1[i], nums2[i])]
    print(*result)