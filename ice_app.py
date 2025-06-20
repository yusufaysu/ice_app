import tkinter
import tkinter.messagebox
import customtkinter
from PIL import Image
import os

image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "assets")

customtkinter.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        # configure window
        self.title("iCe App")

        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        window_width = 1100
        window_height = 580

        #ekranın ortısnı bulmak için
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2

        self.geometry(f"{window_width}x{window_height}+{x}+{y}")

        # full left sidebar
        # set grid layout 1x2
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        self.logo_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "logo.png")))

        self.navigation_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(4, weight=1)

        self.navigation_frame_label = customtkinter.CTkLabel(self.navigation_frame, text="iCe Masterbox Controller", compound="left",
                                                             font=customtkinter.CTkFont(size=15, weight="bold"))
        self.navigation_frame_label.grid(row=0, column=0, padx=20, pady=20)

        self.button1 = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Manuel Giriş/Çıkış",
                                               fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                               command=lambda: self.select_frame_by_name("manuel"))
        self.button1.grid(row=1, column=0, sticky="ew")

        self.button2 = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Otonom Giriş/Çıkış",
                                                fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                command=lambda: self.select_frame_by_name("otonom"))
        self.button2.grid(row=2, column=0, sticky="ew")

        self.button3 = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Kalibrasyon",
                                                fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                command=lambda: self.select_frame_by_name("kalibre"))
        self.button3.grid(row=3, column=0, sticky="ew")

        self.button4 = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Ayarlar",
                                                fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                command=lambda: self.select_frame_by_name("settings"))
        self.button4.grid(row=5, column=0, sticky="ew")

        self.button5 = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Yapılan ayarları Gönder")
        self.button5.grid(row=6, column=0, sticky="ew")

        # manuel frame
        self.frame_manuel = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")

        # otonom frame
        self.frame_otonom = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")

        # kalibre frame
        self.frame_kalibre = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")

        #settings frame
        self.frame_settings = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")

        # select default frame
        self.select_frame_by_name("manuel")

    def select_frame_by_name(self, name):
        # set button color for selected button
        self.button1.configure(fg_color=("gray75", "gray25") if name == "manuel" else "transparent")
        self.button2.configure(fg_color=("gray75", "gray25") if name == "otonom" else "transparent")
        self.button3.configure(fg_color=("gray75", "gray25") if name == "kalibre" else "transparent")
        self.button4.configure(fg_color=("gray75", "gray25") if name == "settings" else "transparent")

        # show selected frame
        if name == "manuel":
            self.frame_manuel.grid(row=0, column=1, sticky="nsew")
            print("manuel")
        else:
            self.frame_manuel.grid_forget()
        if name == "otonom":
            self.frame_otonom.grid(row=0, column=1, sticky="nsew")
            print("otonom")
        else:
            self.frame_otonom.grid_forget()
        if name == "kalibre":
            self.frame_kalibre.grid(row=0, column=1, sticky="nsew")
            print("kalibre")
        else:
            self.frame_kalibre.grid_forget()
        if name == "settings":
            self.frame_settings.grid(row=0, column=1, sticky="nsew")
            print("settings")
        else:
            self.frame_settings.grid_forget()

if __name__ == "__main__":
    app = App()
    app.mainloop()