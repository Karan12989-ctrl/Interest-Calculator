# 📊 Interest Calculator (Simple & Compound Interest)

This project is a simple Python-based **Interest Calculator** that allows users to calculate:

- ✔ Simple Interest  
- ✔ Compound Interest  
- ✔ Total Amount after interest  

The user selects the type of interest, enters the principal amount, rate, and time, and the calculator returns the results.

---

## 🚀 Features

- Easy-to-use console interface  
- Calculates **Simple Interest**  
- Calculates **Compound Interest**  
- Formats results up to 2 decimal places  
- Beginner-friendly code  

---

## 🧮 Formula Used

### ✔ Simple Interest  
\[
SI = \frac{P \times R \times T}{100}
\]

### ✔ Compound Interest  
\[
A = P\left(1 + \frac{R}{100}\right)^T
\]

\[
CI = A - P
\]

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

---

## 📌 Example Output
---- Interest Calculator ----
1. Simple Interest
2. Compound Interest
Enter your choice (1 or 2): 2
Enter Principal Amount: 1000
Enter Rate of Interest (%): 10
Enter Time (in years): 2
Compound Interest = 210.00
Total Amount = 1210.00

---

##🧑‍💻 Author

Karan (You can edit this section)
---

##📄 License

This project is open-source. Feel free to modify and use it anywhere.