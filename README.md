# Aditivi v Hrani – Food Additives Lookup

This is a simple web application for searching food additives (E-numbers) and their Slovenian names and classes.

## Features
- Search by E-number or name (Slovenian)
- See the class/category of each additive
- Modern, responsive web interface

## How to Run

1. **Install dependencies**

```
pip install -r requirements.txt
```

2. **Start the application**

```
python app.py
```

3. **Open your browser**

Go to [http://localhost:5000](http://localhost:5000)

## Data

All data is in `data/additives.csv`.

## Project Structure

- `app.py` – Flask backend
- `templates/index.html` – Frontend
- `data/additives.csv` – Additives data
- `requirements.txt` – Dependencies

---

*Created for easy lookup of food additives in Slovenian.* 