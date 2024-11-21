while True:
    # รับข้อความจากผู้ใช้
    user_input = input("What you gotta say? : ")
    
    # ตรวจสอบว่าผู้ใช้ป้อนคำว่า STOP หรือไม่
    if user_input == "STOP":
        break  # หยุดลูป
    else:
        # แสดงข้อความตอบกลับ
        print("I got that! Anything else?")
