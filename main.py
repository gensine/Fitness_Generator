import customtkinter as ctk
import tkinter as tk
import random
from PIL import Image

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Modern Fitness Generator")
app.geometry("420x600")

# Load and display your real image
try:
    img = Image.open("p1.jpg").resize((350, 220))
    workout_img = ctk.CTkImage(light_image=img, size=(350, 220))
    img_label = ctk.CTkLabel(app, image=workout_img, text="")
    img_label.pack(pady=(15, 0))
except Exception as e:
    error_label = ctk.CTkLabel(app, text=f"Image error: {e}", text_color="red")
    error_label.pack(pady=20)

workouts = {
    "Strength": [
        "Push-ups", "Squats", "Lunges", "Plank", "Dumbbell Press",
        "Overhead Squat", "One-legged Pushup"yeh toh p, "Single Leg Bridge",
        "Superman", "Dead Bug", "Glute Bridge"
     ],
    "Cardio": [
        "Jumping Jacks", "Burpees", "Running", "Jump Rope", "High Knees",
        "Jumping Lunges", "Mountain Climbers", "Bear Crawl", "Inchworms",
        "Dancing", "Screamer Lunges"
    ],
    "Flexibility": [
        "Yoga Stretch", "Hamstring Stretch", "Cat-Cow", "Toe Touches",
        "Kneeling Side Plank with Hip Abduction", "Trunk Rotation",
        "Supine Snow Angel"
    ],
    "Core": [
        "Russian Twist", "Plank with Alternating Leg Lift", "Hollow Rock",
        "L-sit", "Swimming Superman", "Barbell Rollout", "Medicine Ball Slam"
    ],
    "Hybrid": [
        "Burpees", "Bear Crawl", "Jumping Lunges", "Inchworms", "Plank",
        "Push-ups", "Mountain Climbers"
    ]
}

exercise_info = {
    "Push-ups": {
        "how_to": "Start in a plank position. Lower your body until your chest nearly touches the floor, then push back up.",
        "times": "3 sets of 12 reps"
    },
    "Squats": {
        "how_to": "Stand with feet shoulder-width apart. Lower down as if sitting, keeping your back straight, then return up.",
        "times": "3 sets of 15 reps"
    },
    "Lunges": {
        "how_to": "Step forward with one leg and lower your hips until both knees are bent at about 90 degrees.",
        "times": "3 sets of 12 reps per leg"
    },
    "Plank": {
        "how_to": "Hold your body in a straight line from head to heels, supported on elbows and toes.",
        "times": "3 sets of 30 seconds"
    },
    "Dumbbell Press": {
        "how_to": "Lie on a bench and press dumbbells upward until arms are extended.",
        "times": "3 sets of 10 reps"
    },
    "Overhead Squat": {
        "how_to": "Hold a barbell overhead and squat down while keeping the barbell stable.",
        "times": "3 sets of 8 reps"
    },
    "One-legged Pushup": {
        "how_to": "Perform a pushup while lifting one leg off the ground.",
        "times": "3 sets of 8 reps per leg"
    },
    "Single Leg Bridge": {
        "how_to": "Lie on your back and lift hips while keeping one leg extended.",
        "times": "3 sets of 12 reps per leg"
    },
    "Superman": {
        "how_to": "Lie face down and lift arms and legs off the ground simultaneously.",
        "times": "3 sets of 15 reps"
    },
    "Dead Bug": {
        "how_to": "Lie on your back and alternate extending opposite arms and legs.",
        "times": "3 sets of 20 reps"
    },
    "Glute Bridge": {
        "how_to": "Lie on your back and lift hips off the ground squeezing glutes.",
        "times": "3 sets of 15 reps"
    },
    "Jumping Jacks": {
        "how_to": "Jump feet out while raising arms overhead, then return to start.",
        "times": "3 sets of 25 reps"
    },
    "Burpees": {
        "how_to": "From standing, drop into a squat, kick feet back, return to squat, and jump up.",
        "times": "3 sets of 10 reps"
    },
    "Running": {
        "how_to": "Run at a steady pace for the duration.",
        "times": "20 minutes"
    },
    "Jump Rope": {
        "how_to": "Jump over a swinging rope continuously.",
        "times": "3 sets of 2 minutes"
    },
    "High Knees": {
        "how_to": "Run in place lifting knees as high as possible.",
        "times": "3 sets of 30 seconds"
    },
    "Jumping Lunges": {
        "how_to": "Jump and switch legs in a lunge position.",
        "times": "3 sets of 12 reps per leg"
    },
    "Mountain Climbers": {
        "how_to": "From plank, alternate bringing knees to chest quickly.",
        "times": "3 sets of 30 seconds"
    },
    "Bear Crawl": {
        "how_to": "Crawl on hands and feet moving forward.",
        "times": "3 sets of 20 meters"
    },
    "Inchworms": {
        "how_to": "From standing, walk hands forward to plank and back.",
        "times": "3 sets of 10 reps"
    },
    "Dancing": {
        "how_to": "Freestyle dance to keep moving.",
        "times": "15 minutes"
    },
    "Screamer Lunges": {
        "how_to": "Perform lunges with a jump and scream.",
        "times": "3 sets of 10 reps per leg"
    },
    "Yoga Stretch": {
        "how_to": "Perform various yoga poses to stretch muscles.",
        "times": "15 minutes"
    },
    "Hamstring Stretch": {
        "how_to": "Sit and reach for your toes to stretch hamstrings.",
        "times": "3 sets of 30 seconds"
    },
    "Cat-Cow": {
        "how_to": "Alternate arching and rounding your back on hands and knees.",
        "times": "3 sets of 10 reps"
    },
    "Toe Touches": {
        "how_to": "Stand and bend forward to touch your toes.",
        "times": "3 sets of 15 reps"
    },
    "Kneeling Side Plank with Hip Abduction": {
        "how_to": "Hold side plank on knees and lift top leg.",
        "times": "3 sets of 15 reps per side"
    },
    "Trunk Rotation": {
        "how_to": "Sit and rotate your torso side to side.",
        "times": "3 sets of 20 reps"
    },
    "Supine Snow Angel": {
        "how_to": "Lie on back and move arms and legs like a snow angel.",
        "times": "3 sets of 15 reps"
    },
    "Russian Twist": {
        "how_to": "Sit and twist torso side to side holding a weight.",
        "times": "3 sets of 20 reps"
    },
    "Plank with Alternating Leg Lift": {
        "how_to": "Hold plank and lift one leg at a time.",
        "times": "3 sets of 15 reps per leg"
    },
    "Hollow Rock": {
        "how_to": "Lie on back and rock back and forth keeping body hollow.",
        "times": "3 sets of 20 reps"
    },
    "L-sit": {
        "how_to": "Sit and lift legs straight out forming an L shape.",
        "times": "3 sets of 15 seconds"
    },
    "Swimming Superman": {
        "how_to": "Lie face down and alternate lifting opposite arms and legs.",
        "times": "3 sets of 20 reps"
    },
    "Barbell Rollout": {
        "how_to": "Use an ab wheel or barbell to roll forward and back.",
        "times": "3 sets of 10 reps"
    },
    "Medicine Ball Slam": {
        "how_to": "Lift a medicine ball overhead and slam it down.",
        "times": "3 sets of 15 reps"
    },
}

