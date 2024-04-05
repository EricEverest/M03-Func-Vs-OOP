
class Solution:
    def sort012(self,arr,n):
        # code here
      { 
        int ptr1 = 0, ptr2 = n-1;
        
        int i = 0;
        
        while(i <= ptr2) {
            if(a[i] == 0) {
                swap(a[i++], a[ptr1++]);
            else if(a[i] == 2) {
                swap(a[i], a[ptr2--]);
            else {
                i++;
            }
        }
    }
};

#------------------------

class Solution:	
	def binarysearch(self, arr, n, k):
		# code here

      {
        int l = 0 , r = n - 1;
        int pos = -1;
        
        while(l <= r)
        {
            int mid = (l + r)/2;
            if(arr[mid] == k)
            {
                pos = mid;
                break;
            }
            if(arr[mid] > k)
            {
                r = mid - 1;
            }
            else
            {
                l = mid + 1;
            }
        }
        return pos;
    }
    };