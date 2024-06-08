'''
streamlit run C:/Users/Usuario/Desktop/dashboard1.py
'''

import streamlit as st

def add_numbers(num1, num2):
  """Calculates the sum of two numbers.

  Args:
      num1: The first number.
      num2: The second number.

  Returns:
      The sum of num1 and num2.
  """
  return num1 + num2

st.title("Simple 2-Number Calculator")

# Get user input for numbers
num1 = 1


num2 = 2

# Calculate and display the sum
if st.button("Calculate"):
  result = add_numbers(num1, num2)
  st.success(f"The sum is: {result}")






