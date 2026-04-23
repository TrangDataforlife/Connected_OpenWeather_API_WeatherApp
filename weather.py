import tkinter as tk
import requests
import time

#Tạo hàm lấy data thời tiết bằng cách kết nối open API của OpenWeather và dùng HTTP protocol (GET)
def getWeather(canvas):
    city = textfield.get()
    api = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=6dc66893a3eba10ce4d9babafe12701c&units=metric"
    response = requests.get(api)

    # Kiểm tra API
    if response.status_code == 200:
        json_data = response.json()

        # --- Lấy dữ liệu thời tiết qua OpenWeather API với định dạng JSON  ---
        condition = json_data['weather'][0]['main']
        temp = int(json_data['main']['temp'])
        min_temp = int(json_data['main']['temp_min'])
        max_temp = int(json_data['main']['temp_max']) 
        pressure = json_data['main']['pressure']
        humidity = json_data['main']['humidity']
        wind = json_data['wind']['speed']
        sunrise = time.strftime("%I:%M:%S %p", time.gmtime(json_data['sys']['sunrise']+25200))
        sunset = time.strftime("%I:%M:%S %p", time.gmtime(json_data['sys']['sunset']+25200))

        # Thiết kế giao diện màn hình
        label_temp.config(text=f"{temp}°C")
        label_condition.config(text=condition)
        
        final_data = (f"Max Temp: {max_temp}°C  |  Min Temp: {min_temp}°C\n\n"
                      f"Pressure: {pressure} hPa\n"
                      f"Humidity: {humidity}%\n"
                      f"Wind Speed: {wind} m/s\n\n"
                      f"Sunrise: {sunrise}\n"
                      f"Sunset: {sunset}")
        label_details.config(text=final_data)
    else:
        label_condition.config(text="City Not Found!")
        label_temp.config(text="--")
        label_details.config(text="")

# --- Thiết lập giao diện mới ---
canvas = tk.Tk()
canvas.geometry("500x650")
canvas.title("Weather App - Trang Nguyen")
canvas.config(bg="#f2f8ff") # Màu nền xanh nhạt hiện đại

# Font chữ
f_small = ("poppins", 12)
f_medium = ("poppins", 18, "bold")
f_big = ("poppins", 50, "bold")
f_city = ("poppins", 25)

# Ô nhập liệu (Search Bar)
textfield = tk.Entry(canvas, font=f_city, justify='center', bd=0, bg="#ffffff", highlightthickness=2, highlightbackground="#d1e3ff")
textfield.pack(pady=40, padx=50, fill='x')
textfield.focus()
textfield.bind('<Return>', getWeather)

# Hiển thị chính (Nhiệt độ & Trạng thái)
label_condition = tk.Label(canvas, font=f_medium, bg="#f2f8ff", fg="#57606f")
label_condition.pack()

label_temp = tk.Label(canvas, font=f_big, bg="#f2f8ff", fg="#2f3542")
label_temp.pack(pady=10)

# Khung chứa chi tiết
details_frame = tk.Frame(canvas, bg="#ffffff", bd=0, relief="flat", padx=20, pady=20)
details_frame.pack(pady=30, padx=40, fill='both')

label_details = tk.Label(details_frame, font=f_small, bg="#ffffff", fg="#2f3542", justify="left")
label_details.pack()

canvas.mainloop()