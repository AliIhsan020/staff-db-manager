# Staff Database Manager

A lightweight Python utility for managing staff and department data using **SQLite** and **Pandas**. It imports CSV files into a local SQLite database, supports appending new records, and allows running custom SQL queries.

---

## Features

- Load CSV data into SQLite tables automatically
- Append new instructor or department records programmatically
- Run custom SELECT queries and print formatted results
- View full table contents with a single function call

---

## Project Structure

```
staff-db-manager/
├── main.py             # Main script with all DB operations
├── Instructor.csv      # Seed data for the Instructor table
├── Departments.csv     # Seed data for the Departments table
├── Staff.db            # SQLite database (auto-generated)
└── README.md
```

---

## Database Schema

### `Instructor`
| Column | Type   | Description         |
|--------|--------|---------------------|
| ID     | INT    | Unique instructor ID |
| FNAME  | TEXT   | First name          |
| LNAME  | TEXT   | Last name           |
| CITY   | TEXT   | City of residence   |
| CCODE  | TEXT   | Country code        |

### `Departments`
| Column      | Type   | Description          |
|-------------|--------|----------------------|
| DEPT_ID     | INT    | Department ID        |
| DEP_NAME    | TEXT   | Department name      |
| MANAGER_ID  | INT    | Manager's ID         |
| LOC_ID      | TEXT   | Location identifier  |

---

## Getting Started

### Prerequisites

- Python 3.7+
- `pandas` library

```bash
pip install pandas
```

### Usage

```bash
python main.py
```

This will:
1. Import `Instructor.csv` and `Departments.csv` into `Staff.db`
2. Append a sample instructor and department record
3. Run a sample COUNT query on the Departments table

### Example: Append a New Instructor

```python
append_to_instructor(table_instructor, 99, 'Jane', 'Smith', 'London', 'UK')
```

### Example: Run a Custom Query

```python
custom_query("SELECT FNAME, LNAME", table_instructor)
```

---

## Requirements

```
pandas
```

---

## License

This project is open source and available under the [MIT License](LICENSE).

---

## 🇹🇷 Kısa Türkçe Özet

Bu proje, CSV dosyalarından SQLite veritabanına personel ve departman verisi aktarmak için geliştirilmiş küçük bir Python yardımcı programıdır. `pandas` kütüphanesi kullanılarak CSV'ler otomatik olarak tablolara yüklenir; yeni kayıt ekleme ve özel SQL sorgusu çalıştırma işlemleri de desteklenmektedir.
