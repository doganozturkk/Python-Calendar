<h1 align="center">
  <span style="
    background: linear-gradient(to right, #276dc3, #5dc863);
    -webkit-background-clip: text;
    color: transparent;
    font-size: 40px;
    font-weight: 900;
  ">
    Python Calendar Project
  </span>
</h1>

<p align="center" style="
  font-size: 18px;
  color: #555;
  margin-top: -10px;
">
  <i>A fully self-contained calendar built with Python</i>
</p>

<p align="center">
  <img src="https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExYnRtem15ZWZtNXRjMXUzamd2OHluZjdtaHRwdW9hMnpndTRlc2t5aSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/12oTlUqDjqhTUs/giphy.gif" width="320" />
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.14.2-blue?logo=python&style=for-the-badge">
  <img src="https://img.shields.io/badge/IDE-PyCharm-000000?logo=PyCharm&style=for-the-badge">
  <img src="https://img.shields.io/badge/Status-Active-brightgreen?style=for-the-badge">
</p>

---

## 📌 Overview

A fully self-contained Python calendar utility implemented from scratch, without using the built-in calendar or datetime modules.  
This project computes the day names for any past or future date and prints a clean ASCII monthly calendar aligned to ISO 8601 (weeks start on Monday).  

---

## 📁 Project Structure

```
manual-date-weekday/
│
├── simple_calendar.py
└── README.md
```

---

## 🛠️ Technologies

- **Python 3.14.2**
- **PyCharm IDE**

---

## 🔧 How It Works

This project computes the day of the week for any given date **without using Python’s `calendar` module**, relying entirely on manual date arithmetic and a fixed reference date.

### Algorithm Overview

- **Month Lengths**
  - Stores fixed day counts for each month.
  - Adjusts February to 29 days in leap years.

- **Leap Year Detection**
  - A year is leap if:
    - divisible by **4** and not by **100**, or  
    - divisible by **400**.

- **Weekday Names**
  - Uses European order (starting Monday):  
    `["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]`

- **Anchor Date**
  - Reference point: **January 1, 2000 (Saturday)**.

- **Total Day Offset Calculation**
  - If target year **> 2000** → add days year by year.
  - If target year **< 2000** → subtract days year by year.
  - Within the target year:
    - Add all days of previous months.
    - Add `(day - 1)` for the current month.

- **Final Weekday Determination**
  - Apply the total offset to the anchor weekday index.
  - Rotate through the weekday list to obtain the final result.

---

## ✨ Features

✔ ISO 8601 weekday format (Monday = 0)  
✔ Manual leap-year logic  
✔ Correct handling of Gregorian calendar rules  
✔ Tomohiko Sakamoto’s algorithm implementation  
✔ Monthly ASCII calendar output  
✔ No external libraries used  
✔ Fully compatible with PyCharm or any Python IDE  

---

## 📊 Example Usage

Input:  
13/03/2057

Output:  
13/03/2057 -> Wednesday

Monthly Calendar Output:  

```
      March 2057       
Mo Tu We Th Fr Sa Su
             1  2  3
 4  5  6  7  8  9 10
11 12 13 14 15 16 17
18 19 20 21 22 23 24
25 26 27 28 29 30 31
```

---

## 🚀 How to Run

python simple_calendar.py  

You will be prompted to enter a date in the format:  

DD/MM/YYYY

---

## 📅 Leap Year Logic

The project follows the proleptic Gregorian leap year rules:  
✔ If divisible by 4 → leap year  
✔ Except divisible by 100 → not a leap year  
✔ Except divisible by 400 → leap year again  

Example:  
* 2000 = leap year  
* 1900 = not a leap year  
* 2024 = leap year  

---

## 🎯 Why This Project Exists

This utility provides a clear demonstration of how calendars actually work under the hood, without relying on any built-in modules.  
It is ideal for students, beginners, and anyone who wants to understand calendar computation algorithms.

---

## 📈 Future Improvements (Optional Ideas)

These are intentionally not included yet, but can be added later:  
✔ Event tracking  
✔ Alarm/reminder system  
✔ Birthday manager  
✔ Multi-language support  
✔ Unit tests  
✔ GUI version (Tkinter or PyQt)  

---

## ⭐ Ideal for learning:  

✔ Date algorithms  
✔ Leap-year rules  
✔ Month/day computations  

---

## 📄 License

This project is licensed under the MIT License — feel free to fork it, extend it, and experiment with new Python ideas!

---

## 🙌 Author

Developed by: @doganozturkk
