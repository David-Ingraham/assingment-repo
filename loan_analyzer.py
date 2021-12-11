# coding: utf-8
import csv
from pathlib import Path



loan_costs = [500, 600, 200, 1000, 450]


volume_of_loans = len(loan_costs)
print(f'Our firm has issued {volume_of_loans} loans')


total_value_of_issued_loans = sum(loan_costs)
print(f'The value of all of issued loans is ${total_value_of_issued_loans}')


average_loan_amount = total_value_of_issued_loans / volume_of_loans
print(f'The average loan amount is ${average_loan_amount}')


loan = {
    "loan_price": 500,
    "remaining_months": 9,
    "repayment_interval": "bullet",
    "future_value": 1000,
}


remaining_months = loan.get('remaining_months')

future_value = loan.get('future_value')

print (f' your remaining months are {remaining_months}')

print (f' your future value is {future_value}')

discount_rate = 0.2


present_value = future_value / (1 + (discount_rate/12)) ** remaining_months

if present_value >= loan_costs:
    print('this loan is worth at least worth the cost to buy it, its a fair value')
else:
    print('this loan is too expensive, its not a fair value')





"""
"""

new_loan = {
    "loan_price": 800,
    "remaining_months": 12,
    "repayment_interval": "bullet",
    "future_value": 1000,
}
remaining_months = new_loan["remaining_months"]
future_value = new_loan["future_value"]
discount_rate = 0.2


def present_value(future_value, reamaining_months, annual_discount_rate):
    present_value = future_value / (1 + discount_rate/12) ** remaining_months
    return present_value

present_value_of_new_loan = present_value(1000,12,0.2)
rounded_present_value_of_new_loan = round(present_value_of_new_loan, 2)
print(f'the present value of the new loan is {rounded_present_value_of_new_loan}')



present_value_of_new_loan = present_value(1000,12,0.2)
rounded_present_value_of_new_loan = round(present_value_of_new_loan, 2)
print(f'the present value of the new loan is {rounded_present_value_of_new_loan}')


"""
"""

loans = [
    {
        "loan_price": 700,
        "remaining_months": 9,
        "repayment_interval": "monthly",
        "future_value": 1000,
    },
    {
        "loan_price": 500,
        "remaining_months": 13,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 200,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 900,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
]


inexpensive_loans = []


for loan in loans:
    if loan['loan_price'] <=500:
        inexpensive_loans.append(loan)
        
print(inexpensive_loans)





header = ["loan_price", "remaining_months", "repayment_interval", "future_value"]


output_path = Path("inexpensive_loans.csv")


with open (output_path, 'w', newline='') as f:
    writer = csv.writer(f)
    writer = csv.DictWriter(f, fieldnames=header)
    writer.writeheader()
    for loans in inexpensive_loans:
        writer.writerow({
            'loan_price' : loans['loan_price'],
            'remaining_months': loans['remaining_months'],
            'repayment_interval': loans['repayment_interval'],
            'future_value' : loan['future_value']})
            

                        