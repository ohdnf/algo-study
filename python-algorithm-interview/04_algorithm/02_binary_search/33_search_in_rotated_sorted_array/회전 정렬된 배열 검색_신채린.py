def search(self, nums: 'List[int]', target: 'int') -> 'bool':
        
        if not nums :
            return False
        l, r = 0, len(nums)-1
        
        while l < r :
            mid = (l+r)//2
            if nums[mid] == target :
                return True
            
            # 왼쪽 정렬.
            if nums[l] < nums[mid] :
                if nums[l]<=target<nums[mid]:
                    r = mid
                else :
                    l = mid+1
            # 오른쪽 정렬.        
            elif nums[l] > nums[mid] :
                if nums[mid] < target <= nums[r]:
                    l = mid+1
                else :
                    r = mid
            else :
                l += 1
                
        return nums[l] == target