title = ctk.CTkLabel(app, text="Fitness Generator", font=("Arial", 24, "bold"))
title.pack(pady=15)

workout_type = ctk.StringVar(value="Strength")
dropdown = ctk.CTkOptionMenu(app, variable=workout_type, values=list(workouts.keys()), width=200)
dropdown.pack(pady=10)

# Use a Tkinter Listbox for clickable exercises
listbox_frame = ctk.CTkFrame(app)
listbox_frame.pack(pady=10)
exercise_listbox = tk.Listbox(listbox_frame, width=40, height=6, font=("Arial", 14))
exercise_listbox.pack()

info_box = ctk.CTkTextbox(app, width=350, height=100, font=("Arial", 12))
info_box.pack(pady=10)
info_box.insert("end", "Select an exercise above to see how to do it and how many times!")
info_box.configure(state="disabled")

current_exercises = []

def generate_workout():
    w_type = workout_type.get()
    num_exercises = min(6, len(workouts[w_type]))
    exercises = random.sample(workouts[w_type], num_exercises)
    global current_exercises
    current_exercises = exercises

    exercise_listbox.delete(0, tk.END)
    for ex in exercises:
        exercise_listbox.insert(tk.END, ex)

    info_box.configure(state="normal")
    info_box.delete("1.0", "end")
    info_box.insert("end", "Select an exercise above to see how to do it and how many times!")
    info_box.configure(state="disabled")

def on_exercise_select(event):
    selection = exercise_listbox.curselection()
    if selection:
        idx = selection[0]   # <-- FIXED: get the first selected index
        ex_name = current_exercises[idx]
        info = exercise_info.get(ex_name, {"how_to": "No info available.", "times": "No info."})
        info_box.configure(state="normal")
        info_box.delete("1.0", "end")
        info_box.insert("end", f"{ex_name}\n\nHow to do it:\n{info['how_to']}\n\nHow many times:\n{info['times']}")
        info_box.configure(state="disabled")

exercise_listbox.bind("<<ListboxSelect>>", on_exercise_select)

generate_btn = ctk.CTkButton(app, text="Generate Workout", command=generate_workout, width=200)
generate_btn.pack(pady=10)

app.mainloop()
