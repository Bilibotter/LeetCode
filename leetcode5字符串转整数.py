class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        s = ''
        flag = ''
        str = str.strip()
        if not str:
            return 0
        if str[0].isdigit():
            for i in str:
                if i.isdigit():
                    s += i
                else:
                    return int(s) if int(s).bit_length() < 32 else 2**31-1
            return int(s) if int(s).bit_length() < 32 else 2**31-1

        if str[0] == '-' or str[0] == '+':
            flag = str[0]
            if len(str) == 1 or not str[1].isdigit():
                return 0
            for i in str[1:]:
                if i.isdigit():
                    s += i
                elif flag == '-':
                    return int(flag+s) if int(s).bit_length() < 32 else -2**31
                else:
                    return int(flag+s) if int(s).bit_length() < 32 else 2**31-1
            if flag == '-':
                return int(flag+s) if int(s).bit_length() < 32 else -2**31
            else:
                return int(flag + s) if int(s).bit_length() < 32 else 2 ** 31 - 1
        return 0

s = Solution()
print(s.myAtoi("91283472332"))
