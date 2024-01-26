import streamlit as st
import creds

def main():
    st.title("Greeting App")
    
    # Get user input for name
    name = creds.var
    
    # Display greeting
    if name:
        st.write(f"Hey, {name}!")

if __name__ == "__main__":
    main()
