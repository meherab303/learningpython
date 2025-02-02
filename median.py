def median(nums1,nums2):
    # lists=sorted(list1+list2)
    # lenght=int(len(lists)/2)
    # mediann=float((lists[lenght-1]+lists[lenght])/2) if len(lists)%2==0 else (lists[lenght])
    # return mediann
    # if len(lists)%2==0:

    #     mediann=(lists[lenght-1]+lists[lenght])/2
        
    #     return mediann
    # else:
    #     mediann=(lists[lenght+1])
   
        lists = sorted(nums1 + nums2)  # Merge and sort the two lists
        length = len(lists)
        mid = length // 2  # Find the middle index

        if length % 2 == 0:
            return (lists[mid - 1] + lists[mid]) / 2.0  # Average of two middle elements
        else:
            return lists[mid]  # Return the middle element



print(median([1,2],[3,4]))