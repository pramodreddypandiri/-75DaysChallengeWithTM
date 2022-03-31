class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        #timeComplexity=O(N) in worst case
        #spaceComplexity=O(1)
        #reverse the array
        digits=digits[::-1]
        i=0
        carry=1
        while carry==1:
            if i<len(digits):
                # if digit is 9 ,make it zero ,take carry as 1
                if digits[i]==9:
                        digits[i]=0
                        carry=1
                # if digit is not 9 ,then just incriment,take carry as 0
                else:
                    digits[i]+=1
                    carry=0
                i=i+1    
            # after completing array,if carry exist,then append (carry) and set carry to zero
            else:
                digits.append(carry)
                carry=0
        return digits[::-1]    
            