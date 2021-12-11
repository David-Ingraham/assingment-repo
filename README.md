# assingment-repo

Part 1: 
Automatinge calculations for the loan portfolio summaries.

First, let's start with some calculations on a list of prices for 5 loans.

    1. Using the `len` function to calculate the total number of loans in the list.
    
    2. Using the `sum` function to calculate the total of all loans in the list.
    
    3. Using the sum of all loans and the total number of loans, calculate the average loan price.
    
    4. Printing all calculations with descriptive messages.
    
    
    ![Screen Shot 2021-12-11 at 11 26 18 AM](https://user-images.githubusercontent.com/86004112/145684048-794250bb-f182-4741-9480-4e66efc0a1b3.png)


Part 2: 
Analyze the loan to determine the investment evaluation.
Using more detailed data on one of these loans, this calculates a "fair price" for what this loan would be worth.
1. Using get() on the dictionary of additional information to extract the Future Value and 
Remaining Months on the loan.
    a. Saving these values as variables called `future_value` and `remaining_months`.
    b. Printing each variable.
    @NOTE:
    Future Value: The amount of money the borrower has to pay back upon maturity of the loan 
    (a.k.a. "Face Value")
    **Remaining Months**: The remaining maturity (in months) before the loan needs to be fully repaid.
2. Using the formula for Present Value to calculate a "fair value" of the loan.
 Using a minimum required return of 20% as the discount rate.
3. Writing a conditional statement (an if-else statement) to decide if the present 
value represents the loan's fair value.
    a. If the present value of the loan is greater than or equal to the cost, then it prints a 
    message that says the loan is worth at least the cost to buy it.
    b. Else, the present value of the loan is less than the loan cost, 
    then it prints a message that says that the loan is too expensive and not worth the price.
    @NOTE:
    If Present Value represents the loan's fair value (given the required minimum return of 20%),
     does it make sense to buy the loan at its current cost?
     
![Screen Shot 2021-12-11 at 11 35 54 AM](https://user-images.githubusercontent.com/86004112/145684370-53131aa8-e8a5-4247-aa75-0a80361bad4a.png)





Part 3: 

Performing financial calculations using python functions.

1. Defining a new function that will be used to calculate present value.
    a. This function includes parameters for `future_value`, `remaining_months`, and the `annual_discount_rate`
    b. The function returns the `present_value` for the loan.
2. the function calculates the present value of the new loan given below.
    a. Using an `annual_discount_rate` of 0.2 for this new loan calculation.
    
    
![Screen Shot 2021-12-11 at 11 38 46 AM](https://user-images.githubusercontent.com/86004112/145684464-366df680-e763-4d0e-8ae7-59c8c034fc52.png)





Part 4: Conditional filter for lists of loans.

In this section, a loop iterates through a series of loans and selects only the inexpensive loans.

1. Creating a new, empty list called `inexpensive_loans`.
2.  for loop to select each loan from a list of loans.
    a. Inside the for loop, is an if-statement to determine if the loan_price is less than 500
    b. If the loan_price is less than or equal to 500 then that loan is appended to the `inexpensive_loans` list.
3. Printing the list of inexpensive_loans.




![Screen Shot 2021-12-11 at 11 40 29 AM](https://user-images.githubusercontent.com/86004112/145684502-04c1fd05-6930-4119-be47-e12cb7a1ed2a.png)





Part 5: Save the results.

Output this list of inexpensive loans to a csv file
    1. Use `with open` to open a new CSV file.
        a. Create a `csvwriter` using the `csv` library.
        b. Use the new csvwriter to write the header variable as the first row.
        c. Use a for loop to iterate through each loan in `inexpensive_loans`.
            i. Use the csvwriter to write the `loan.values()` to a row in the CSV file.
            
            
            
![Screen Shot 2021-12-11 at 11 43 56 AM](https://user-images.githubusercontent.com/86004112/145684607-be60c0e7-5765-4279-a445-549fb98012b9.png)


