def backspace_compare(S: str, T: str):
        i,j = len(S)-1,len(T)-1
        cnt1 = cnt2 = 0
        while i>=0 or j>=0:
            while i>=0:
                if S[i]=='#':
                    i -= 1
                    cnt1 += 1
                elif S[i]!='#' and cnt1>0:
                    cnt1 -= 1
                    i -= 1
                else:
                    break
            while j>=0:
                if T[j]=='#':
                    j -= 1
                    cnt2 += 1
                elif T[j]!='#' and cnt2>0:
                    j -= 1
                    cnt2 -= 1
                else:
                    break
            if (i>=0 and j<0) or (i<0 and j>=0):
                return False
            if i>=0 and j>=0 and S[i]!=T[j]:
                return False
            i -= 1
            j -= 1
        return True
str1 = "ab#c"
str2 = "ad#c"
print(backspace_compare(str1, str2))