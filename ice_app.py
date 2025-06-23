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
        window_height = 700

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
        self.frame_manuel.grid_columnconfigure(0, weight=1)
        self.label_manuel = customtkinter.CTkLabel(self.frame_manuel, text="Manuel Giriş/Çıkış", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.label_manuel.grid(row=0, column=0, pady=20, sticky="new")

        # otonom frame
        self.frame_otonom = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.frame_otonom.grid_columnconfigure(0, weight=1)
        self.label_otonom = customtkinter.CTkLabel(self.frame_otonom, text="Otonom Giriş/Çıkış", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.label_otonom.grid(row=0, column=0, pady=20, sticky="new")

        # kalibre frame
        self.frame_kalibre = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.frame_kalibre.grid_columnconfigure(0, weight=1)
        self.label_kalibre = customtkinter.CTkLabel(self.frame_kalibre, text="Kalibrasyon", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.label_kalibre.grid(row=0, column=0, pady=20, sticky="new")

        # settings frame
        self.frame_settings = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.frame_settings.grid_columnconfigure(0, weight=1)
        self.frame_settings.grid_columnconfigure(1, weight=1)

        # Sol frame (ayarlar ve proje)
        self.settings_left_frame = customtkinter.CTkFrame(self.frame_settings, fg_color="transparent")
        self.settings_left_frame.grid(row=0, column=0, sticky="nsew", padx=(40, 20), pady=30)
        self.settings_left_frame.grid_columnconfigure(0, weight=1)

        self.label_settings = customtkinter.CTkLabel(self.settings_left_frame, text="Ayarlar", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.label_settings.grid(row=0, column=0, pady=20, sticky="w")

        # Ayarlar label ve textboxlar (yan yana)
        self.label_device_name = customtkinter.CTkLabel(self.settings_left_frame, text="Cihaz Adı:")
        self.label_device_name.grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.entry_device_name = customtkinter.CTkEntry(self.settings_left_frame)
        self.entry_device_name.grid(row=1, column=1, padx=5, pady=5, sticky="ew")
        self.entry_device_name.insert(0, "Varsayılan Cihaz Adı")

        self.label_device_id = customtkinter.CTkLabel(self.settings_left_frame, text="Cihaz ID:")
        self.label_device_id.grid(row=2, column=0, padx=5, pady=5, sticky="w")
        self.entry_device_id = customtkinter.CTkEntry(self.settings_left_frame)
        self.entry_device_id.grid(row=2, column=1, padx=5, pady=5, sticky="ew")
        self.entry_device_id.insert(0, "ID")

        self.label_license = customtkinter.CTkLabel(self.settings_left_frame, text="Lisans:")
        self.label_license.grid(row=3, column=0, padx=5, pady=5, sticky="w")
        self.entry_license = customtkinter.CTkEntry(self.settings_left_frame)
        self.entry_license.grid(row=3, column=1, padx=5, pady=5, sticky="ew")
        self.entry_license.insert(0, "Lisans")

        self.label_mqtt_server = customtkinter.CTkLabel(self.settings_left_frame, text="MQTT Server:")
        self.label_mqtt_server.grid(row=4, column=0, padx=5, pady=5, sticky="w")
        self.entry_mqtt_server = customtkinter.CTkEntry(self.settings_left_frame)
        self.entry_mqtt_server.grid(row=4, column=1, padx=5, pady=5, sticky="ew")
        self.entry_mqtt_server.insert(0, "Lisans")


        self.label_mqtt_keepalive = customtkinter.CTkLabel(self.settings_left_frame, text="MQTT Keepalive:")
        self.label_mqtt_keepalive.grid(row=5, column=0, padx=5, pady=5, sticky="w")
        self.entry_mqtt_keepalive = customtkinter.CTkEntry(self.settings_left_frame)
        self.entry_mqtt_keepalive.grid(row=5, column=1, padx=5, pady=5, sticky="ew")

        self.settings_left_frame.grid_columnconfigure(1, weight=1)

        # Checkboxlar aynı kalacak, satır numaralarını güncelle
        self.checkbox_web = customtkinter.CTkCheckBox(self.settings_left_frame, text="Web Sayfası")
        self.checkbox_web.grid(row=6, column=0, padx=5, pady=5, sticky="w", columnspan=2)
        self.checkbox_web.select()
        self.checkbox_tcp = customtkinter.CTkCheckBox(self.settings_left_frame, text="TCP Server")
        self.checkbox_tcp.grid(row=7, column=0, padx=5, pady=5, sticky="w", columnspan=2)
        self.checkbox_tcp.select()
        self.checkbox_reset = customtkinter.CTkCheckBox(self.settings_left_frame, text="Reset Servisi")
        self.checkbox_reset.grid(row=8, column=0, padx=5, pady=5, sticky="w", columnspan=2)
        self.checkbox_random_mac = customtkinter.CTkCheckBox(self.settings_left_frame, text="Random MAC")
        self.checkbox_random_mac.grid(row=9, column=0, padx=5, pady=5, sticky="w", columnspan=2)
        self.checkbox_time_sync = customtkinter.CTkCheckBox(self.settings_left_frame, text="Time Sync")
        self.checkbox_time_sync.grid(row=10, column=0, padx=5, pady=5, sticky="w", columnspan=2)

        self.label_project = customtkinter.CTkLabel(self.settings_left_frame, text="Proje", font=customtkinter.CTkFont(size=18, weight="bold"))
        self.label_project.grid(row=11, column=0, pady=(20, 10), sticky="w", columnspan=2)

        self.label_blok_no = customtkinter.CTkLabel(self.settings_left_frame, text="Blok No:")
        self.label_blok_no.grid(row=12, column=0, padx=5, pady=5, sticky="w")
        self.entry_blok_no = customtkinter.CTkEntry(self.settings_left_frame)
        self.entry_blok_no.grid(row=12, column=1, padx=5, pady=5, sticky="ew")

        self.label_daire_no = customtkinter.CTkLabel(self.settings_left_frame, text="Daire No:")
        self.label_daire_no.grid(row=13, column=0, padx=5, pady=5, sticky="w")
        self.entry_daire_no = customtkinter.CTkEntry(self.settings_left_frame)
        self.entry_daire_no.grid(row=13, column=1, padx=5, pady=5, sticky="ew")

        self.label_location = customtkinter.CTkLabel(self.settings_left_frame, text="Location:")
        self.label_location.grid(row=14, column=0, padx=5, pady=5, sticky="w")
        self.entry_location = customtkinter.CTkEntry(self.settings_left_frame)
        self.entry_location.grid(row=14, column=1, padx=5, pady=5, sticky="ew")

        self.label_project_no = customtkinter.CTkLabel(self.settings_left_frame, text="Proje No:")
        self.label_project_no.grid(row=15, column=0, padx=5, pady=5, sticky="w")
        self.entry_project_no = customtkinter.CTkEntry(self.settings_left_frame)
        self.entry_project_no.grid(row=15, column=1, padx=5, pady=5, sticky="ew")

        # Sağ frame (WAN başlığı ve içerik)
        self.settings_right_frame = customtkinter.CTkFrame(self.frame_settings, fg_color="transparent")
        self.settings_right_frame.grid(row=0, column=1, sticky="nsew", padx=(20, 40), pady=30)
        self.settings_right_frame.grid_columnconfigure(0, weight=1)

        self.label_wan = customtkinter.CTkLabel(self.settings_right_frame, text="WAN", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.label_wan.grid(row=0, column=0, pady=20, sticky="n")

        # WAN Checkboxlar
        self.checkbox_ethernet = customtkinter.CTkCheckBox(self.settings_right_frame, text="Ethernet")
        self.checkbox_ethernet.grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.checkbox_ethernet.select()

        self.checkbox_wireless_ap = customtkinter.CTkCheckBox(self.settings_right_frame, text="wirelessAP")
        self.checkbox_wireless_ap.grid(row=2, column=0, padx=5, pady=5, sticky="w")

        self.checkbox_wireless_sta = customtkinter.CTkCheckBox(self.settings_right_frame, text="wirelessSTA")
        self.checkbox_wireless_sta.grid(row=3, column=0, padx=5, pady=5, sticky="w")

        # IP başlığı
        self.label_ip = customtkinter.CTkLabel(self.settings_right_frame, text="IP", font=customtkinter.CTkFont(size=18, weight="bold"))
        self.label_ip.grid(row=4, column=0, pady=(20, 10), sticky="w", columnspan=2)

        # Statik/Dinamik checkboxlar
        self.checkbox_static = customtkinter.CTkCheckBox(self.settings_right_frame, text="Statik")
        self.checkbox_static.grid(row=5, column=0, padx=5, pady=5, sticky="w", columnspan=2)
        self.checkbox_dynamic = customtkinter.CTkCheckBox(self.settings_right_frame, text="Dinamik")
        self.checkbox_dynamic.grid(row=6, column=0, padx=5, pady=5, sticky="w", columnspan=2)
        self.checkbox_dynamic.select()

        # IP ile ilgili label ve textboxlar (yan yana)
        self.label_ip_addr = customtkinter.CTkLabel(self.settings_right_frame, text="IP:")
        self.label_ip_addr.grid(row=7, column=0, padx=5, pady=5, sticky="w")
        self.entry_ip = customtkinter.CTkEntry(self.settings_right_frame)
        self.entry_ip.grid(row=7, column=1, padx=5, pady=5, sticky="ew")

        self.label_netmask = customtkinter.CTkLabel(self.settings_right_frame, text="Netmask:")
        self.label_netmask.grid(row=8, column=0, padx=5, pady=5, sticky="w")
        self.entry_netmask = customtkinter.CTkEntry(self.settings_right_frame)
        self.entry_netmask.grid(row=8, column=1, padx=5, pady=5, sticky="ew")

        self.label_gateway = customtkinter.CTkLabel(self.settings_right_frame, text="Gateway:")
        self.label_gateway.grid(row=9, column=0, padx=5, pady=5, sticky="w")
        self.entry_gateway = customtkinter.CTkEntry(self.settings_right_frame)
        self.entry_gateway.grid(row=9, column=1, padx=5, pady=5, sticky="ew")

        self.label_dns = customtkinter.CTkLabel(self.settings_right_frame, text="DNS:")
        self.label_dns.grid(row=10, column=0, padx=5, pady=5, sticky="w")
        self.entry_dns = customtkinter.CTkEntry(self.settings_right_frame)
        self.entry_dns.grid(row=10, column=1, padx=5, pady=5, sticky="ew")

        self.label_backup_dns = customtkinter.CTkLabel(self.settings_right_frame, text="Backup DNS:")
        self.label_backup_dns.grid(row=11, column=0, padx=5, pady=5, sticky="w")
        self.entry_backup_dns = customtkinter.CTkEntry(self.settings_right_frame)
        self.entry_backup_dns.grid(row=11, column=1, padx=5, pady=5, sticky="ew")

        self.label_console_ip = customtkinter.CTkLabel(self.settings_right_frame, text="Console IP:")
        self.label_console_ip.grid(row=12, column=0, padx=5, pady=5, sticky="w")
        self.entry_console_ip = customtkinter.CTkEntry(self.settings_right_frame)
        self.entry_console_ip.grid(row=12, column=1, padx=5, pady=5, sticky="ew")

        self.label_ping_time = customtkinter.CTkLabel(self.settings_right_frame, text="Ping Time:")
        self.label_ping_time.grid(row=13, column=0, padx=5, pady=5, sticky="w")
        self.entry_ping_time = customtkinter.CTkEntry(self.settings_right_frame)
        self.entry_ping_time.grid(row=13, column=1, padx=5, pady=5, sticky="ew")

        self.label_update_server = customtkinter.CTkLabel(self.settings_right_frame, text="Update Server:")
        self.label_update_server.grid(row=14, column=0, padx=5, pady=5, sticky="w")
        self.entry_update_server = customtkinter.CTkEntry(self.settings_right_frame)
        self.entry_update_server.grid(row=14, column=1, padx=5, pady=5, sticky="ew")

        self.settings_right_frame.grid_columnconfigure(1, weight=1)

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