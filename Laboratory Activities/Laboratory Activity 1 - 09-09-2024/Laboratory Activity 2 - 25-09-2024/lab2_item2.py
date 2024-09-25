def calculate_discount(amount):
    
    if amount > 5000:
        discount_percentage = 0.10  
    else:
        discount_percentage = 0.05  
    
    discount = amount * discount_percentage
    final_price = amount - discount
    
    return discount, final_price

def main():
    while True:
        try:
            purchase_amount = float(input("Enter the total purchase amount: "))
            
            discount, final_price = calculate_discount(purchase_amount)
            
            print(f"Initial Purchase Amount: {purchase_amount:.2f}")
            print(f"Discount: {discount:.2f}")
            print(f"Final Price: {final_price:.2f}")
            
            retry = input("Do you want to try again? (yes/no): ").strip().lower()
            if retry != "yes":
                print("Thank you!")
                break
        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    main()
