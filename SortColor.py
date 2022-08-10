 """
 Since we have to keep the space complexity constant and we know that numbers will always be 0,1 or 2 so we just found their frequency and append accordingly.
 Time Complexity = O(n) , Space = O(1)
 """
  
  def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        red = nums.count(0)
        white = nums.count(1)
        blue = nums.count(2) 
        for h in range(red):
            nums[h] = 0
        for j in range(red,red + white):
            nums[j] = 1
        for k in range(red+white , red+white+blue  ):
            nums[k] = 2
        print(nums)
