<<<<<<< HEAD
# Student Management System 🧑‍🎓

This is a simple Python-based **Student Management System** designed for basic operations such as storing, retrieving, modifying, and deleting student information. Data is saved to and loaded from a text file (`students.txt`).

## Features

✅ Add new student 
✅ Modify student record 
✅ Delete student 
✅ Find student by student number 
✅ Show all students 
✅ Show students by year of birth 
✅ Save to file / Load from file 
✅ Calculates student age automatically

## Technologies

- **Language**: Python 3
- **File I/O**: Reads/Writes `.txt` files
- **Data Format**: CSV (Comma Separated Values)

## How It Works

- A student is represented as an object with the following attributes:
  - Student Number
  - First Name
  - Last Name
  - Date of Birth
  - Sex
  - Country of Birth
- Student records are stored in a fixed-size list (up to 100 students).
- Data persistence is done through `students.txt`.

## How to Run

1. Clone this repository:

   ```bash
   git clone https://github.com/mrtsekr/StudentManagementSystem
   cd student-management-system
2. Run the Python script:

	```bash
	python student_management.py
3. Follow the menu options to manage student records.

File Structure
	```bash
	student-management-system/
	│
	├── student_management.py   # Main program
	├── students.txt            # Data file (auto-created)
	└── README.md               # This file
Sample Menu

Menu:
1. Write students to file
2. Read students from file
3. Add new student
4. Find student by number
5. Show all students
6. Show students by birth year
7. Modify student record
8. Delete student
9. Quit
License
This project is licensed for educational and personal use.

Author / Yazar
Created by [Mert Şeker]
[Optional: https://github.com/mrtsekr]

🇹🇷 Türkçe Açıklama
Bu proje, Python diliyle yazılmış basit bir Öğrenci Yönetim Sistemidir. Öğrenci bilgilerini dosyaya kaydetme, listeleme, arama, güncelleme ve silme gibi temel işlemleri yapabilirsiniz. Veriler students.txt dosyasında saklanır.

Özellikler
Yeni öğrenci ekleme
Öğrenci bilgisi güncelleme
Öğrenci silme
Öğrenci numarasına göre arama
Tüm öğrencileri listeleme
Belirli doğum yılına göre listeleme
Dosyaya yazma / Dosyadan okuma
Otomatik yaş hesaplama

Çalıştırmak için
1. Depoyu klonlayın:

	```bash

	git clone https://github.com/mrtsekr/StudentManagementSystem
	cd student-management-system

2. Python dosyasını çalıştırın:

```bash

python student_management.py

3. Menüden işlemlerinizi seçin.

