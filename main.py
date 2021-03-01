'''main'''
from myMath import myArithmetic

a1 = float(input("輸入第一個數字 :"))
a2 = float(input("輸入第二個數字 :"))
a3 = float(input("輸入第三個數字 :"))
a4 = float(input("輸入第四個數字 :"))
a5 = float(input("輸入第五個數字 :"))

a = myArithmetic.myAdd(a1,a2)
a = myArithmetic.myAdd(a,a3)
a = myArithmetic.myAdd(a,a4)
a = myArithmetic.myAdd(a,a5)
ans = myArithmetic.myDiv(a,5)
print("平均數為",ans)
