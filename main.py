import csv

def csv_yozuvchi(fayl_ismi, ma'lumotlar):
    try:
        with open(fayl_ismi, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(ma'lumotlar)
        print("Ma'lumotlar yozildi.")
    except Exception as e:
        print(f"Xatolik yuz berdi: {e}")

# Misol foydalanish:
ma'lumotlar = [
    ["Ism", "Yosh"],
    ["Ali", 20],
    ["Vali", 25],
    ["Hasan", 30]
]
csv_yozuvchi("ma'lumotlar.csv", ma'lumotlar)
```

```python
import csv

def csv_yozuvchi(fayl_ismi, ma'lumotlar):
    try:
        with open(fayl_ismi, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(ma'lumotlar)
        print("Ma'lumotlar yozildi.")
    except Exception as e:
        print(f"Xatolik yuz berdi: {e}")

# Misol foydalanish:
ma'lumotlar = [
    ["Ism", "Yosh"],
    ["Ali", 20],
    ["Vali", 25],
    ["Hasan", 30]
]
csv_yozuvchi("ma'lumotlar.csv", ma'lumotlar)
