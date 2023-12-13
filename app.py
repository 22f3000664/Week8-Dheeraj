# Importing necessary libraries
import streamlit as st

# Function to find the greatest of three numbers
def find_greatest(num1, num2, num3):
    return max(num1, num2, num3)

# Streamlit app
def main():
    # Setting up the app title
    st.title("Find Greatest of Three Numbers")

    # Input for the three numbers
    num1 = st.number_input("Enter the first number:", step=1)
    num2 = st.number_input("Enter the second number:", step=1)
    num3 = st.number_input("Enter the third number:", step=1)

    # Button to find the greatest number
    if st.button("Find Greatest"):
        # Call the function to find the greatest number
        result = find_greatest(num1, num2, num3)

        # Display the result
        st.success(f"The greatest number is: {result}")

# Run the app
if __name__ == "__main__":
    main()
