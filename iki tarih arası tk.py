import tkinter as tk
from tkinter import messagebox
from datetime import datetime
import pandas as pd

# Fonksiyonumuzu GUI ile uyumlu hale getiriyoruz (input yerine Entry kullanılıyor)
def calculate_date_difference(start_date_input, end_date_input):
    # String'leri datetime objelerine dönüştür
    start_date = datetime.strptime(start_date_input, '%Y-%m-%d')
    end_date = datetime.strptime(end_date_input, '%Y-%m-%d')

    # DataFrame oluştur
    df = pd.DataFrame({
        "Date": [start_date, end_date]
    })

    # Yıl, ay ve gün sütunları ekle
    df['Year'] = df['Date'].dt.year
    df['Month'] = df['Date'].dt.month
    df['Day'] = df['Date'].dt.day

    # Yıl, ay ve gün farkını hesapla
    years_diff = df.iloc[-1]['Year'] - df.iloc[0]['Year']
    months_diff = df.iloc[-1]['Month'] - df.iloc[0]['Month']
    days_diff = df.iloc[-1]['Day'] - df.iloc[0]['Day']

    # Negatif farklar için ayarlama yap
    if days_diff < 0:
        months_diff -= 1
        days_diff += 30  # Her ayın 30 gün olduğunu varsay
    if months_diff < 0:
        years_diff -= 1
        months_diff += 12

    # Yılları gün cinsine çevir
    total_days = years_diff * 360 + months_diff * 30 + days_diff

    # Gün, ay ve yıl hesaplamalarını yap
    day = total_days % 360 % 30
    month = (total_days % 360) // 30 if (total_days % 360) > 30 else 0
    year = total_days // 360

    # Sonuçları GUI'de göstermek için bir string oluşturuyoruz
    result_str = f"Total Days Difference: {total_days}\nYears: {year}, Months: {month}, Days: {day}"
    return result_str

# GUI'de 'Calculate' butonuna basıldığında bu fonksiyon çalışacak
def on_calculate_clicked():
    # Entry'den tarihleri al
    start_date = start_date_entry.get()
    end_date = end_date_entry.get()

    # Tarihlerin doğru girildiğinden emin ol
    try:
        # Hesaplamayı yap ve sonucu result_label'a yaz
        result = calculate_date_difference(start_date, end_date)
        result_label.config(text=result)
    except ValueError:
        messagebox.showerror("Error", "Please enter the dates in YYYY-MM-DD format.")

# Tkinter penceresini oluştur
root = tk.Tk()
root.title("Date Difference Calculator")

# Başlangıç tarihi etiketi ve metin kutusu
start_date_label = tk.Label(root, text="Başlangıç Tarihi Girin (YYYY-MM-DD):")
start_date_label.pack()
start_date_entry = tk.Entry(root)
start_date_entry.pack()

# Bitiş tarihi etiketi ve metin kutusu
end_date_label = tk.Label(root, text="Bitiş Tarihi Girin (YYYY-MM-DD):")
end_date_label.pack()
end_date_entry = tk.Entry(root)
end_date_entry.pack()

# Hesapla butonu
calculate_button = tk.Button(root, text="Hesapla", command=on_calculate_clicked)
calculate_button.pack()

# Sonuç etiketi
result_label = tk.Label(root, text="")
result_label.pack()

# GUI başlat
root.mainloop()
