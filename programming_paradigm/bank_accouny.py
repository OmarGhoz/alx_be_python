class BankAccount:
    """
    Represents a simple bank account with deposit, withdrawal, and balance display functionalities.
    """

    def __init__(self, initial_balance=0.0):
        """
        Initializes a BankAccount object with the given initial balance (default: 0.0).

        Args:
            initial_balance (float, optional): The initial balance of the account. Defaults to 0.0.
        """

        self.balance = initial_balance  # Encapsulate balance attribute

    def deposit(self, amount):
        """
        Deposits the specified amount to the account balance.

        Args:
            amount (float): The amount to be deposited.
        """

        if amount <= 0:
            print("Invalid deposit amount: Must be positive.")
            return

        self.balance += amount
        print(f"Deposited: ${amount:.2f}")  # Format for two decimal places

    def withdraw(self, amount):
        """
        Attempts to withdraw the specified amount from the account balance.

        Args:
            amount (float): The amount to be withdrawn.

        Returns:
            bool: True if withdrawal is successful, False otherwise.
        """

        if amount <= 0:
            print("Invalid withdrawal amount: Must be positive.")
            return False

        if amount > self.balance:
            print("Insufficient funds.")
            return False

        self.balance -= amount
        print(f"Withdrew: ${amount:.2f}")  # Format for two decimal places
        return True

    def display_balance(self):
        """
        Prints the current balance in a user-friendly format.
        """

        print(f"Current Balance: ${self.balance:.2f}")  # Format for two decimal places
