class Solution:
    def myAtoi(self, s: str) -> int:
        
        result = ''
        check_in_range = [-2**31, 2**31 - 1]
        
        for i in s:
            if i == '+' or i == '-':
                result += i
                
                # if i == '0':
                #     continue
                
            else:
                try:
                    a = int(i)
                    result += i
                    
                except Exception:
                    continue
                                
        # print(f'the parsed integer is {int(result)}')
        result = int(result)
        if result > -2**31 or result < 2**31 - 1:
            return result
        
        else:
            return result