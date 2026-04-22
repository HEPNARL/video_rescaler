import tkinter as tk
from tkinter import ttk, filedialog, messagebox

import rescale_video
import ratio_fit


# ---------------- Utilities ----------------

def parse_ratio(value: str) -> float:
    w, h = value.split(":")
    return int(w) / int(h)


def browse_dir(var):
    path = filedialog.askdirectory()
    if path:
        var.set(path)


def set_ratio(value):
    ratio_var.set(value)


def run_pipeline():
    try:
        size = (int(width_var.get()), int(height_var.get()))
        ratio = parse_ratio(ratio_var.get())

        rescale_video.rescale_videos(
            input_var.get(),
            output_var.get(),
            size=size,
            target_ratio=ratio
        )

        ratio_fit.ratio_fit_images(
            input_var.get(),
            output_var.get(),
            size=size,
            prior_ratio=ratio
        )

        messagebox.showinfo("Done", "Processing completed successfully.")

    except Exception as e:
        messagebox.showerror("Error", str(e))


# ---------------- GUI ----------------

root = tk.Tk()
root.title("Image & Video Rescale Tool")
root.geometry("520x420")
root.resizable(False, False)

style = ttk.Style()
style.theme_use("default")
style.configure("TLabel", font=("Segoe UI", 10))
style.configure("TButton", font=("Segoe UI", 10))
style.configure("Header.TLabel", font=("Segoe UI", 12, "bold"))

main = ttk.Frame(root, padding=20)
main.pack(fill="both", expand=True)

# ---------------- Variables ----------------

input_var = tk.StringVar(value="in")
output_var = tk.StringVar(value="out")
width_var = tk.StringVar(value="1920")
height_var = tk.StringVar(value="1080")
ratio_var = tk.StringVar(value="16:9")

# ---------------- Paths Section ----------------

ttk.Label(main, text="Paths", style="Header.TLabel").pack(anchor="w", pady=(0, 8))

paths = ttk.Frame(main)
paths.pack(fill="x", pady=(0, 20))

def path_row(parent, label, var):
    row = ttk.Frame(parent)
    row.pack(fill="x", pady=4)
    ttk.Label(row, text=label, width=12).pack(side="left")
    ttk.Entry(row, textvariable=var).pack(side="left", fill="x", expand=True, padx=6)
    ttk.Button(row, text="Browse", command=lambda: browse_dir(var)).pack(side="left")

path_row(paths, "Input", input_var)
path_row(paths, "Output", output_var)

# ---------------- Settings Section ----------------

ttk.Label(main, text="Output settings", style="Header.TLabel").pack(anchor="w", pady=(0, 8))

settings = ttk.Frame(main)
settings.pack(fill="x")

size_row = ttk.Frame(settings)
size_row.pack(fill="x", pady=4)

ttk.Label(size_row, text="Width").pack(side="left")
ttk.Entry(size_row, textvariable=width_var, width=8).pack(side="left", padx=(5, 15))
ttk.Label(size_row, text="Height").pack(side="left")
ttk.Entry(size_row, textvariable=height_var, width=8).pack(side="left", padx=5)

ratio_row = ttk.Frame(settings)
ratio_row.pack(fill="x", pady=4)

ttk.Label(ratio_row, text="Aspect ratio").pack(side="left")
ttk.Entry(ratio_row, textvariable=ratio_var, width=8).pack(side="left", padx=5)

# Preset buttons
presets = ttk.Frame(settings)
presets.pack(fill="x", pady=(6, 16))

for text in ("16:9", "1:1", "9:16", "3:2"):
    ttk.Button(presets, text=text, command=lambda t=text: set_ratio(t)).pack(
        side="left", padx=4
    )

# ---------------- Run Button ----------------

run_button = ttk.Button(
    main,
    text="Run processing",
    command=run_pipeline
)
run_button.pack(pady=10, ipadx=10, ipady=6)

root.mainloop()