import cv2
import tkinter as tk
import threading
import winsound

FRAME_LIMIT = 15     
NO_FACE_LIMIT = 100   

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

class NapKnightApp:
    def __init__(self, root):
        self.root = root
        self.root.title("NapKnight Panel")
        self.root.geometry("500x350")
        self.root.configure(bg="#222")

        tk.Label(root, text="NapKnight AI", font=("Arial", 28, "bold"), bg="#222", fg="white").pack(pady=20)
        
        instr = "CONTROLS:\n'D' = DRIVE MODE\n'P' = PARK MODE\n'Q' = QUIT"
        tk.Label(root, text=instr, font=("Consolas", 12), bg="#333", fg="#ccc", padx=10, pady=10).pack(pady=10)

        self.btn_start = tk.Button(root, text="LAUNCH SYSTEM", font=("Arial", 14, "bold"), 
                                   bg="#28573b", fg="white", command=self.start_system, height=2, width=20)
        self.btn_start.pack(pady=20)

        self.running = False
        self.driving_mode = False 
        self.is_beeping = False

    def beep(self):
        if self.is_beeping:
            return
            
        def play_sound():
            self.is_beeping = True
            try:
                winsound.Beep(2500, 500) 
            except:
                pass
            self.is_beeping = False

        threading.Thread(target=play_sound).start()

    def start_system(self):
        if self.running: return
        self.running = True
        self.btn_start.config(state=tk.DISABLED, text="RUNNING...")
        # We use a thread so the camera doesn't freeze the menu buttons!
        threading.Thread(target=self.run_loop).start()

    def run_loop(self):
        cap = cv2.VideoCapture(0)
        eye_counter = 0
        face_counter = 0

        while self.running:
            ret, frame = cap.read()
            if not ret: break

            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            key = cv2.waitKey(5) & 0xFF
            
            if key == ord('q') or key == ord('Q'):
                self.running = False
                break
            elif key == ord('d') or key == ord('D'):
                self.driving_mode = True
            elif key == ord('p') or key == ord('P'):
                self.driving_mode = False
                eye_counter = 0    
                face_counter = 0

            cv2.rectangle(frame, (0,0), (frame.shape[1], 80), (0,0,0), -1)

            if not self.driving_mode:
                cv2.putText(frame, "MODE: PARKED", (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)
                eye_counter = 0
                face_counter = 0
            else:
                cv2.putText(frame, "MODE: DRIVING", (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

                faces = face_cascade.detectMultiScale(gray, 1.3, 5)

                if len(faces) == 0:
                    face_counter += 1
                    cv2.putText(frame, "CRITICAL: HEAD DROP / NO DRIVER", (20, 200), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)
                    if face_counter > NO_FACE_LIMIT:
                        self.beep()
                else:
                    face_counter = 0
                    (x, y, w, h) = faces[0]
                    cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

                    roi_gray = gray[y:y+h, x:x+w]
                    eyes = eye_cascade.detectMultiScale(roi_gray, 1.1, 10)

                    if len(eyes) == 0:
                        eye_counter += 1
                        cv2.putText(frame, "ALERT: EYES CLOSED / DISTRACTED", (20, 300), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 165, 255), 2)
                    else:
                        eye_counter = 0
                        cv2.putText(frame, "STATUS: AWAKE", (20, 120), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
                        for (ex, ey, ew, eh) in eyes:
                            cv2.rectangle(frame, (x+ex, y+ey), (x+ex+ew, y+ey+eh), (0, 255, 0), 2)

                    if eye_counter > FRAME_LIMIT:
                        self.beep()

            cv2.imshow('NapKnight Dashboard', frame)

        cap.release()
        cv2.destroyAllWindows()
        self.btn_start.config(state=tk.NORMAL, text="LAUNCH SYSTEM")

if __name__ == "__main__":
    root = tk.Tk()
    app = NapKnightApp(root)
    root.mainloop()