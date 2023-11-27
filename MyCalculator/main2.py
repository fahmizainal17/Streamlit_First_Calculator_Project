from calculator_function import add, subtract, multiply, divide, expo
import streamlit as st

def calculator():
    st.title("My First Project on Streamlit: Calculator")

    # Get user input
    num1 = st.number_input("Enter the first number:", min_value=0.00, step=0.01)
    num2 = st.number_input("Enter the second number:")

    # Perform calculation
    result = 0

    # Calculator buttons and styling
    st.markdown("""
        <style>
            .calculator-container {
                display: grid;
                grid-template-columns: repeat(4, 1fr);
                gap: 8px;
                margin-top: 20px;
            }
            .calculator-button {
                padding: 10px;
                font-size: 18px;
                text-align: center;
                background-color: #3498db;
                color: #ffffff;
                border: none;
                cursor: pointer;
                border-radius: 4px;
            }
        </style>
    """, unsafe_allow_html=True)

    # Calculator buttons
    button_layout = st.empty()
    button_layout.markdown('<div class="calculator-container">'
                           '<button class="calculator-button" onclick="setOperation(\'+\')">+</button>'
                           '<button class="calculator-button" onclick="setOperation(\'-\')">-</button>'
                           '<button class="calculator-button" onclick="setOperation(\'*\')">*</button>'
                           '<button class="calculator-button" onclick="setOperation(\'/\')">/</button>'
                           '<button class="calculator-button" onclick="setOperation(\'**\')">**</button>'
                           '</div>', unsafe_allow_html=True)

    # JavaScript to update the selected operation
    st.markdown("""
        <script>
            function setOperation(op) {
                document.getElementById("operation").value = op;
            }
        </script>
    """, unsafe_allow_html=True)

    # Display result
    if st.button("Calculate"):
        operation = st.text_input("Selected Operation:", key="operation")
        if operation:
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
