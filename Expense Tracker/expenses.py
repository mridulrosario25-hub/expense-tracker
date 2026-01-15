import streamlit as st

def add_expense(amount, category, note):
    with open("expenses.txt", "a") as file:
        file.write(f"{amount}, {category}, {note}\n")
    print("Expenses added successfully!")

def view_expenses():
    the_list = []
    try:
        with open("expenses.txt","r") as file:
            expense = file.readlines()
        
        if not expense:
            print("No expenses found.")
            return
    
        print("-----All Expenses-----")
        for i in expense:
            amount, category, note = i.strip().split(',')
            the_list.append((amount,category,note))
    
    except FileNotFoundError:
        pass

    return the_list
    
st.title("$Expenses Tracker$")

amount = st.number_input("Enter Amount: ", min_value=0)
category = st.text_input("Enter Category: ")
note = st.text_input("Personal Note (What did you buy this time?): ")

if st.button("Add Expenses"):
    if category == "":
        st.error("Category cannot be empty.")
    
    elif note == "":
        st.error("NOTE DOWN WHAT IT IS!!")

    else:
        add_expense(amount,category,note)
        st.success("Expense added!")


st.subheader("All Expenses")
expenses = view_expenses()

if expenses:
    for amt, cat, note in expenses:
        col1, col2, col3 = st.columns([1,1,3])
        col1.write(f"Rs{amt} -")
        col2.write(cat)
        col3.write(note)
else:
    st.info("No expenses added yet.")
