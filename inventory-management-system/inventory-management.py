import pandas as pd
import datetime

path='<path-of-file>/Inventory.xlsx'
df=pd.read_excel(path)

def view_inventory():
    print(df)

def add_inventory():
    global df

    print("--Input product details--")
    id=int(input("Product ID: "))
    name=input("Product Name: ")
    category=input("Category: ")
    quantity=int(input("Quantity: "))
    price=int(input("Price: "))
    date=datetime.datetime.today()

    new_row={'Product ID':id,"Product Name":name,"Category":category,"Quantity":quantity,"Price":price,"Last Updated":date}
    new_df=pd.DataFrame([new_row])
    df=pd.concat([df,new_df],ignore_index=True)
    try:
        df.to_excel(path,index=False)
        print("Item Added!")
    except PermissionError:
        print("Please close the file and try again...")

def update_inventory():
    global df 

    id=int(input("Enter product id to update: "))
    if df[df['Product ID']==id].empty:
        print("No existing item with Product ID:",id)
        return
    print("\n",df[df['Product ID']==id],"\n")
    col=int(input("Select column to update:\n1. Category\n2. Quantity\n3. Price\n"))
    
    if col==1:
        new_val=input("New Category: ")
        df.loc[df["Product ID"] == id, "Category"] = new_val
        df.to_excel(path,index=False)
        print("Inventory Updated Successfully!")
    elif col==2:
        new_val=input("New Quantity: ")
        df.loc[df["Product ID"] == id, "Quantity"] = new_val
        df.to_excel(path,index=False)
        print("Inventory Updated Successfully!")
    elif col==3:
        new_val=input("New Price: ")
        df.loc[df["Product ID"] == id, "Category"] = new_val
        df.to_excel(path,index=False)
        print("Inventory Updated Successfully!")
    else:
        print("Invalid Input...")

def remove_item():
    global df

    id=int(input("Enter product id: "))
    print("\n",df.loc[df['Product ID']==id],"\n")
    confirm=input("Delete this row? Y/N: ")
    if confirm=="Y" or confirm=="y":
        df=df.drop(df[df['Product ID']==id].index)
        try:
            df.to_excel(path,index=False)
            print("Item Removed")
        except PermissionError:
            print("Close File and try again...")
    elif confirm=="N" or confirm=="n":
        print("Exiting...")
    else:
        print("Invalid Input: Deletion Failed...")

exit=0

while(exit==0):
    op=int(input("\n---Enter Operation to perform---\n1. View Inventory\n2. Add Item\n3. Update Item\n4. Remove Item\n5. Exit\n"))
    match op:
        case 1:
            view_inventory()
        case 2:
            add_inventory()
        case 3:
            update_inventory()    
        case 4:
            remove_item()
        case 5:
            exit=1
            print("Exiting Program...")
        case _:
            print("Invalid Operation: Execution failed...")
