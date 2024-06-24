import heapq

def pairs(nums1, nums2, k):
    if not nums1 or not nums2 or k == 0:
        return []

    min_heap = []
    result = []

  
    for j in range(len(nums2)):
        heapq.heappush(min_heap, (nums1[0] + nums2[j], 0, j))

    
    while min_heap and len(result) < k:
        sum, i, j = heapq.heappop(min_heap)
        result.append([nums1[i], nums2[j]])

     
        if i + 1 < len(nums1):
            heapq.heappush(min_heap, (nums1[i + 1] + nums2[j], i + 1, j))

    return result

nums1 = [1, 7, 11]
nums2 = [2, 4, 6]
k = 3
print(pairs(nums1, nums2, k))
