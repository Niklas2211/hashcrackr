# 🔐 hashcrackr

**hashcrackr** is a simple and extensible CLI tool for educational use to perform hash cracking via brute-force or wordlist attacks.

> ⚠️ **Disclaimer**: This tool is intended for **educational and ethical use only**. Do not use it on systems or data you do not own or have explicit permission to test. Unauthorized use is illegal and unethical.

### CLI Interface
![CLI Interface](/doc/example-main.JPG)
---
### Example Brute Force Attack
![Example Bruteforce Overview](/doc/example-brute.JPG)
![Example Bruteforce Operation](/doc/example-brute-operation.JPG)


---

## 🚀 Features

- 🔍 Brute-force attack with configurable charset and password length
- 📚 Wordlist attack (dictionary-based)
- 🎨 Pretty console output using `rich`
- 📦 Modern Python packaging (`pyproject.toml`)

---

## 📦 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/hashcrackr.git
cd hashcrackr
```

### 2. Create and Activate a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate      # macOS/Linux
# or
venv\Scripts\activate         # Windows
```

### 3. Install in Editable Mode
```bash
pip install -e .
```


## 🧪 Usage

To see available commands and options:
```bash
hashcrackr --help
hashcrackr brute --help
```

### Example: Brute-Force-Attack
```bash
hashcrackr brute --hash e625c78b51005849249e03fa3963a7f6 --algorithm md5 --min-length 4 --max-length 4 --lowercase --uppercase --digits
```
