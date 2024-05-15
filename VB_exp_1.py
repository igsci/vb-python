from abc import ABC, abstractmethod

class DataOperation(ABC):
    """
    Abstract base class for data operations.
    """

    @abstractmethod
    def perform_operation(self, input_number: int) -> int:
        """
        Abstract method to be implemented by derived classes.
        Performs an operation on the input number.

        Args:
            input_number (int): The input number.

        Returns:
            int: The result of the operation.
        """
        pass


class AdditionOperation(DataOperation):
    """
    Concrete class for performing addition operation.
    """

    def perform_operation(self, input_number: int) -> int:
        """
        Performs addition by adding 10 to the input number.

        Args:
            input_number (int): The input number.

        Returns:
            int: The result of the addition operation.
        """
        return input_number + 10


class SubtractionOperation(DataOperation):
    """
    Concrete class for performing subtraction operation.
    """

    def perform_operation(self, input_number: int) -> int:
        """
        Performs subtraction by subtracting 5 from the input number.

        Args:
            input_number (int): The input number.

        Returns:
            int: The result of the subtraction operation.
        """
        return input_number - 5


def update_database(operation_name: str, input_number: int, output_number: int) -> None:
    """
    Prints the operation details to the console.
    This is a placeholder for the actual database update code.

    Args:
        operation_name (str): The name of the operation performed.
        input_number (int): The input number used in the operation.
        output_number (int): The result of the operation.
    """
    print(f"Updating database with operation: {operation_name}, Input: {input_number}, Output: {output_number}")


def main():
    """
    Main function of the program.
    """

    try:
        # Greet the user
        print("Welcome to Data Operation Program")

        # Get the operation type from the user
        operation_type = input("Enter operation type (A for Addition, S for Subtraction): ").upper()

        # Get the input number from the user
        input_number = int(input("Enter a number: "))

        # Create the operation object based on user's choice
        operation: DataOperation = None
        if operation_type == "A":
            operation = AdditionOperation()
        elif operation_type == "S":
            operation = SubtractionOperation()
        else:
            print("Invalid operation type.")
            return

        # Perform the operation and get the result
        output_number = operation.perform_operation(input_number)

        # Display the result to the user
        print(f"Result: {output_number}")

        # Update the database with operation details
        update_database(operation_type, input_number, output_number)

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()