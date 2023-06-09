# Homework 08, file 3 (2023.06.08)
# Actions

from PythonQA_HW_08_2_AccEngine import AccountingEngine

if __name__ == '__main__':
    acc_engine = AccountingEngine()
    income = 600
    taxes = acc_engine.calc_se_taxes(income)
    print(taxes)
