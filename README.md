# ProjectPassword
Password manager from Dr Angela of @londonappbrewery
logo source: https://www.pngegg.com/en/png-emkrt/download?width=200

About
Simple password manager that I learnt from Dr Angela of @londonappbrewery. Part of the 100 Days of Code: The Complete Python Pro Bootcamp for 2022. 
Customised the code to display my understanding of the syntax used in this mini project. Mainly the GUI but I believe more can be done to make it better.

Project Password
GUI
Made using Tkinter. 

Saving details
User can store username and password. The two data will be stored as json format and can be retrieved from specific account. 
Example: Account: Amazon
         Username: Haziq
         Password: Password
#Nil entry
Programme can recognise nil entry in username or password and will return error messagebox to prompt user to enter values.

Account Retrieval
Account will be the key. Username and password will be the values. User has to input Account(case sensative) to retrieve Username and Password by
clicking on the search button. The values will be displayed in the message box. 
#Json file not found
Messagebox will return error as file not found. Most likely code was run the first time and Json file was not created.
#Account not found
Messagebox will return error if account not found in the json file.

***AREAS FOR IMPROVEMENT***
- Getting the widget to the right size and placement.
- Resizing the canvas when windows being expanded.


         
