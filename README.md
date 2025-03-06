# pyiwy (It Worked Yesterday)

### Replace boring error messages with **hilarious** responses! Because debugging shouldn't be painful.  

[![License](https://img.shields.io/badge/license-GPLv3-blue)](LICENSE)  

---

## 🎭 **What is this?**
Ever been frustrated by boring error messages?  
This package **catches exceptions** and replaces them with **funny responses** while keeping the original error message intact.  

💡 **Example:**  
```python
import pyiwy  # Just import it, and it's active!

print(10 / 0)  # ZeroDivisionError
```
💥 Output:
```sh
🔥 ERROR ALERT 🔥
Nice try! Even Python can't divide by zero. 🤦

Original Error: division by zero
```
## 🚀 Installation
Install it directly from PyPI:
```sh
pip install pyiwy
```
## 📖 Usage

Simply import the package in your script, and it will automatically replace error messages:
```python
import pyiwy  # This enables the fun!

# Trigger some errors for fun
print(1 / 0)  # ZeroDivisionError
print({}["missing_key"])  # KeyError
print("text" + 5)  # TypeError

```
## 🤯 Some Funny Error Messages

|Exception|Funny Message|
|---------|-------------|
|ZeroDivisionError|"Nice try! Even Python can't divide by zero. 🤦"|
|TypeError|"You just mixed up data types. Python is not a smoothie blender! 🥤"|
|KeyError|"That key doesn't exist! Maybe it got lost in the matrix. 🔑💻"|
|FileNotFoundError|"File not found! Maybe it's playing hide and seek? 🕵️‍♂️"|
|RecursionError|"Recursion limit reached! Recursion limit reached! Recursion limit reached! 🔄"|
|AttributeError|"That attribute doesn't exist! Maybe it left the codebase to follow its dreams. 🚀"|
|TimeoutError|"Operation took too long. Python is impatient, unlike your crush. ⏳"|

## 🧪 Running Tests
To run unit tests, use:
```sh
python -m unittest discover tests
```
or
```sh
python -m unittest tests/test_exceptions.py
```

## 🛠 Customization
Want to add your own funny messages? Modify the exceptions_data.py file inside the package.

Example:
```python
EXCEPTION_MESSAGES[ValueError] = "Oops! Your value isn't valid. But don't worry, neither is my life decision to be a Python script. 😅"
```
## 🤝 Contributing
Want to make this funnier? Fork the repo, add some jokes, and submit a pull request!

## 📜 License
This project is licensed under the GNU GPLv3 License. See the [LICENSE](./LICENSE) file for details.

## 💬 Connect with Me
Made by [Shreehar K E](https://www.linkedin.com/in/shreehar-ke/). Connect with me on LinkedIn 🚀

