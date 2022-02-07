# **Expense Tracker V2**

#### *by Gavin Dsouza*

#### gavin_dsouza@live.com

---

## **Features**

---

### Tracking and evaluating your daily expenses has never been this easy

#### In a few basic steps, you'll have an overview of where you're spending the most. You'll be able to:

* Evaluate your daily expenses based on **month**, **year(s)** and even **categories.**

* Generates charts graphs to visually compare your expenses.
  
* Export your data as an Excel Document *(.xlsx)*.

---

## **Installation**

---

### To get started, you'll have to install a few packages

* [Python 3.10](https://www.python.org/downloads/)

##### *(note: check the box that says "Add Python 3.10 to PATH" at the end of the installation)*

* Open command prompt as admin and pip install the following:
  * >pip install matplotlib
  * >pip install pandas
  * >pip install webbrowser
  * >pip install pathlib
  * >pip install tkinter
  * >pip install PIL
* Once you've downloaded my repository, go into the folder from command prompt and type:
  >python start_up.py
  * This will launch the Quick setup where you can enter your own categories or leave the defaults.
  ![quick_setup](https://github.com/gaaaaaaavin/ExpenseTrackerV2/blob/main/images/quick_setup.png)

##### *(note: make sure that each category is one word; ✘medical care ✓ **medical**)*

---

## **Getting Started**

---

### **Saving an Entry:**

  * ![entry](https://github.com/gaaaaaaavin/ExpenseTrackerV2/blob/main/images/help/entry_index.png)

  1) **Add date** Todays date is selected by default based on your system's clock, but you'll be able to enter any date of your choice.
  2) **Add a name** for your expense. This wont be used by my application, but you might find labeling your entries if you ever want to look it up.
  3) **Add amount** The value here will be used to evaluate your data in the *View Data* menu.
  4) **Select a Category** You'll be able to choose a category based on what you've entered in the *Quick Setup* window. Again, this will be used to evaluate your data in the *View Data* menu.
  5) **Click *Save*** to save your entry. all your data will be stored locally in *logs\exp_log.txt* and a unique Index wll be assigned to it.

##### *(note: the ***Clear*** button will clear entry instead of selecting each box and hitting backspace multiple times)*

### **View Data**

* By Index:
  * ![viewbyIndex](https://github.com/gaaaaaaavin/ExpenseTrackerV2/blob/main/images/help/view_by_index.png)
  1) **Type the Index**
  2) **Click *Search***
  3) **Clicking *Delete Entry*** is an optional feature, incase you've accidentally saved an entry with incorrect infomation.
  4) **Click *Delete {index}*** acts as a confirmation before the entry is removed from your logs.
* By Month:
  * ![viewbyMonth](https://github.com/gaaaaaaavin/ExpenseTrackerV2/blob/main/images/help/view_by_month.png)
  1) A pop up window will appear in which you'll have to **select the Year and Month** you wish to view.
  2) Clicking the **View Pie Chart** will generate a pie chart of that month that shows the percentage of you expenses based on it's categories.
* By Year:
  * ![viewbyYear](https://github.com/gaaaaaaavin/ExpenseTrackerV2/blob/main/images/help/view_by_year.png)
  1) **Select Year(s)**
  2) **Click *View/Update Data*** This will generate a Textbox on your right with every entry in the range you've selected. It will also generate another popup window with the sum total of each selected year, including a total of years if more than one year is selected.

##### ***Clicking *View Graph*** will generate a graph that you can use as a visual difference between the selected years*

##### ***Clicking *View/Update Data*** again after selecting a different year(s) will update the textbox)*

* By Category:
  * ![viewbyCategory](https://github.com/gaaaaaaavin/ExpenseTrackerV2/blob/main/images/help/view_by_category.png)
   **See *By Year* as it covers the same thing except instead of months of the year, it evaluates your categories.**
* All:  
  * ![viewAll](https://github.com/gaaaaaaavin/ExpenseTrackerV2/blob/main/images/help/view_by_year.png)
 Here you'll find every entry you've entered.

---
Enjoy keeping track of your spending.
