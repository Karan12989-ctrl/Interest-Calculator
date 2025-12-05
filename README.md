# 📊 Interest Calculator (Simple & Compound Interest)

This project is a beginner-friendly **Python Interest Calculator** that helps users compute:

- ✔ Simple Interest (SI)  
- ✔ Compound Interest (CI)  
- ✔ Total Amount after interest  

Users enter the principal amount, rate of interest, and time period. The program then calculates and displays the results clearly.

---

## 🚀 Features

- 🧮 Calculates **Simple Interest**  
- 🔁 Calculates **Compound Interest**  
- 🎯 Accurate results (formatted to 2 decimal places)  
- 💡 Simple and beginner-friendly code  
- 🖥️ Console-based interaction  

---

## 🧮 Formula Used

### ✔ Simple Interest  
SI = (P × R × T) / 100

shell
Copy code

### ✔ Compound Interest  
A = P × (1 + R/100)^T
CI = A - P

python
Copy code

---

## 📝 Code Overview

```python
def simple_interest(p, r, t):
    return (p * r * t) / 100

def compound_interest(p, r, t):
    amount = p * (1 + r/100) ** t
    return amount - p

print("---- Interest Calculator ----")
print("1. Simple Interest")
print("2. Compound Interest")

choice = int(input("Enter your choice (1 or 2): "))

principal = float(input("Enter Principal Amount: "))
rate = float(input("Enter Rate of Interest (%): "))
time = float(input("Enter Time (in years): "))

if choice == 1:
    si = simple_interest(principal, rate, time)
    print(f"Simple Interest = {si:.2f}")
    print(f"Total Amount = {principal + si:.2f}")

elif choice == 2:
    ci = compound_interest(principal, rate, time)
    print(f"Compound Interest = {ci:.2f}")
    print(f"Total Amount = {principal + ci:.2f}")

else:
    print("Invalid Choice! Please enter 1 or 2.")
📌 Example Output
java
Copy code
---- Interest Calculator ----
1. Simple Interest
2. Compound Interest
Enter your choice (1 or 2): 2
Enter Principal Amount: 1000
Enter Rate of Interest (%): 10
Enter Time (in years): 2
Compound Interest = 210.00
Total Amount = 1210.00
🧑‍💻 Author
Karan

📄 License
This project is open-source.
You are free to use, modify, or improve it.
