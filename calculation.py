# _*_ coding:utf-8 _*_
__author__ = 'JiangKui'
__date__ = '2018/1/19 19:51'

import math
class expensesSummary:
    """
    目前全部开支项目

    """
    def Level1(self):
        total = 0
        level1 = dict({"房租":4000})
        for k ,v in level1.items():
            print (k ,v)
            total = v + total
        print ("小计"+str(total))
        return total

    def Level2(self):
        total = 0
        print("基本生活开支：吃饭、交通费、话费、水电、燃气、网费")
        level2  = dict({"吃饭":3000,"交通费":600,"话费":120,"水电":200,"燃气":50,"网费":58})
        for k ,v in level2.items():
            print (k ,v)
            total = v + total
        print ("小计"+str(total))
        return total

    def level3(self):
        total = 0
        print("Advance生活开支：水果、化妆品、酒水饮料、四季衣物、约会、书籍、电脑会员")
        level3  = dict({"水果":150,"化妆品":300,"酒水饮料":100,"四季衣物":200,"约会":200,"书籍":208,"电脑会员":50})
        for k ,v in level3.items():
            print (k ,v)
            total = v + total
        print ("小计"+str(total))
        return total

    def level4 (self):
        total = 0
        print ("人情经费、探亲经费、电子设备升级经费、养老经费、教育经费、医疗经费、旅游经费")
        level4  = dict({"人情经费":200,"探亲经费":200,"电子设备升级经费":500,"养老经费":100,"教育经费":50,"医疗经费":100,"旅游经费":100})
        for k ,v in level4.items():
            print (k ,v)
            total = v + total
        print ("小计"+str(total))
        return total

    def level5(self):
        total = 0
        print ("长期账户、中期账户、短期账户、活期账户")
        level5  = dict({"长期账户":0,"中期账户":0,"短期账户":0,"活期账户":0})
        for k ,v in level5.items():
            print (k ,v)
            total = v + total
        print ("小计"+str(total))
        return total

class incomeSummary:
    """
    目前全部收入项目

    """
    def work_salary(self):
        salary = 23000
        return salary
    def schoolarship(self):
        total = 2400+1000
        return total
    def government_fund(self):
        caf = 800
        an_year_caf = caf * 12
        total = an_year_caf + 40000
        return total


"""
假设工资按15%/年递增
"""
    # sum = 0
    # i = 1
    # salary = 23000
    #     #int(input("第一年工资"))
    # l = 1
    #
    #
    # while i < 6:
    #     total_salary = salary *13
    #     income1 = salary - 4000 * l
    #     total_salary1 = income1 *13
    #     print("第" + str(i) + "年工资: " + str(salary))
    #     print ("房租费用为"+str(4000*l)+"\n去除房租剩余工资"+str(income1))
    #     print("\n年度1级可支配工资" +str(total_salary)+"去除房租")
    #     print("\n年度2级可支配工资" +str(total_salary1)+"\n")
    #     print("")
    #
    #     salary = salary * 1.15
    #     l = l * 1.1
    #     i = i + 1
    #     sum = sum +total_salary

sum_cost = expensesSummary.Level1(0)+expensesSummary.Level2(0)+expensesSummary.level3(0)+expensesSummary.level4(0)
sum_income = incomeSummary.schoolarship(0)+incomeSummary.government_fund(0)+incomeSummary.work_salary(0)
print ("总计支出"+str(sum_cost))
print ("总计收入"+str(sum_income))
print ("总计结余"+str(sum_income - sum_cost))

