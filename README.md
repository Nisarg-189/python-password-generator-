# 🔐 Advanced Python Password Generator

A clean and modular password generator built using Python, organized into multiple files for better structure and scalability.  
It allows users to customize password length and choose whether to include lowercase letters, uppercase letters, digits, and symbols.

---

## 📁 Project Structure

password_generator/
│── main.py
│── generator/
│ ├── init.py
│ ├── config.py
│ ├── generator.py
│ ├── validator.py


---

## 🚀 Features

- Choose password length  
- Include/exclude:
  - Lowercase letters  
  - Uppercase letters  
  - Numbers  
  - Symbols  
- Input validation  
- Clean multi-file architecture  
- Easy to extend (strength meter, save to file, GUI, etc.)

---

## 🧠 How It Works

- `config.py` → Stores character sets  
- `validator.py` → Validates length & options  
- `generator.py` → Builds the actual password  
- `main.py` → User input + program execution  

---

## ▶️ Usage

Run the program using:

```bash
python3 main.py
