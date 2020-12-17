from collections import defaultdict


class Solution:
    def countOfAtoms(self, formula: str) -> str:
        result = defaultdict(int)
        atom_list = []
        kuo_stack = []
        left, right = 0, 1
        while (left<len(formula)):
            if ord('A') <= ord(formula[left]) <= ord('Z'):
                atom_name = formula[left]
                right=left+1
                if right<len(formula) and formula[right].islower():
                    atom_name += formula[right]
                    right += 1
                number = ""
                while (right < len(formula) and formula[right].isdigit()):
                    number += formula[right]
                    right += 1
                if len(atom_name) > 0 and len(number) > 0:
                    atom_list.append([atom_name, int(number), len(kuo_stack)])
                else:
                    atom_list.append([atom_name, 1, len(kuo_stack)])
            elif formula[left]=='(':
                kuo_stack.append('(')
            elif formula[left]==')':
                right=left+1
                number=""
                while(right<len(formula) and formula[right].isdigit()):
                    number+=formula[right]
                    right+=1
                if len(number)>0:
                    for i in range(len(atom_list)-1,-1,-1):
                        if atom_list[i][2]==len(kuo_stack):
                            atom_list[i][1]*=int(number)
                            atom_list[i][2]-=1
                        else:
                            break
                    kuo_stack.pop()
            left+=1
        for i in atom_list:
            result[i[0]]+=i[1]
        ans=""
        for i in sorted(result):
            if result[i]==1:
                ans=ans+i
            else:
                ans=ans + i+str(result[i])
        return ans


s = Solution()
print(s.countOfAtoms("N"))
