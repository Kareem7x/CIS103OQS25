import tkinter as tk

def main():
    window = tk.Tk()
    window.title("My Smiley Face")

    canvas_width = 400
    canvas_height = 400
    canvas = tk.Canvas(window, width=canvas_width, height=canvas_height, bg="white")
    canvas.pack()

    center_x = canvas_width // 2
    center_y = canvas_height // 2

    face_radius = 150
    canvas.create_oval(center_x - face_radius, center_y - face_radius,
                       center_x + face_radius, center_y + face_radius,
                       outline="green", width=3)  

    eye_radius = 30
    eye_offset_x = 60
    eye_y = center_y - 50  

   
    canvas.create_oval(center_x - eye_offset_x - eye_radius, eye_y - eye_radius,
                       center_x - eye_offset_x + eye_radius, eye_y + eye_radius,
                       fill="red")  

  
    canvas.create_oval(center_x + eye_offset_x - eye_radius, eye_y - eye_radius,
                       center_x + eye_offset_x + eye_radius, eye_y + eye_radius,
                       fill="blue")  


    mouth_width = 100
    mouth_height = 20
    mouth_y = center_y + 50  
    canvas.create_rectangle(center_x - mouth_width // 2, mouth_y - mouth_height // 2,
                            center_x + mouth_width // 2, mouth_y + mouth_height // 2,
                            fill="yellow")  


    nose_width = 40
    nose_height = 30
    nose_y = center_y + 120 
    nose_points = [center_x - nose_width // 2, nose_y - nose_height // 2,
                   center_x + nose_width // 2, nose_y - nose_height // 2,
                   center_x, nose_y + nose_height // 2]
    canvas.create_polygon(nose_points, fill="black") 


    window.mainloop()

if __name__ == "__main__":
    main()