import cv2

def capture_photo():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Could not open camera.")
        return
    ret, frame = cap.read()
    if not ret:
        print("Error: Could not read frame.")
        cap.release()
        return
    cv2.imwrite("captured_photo.jpg", frame)

    print('''
  /$$$$$$  /$$   /$$ /$$$$$$$$  /$$$$$$  /$$       /$$$$$$  /$$$$$$  /$$   /$$
 /$$__  $$| $$$ | $$| $$_____/ /$$__  $$| $$      |_  $$_/ /$$__  $$| $$  /$$/
| $$  \ $$| $$$$| $$| $$      | $$  \__/| $$        | $$  | $$  \__/| $$ /$$/ 
| $$  | $$| $$ $$ $$| $$$$$   | $$      | $$        | $$  | $$      | $$$$$/  
| $$  | $$| $$  $$$$| $$__/   | $$      | $$        | $$  | $$      | $$  $$  
| $$  | $$| $$\  $$$| $$      | $$    $$| $$        | $$  | $$    $$| $$\  $$ 
|  $$$$$$/| $$ \  $$| $$$$$$$$|  $$$$$$/| $$$$$$$$ /$$$$$$|  $$$$$$/| $$ \  $$
 \______/ |__/  \__/|________/ \______/ |________/|______/ \______/ |__/  \__/


                 ////////////////SUCESSFULLY CAPTURE////////////////// 
                                 CREATED BY-CYBER_BOY

                                                                              
                                                                              
''')
    cap.release()

if __name__ == "__main__":
    capture_photo()
