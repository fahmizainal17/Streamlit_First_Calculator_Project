from calculator_function import add, subtract, multiply, divide, expo
import streamlit as st

def calculator():
    st.title("Professional Calculator")

    # Set the overall layout
    col1, col2, col3 = st.columns(3)

    # Get user input
    with col1:
        num1 = st.number_input("Enter the first number:", min_value=0.00, step=0.01)

    with col2:
        operation = st.selectbox("Select operation:", ["+", "-", "*", "/", "**"])

    with col3:
        num2 = st.number_input("Enter the second number:")

    # Perform calculation
    result = 0
    if operation == "+":
        result = add(num1, num2)
    elif operation == "-":
        result = subtract(num1, num2)
    elif operation == "*":
        result = multiply(num1, num2)
    elif operation == "/":
        if num2 != 0:  # Check for division by zero
            result = divide(num1, num2)
        else:
            st.error("Error: Division by zero")
    elif operation == "**":
        result = expo(num1, num2)

    # Display result
    st.write("Result:", result)

if __name__ == "__main__":
    calculator()
