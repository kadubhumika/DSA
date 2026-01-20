import random
import time

users = {}
otp_stores = {}
def login():
    email = input("Email: ")
    password = input("Password: ")
    if email not in users:
        print("User not found")
        return
    if password != users[email]['password']:
        print("Incorrect password")
        print("Please try again")
        print("Login unsuccessful!!")
        return
    else:
        print("Login successful")
def sign_up():
    email = input("Enter your email: ")
    if email in users:
        print("Email already registered")
    password = input("Enter your password: ")
    if otp_scan(email):
        users[email] = {

            "password": password,
            "verified": True,
        }
        print("Login successful")
    else:
        print("Login failed")

def otp_scan(email):
    otp = random.randint(100000, 999999)
    otp_stores[email] = otp
    print(f"OTP send to {email}: {otp}")
    time.sleep(1)
    user_otp = int(input("Enter your OTP: "))
    if otp_scan[email] == user_otp:
        print("OTP verified")
        return True
    else:
        print("OTP NOT verified")
        return False
def main():
    while True:
        print("Auth System")
        print("1. Login")
        print("2. Sign up")
        print("3. Nothing")
        choice = input("Enter your choice: ")
        if choice == "1":
            login()
        elif choice == "2":
            sign_up()
        else:
            print("Thank you!")
if __name__ == "__main__":
    main()

