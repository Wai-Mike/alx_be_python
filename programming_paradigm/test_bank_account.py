
from bank_account import BankAccount

def test_bank_account():
   
    print("=== Bank Account Testing ===\n")
    
    account = BankAccount(100)
    print("Created account with initial balance of $100")
    account.display_balance()
    print()
    
    print("Testing deposit of $50...")
    account.deposit(50)
    print("Deposited: $50")
    account.display_balance()
    print()
    
    
    print("Testing withdrawal of $20...")
    if account.withdraw(20):
        print("Withdrew: $20")
    else:
        print("Insufficient funds.")
    account.display_balance()
    print()
    
    
    print("Testing withdrawal of $150...")
    if account.withdraw(150):
        print("Withdrew: $150")
    else:
        print("Insufficient funds.")
    account.display_balance()
    print()
    
    
    print("Final balance check:")
    account.display_balance()

if __name__ == "__main__":
    test_bank_account()
