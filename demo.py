# # while 1:
# #     n, m = map(int, input().split())
# #     res = []
# #     for i in range(m):
# #         a, b, c = map(int, input().split())
# #         if c == 1:
# #             tmp = [a, b] if a < b else [b, a]
# #             res.append(tmp)
# #     res.sort()
# #     s = set()
# #     s.add(1)
# #     for i in res:
# #         if i[0] in s:
# #             s.add(i[1])
# #     print(len(s) - 1)
# # import math
# # while 1:
# #     n,m= map(int,input().split())
# #     sums=0
# #     for i in range(m):
# #         sums+=n
# #         n=math.sqrt(n)
# #         n=round(n,2)
# #     print(round(sums,2))
#
#
#
# def is_waterflower(num):
#     tmp=num
#     sums=0
#     while tmp>0:
#         a=tmp%10
#         sums=sums+a*a*a
#         tmp=tmp//10
#     return sums==num
#
# while 1:
#     m,n=map(int,input().split())
#     res=[]
#     for i in range(m,n+1):
#         if i==370:
#             print(i)
#         if is_waterflower(i):
#             res.append(str(i))
#     if len(res)>0:
#         ans=" ".join(res)
#         print(ans)
#     else:
#         print("no")
# str_list=input().split()
# stack1=[]
# stack2=[]
# opt=("or","and")
# bools={"true":True,"false":False}
# for i in str_list:
#     if i in opt:
#         stack1.append(i)
#     else:
#         stack2.append(bools[i])
# msg=""
# while len(stack1)>0:
#     o=stack1.pop(0)
#     if len(stack2)>0:
#         p1=stack2.pop(0)
#     else:
#         msg="error"
#         break
#     if len(stack2)>0:
#         p2=stack2.pop(0)
#     else:
#         msg="error"
#         break
#     if o=="or":
#         stack2.append(p1 or p2)
#     if o=="and":
#         stack2.append(p1 and p2)
# if len(stack2)!=1 or msg=="error":
#     print("error")
# else:
#     s=stack2.pop()
#     if s:
#         print("true")
#     else:
#         print("false")
# def compute(p,t):
#     index1=0
#     index2=0
#     while index1<len(p) and index2<len(t):
#         if p[index1]=="?" or p[index1]==t[index2]:
#             index1+=1
#             index2+=1
#         elif p[index1]=="*":
#             for i in range(index2,len(t)):
#                 if compute(p[index1+1:], t[i:]):
#                     return True
#             return False
#         elif p[index1]!=t[index2]:
#             return False
#     if index1>=len(p) and index2>=len(p):
#         return True
#     else:
#         return False
# p=input()
# t=input()
#
# if compute(p, t):
#     print(1)
# else:
#     print(0)
import heapq

s = [1, 8, 5, 8, 4, 65, 1, 6, 3, 4]
heapq.heapify(s)
print(s)
