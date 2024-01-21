import customtkinter as customtkinter
import tkinter as tkinter
import pytube as YouTube
import os 

#creating a root window

root = customtkinter.CTk()
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")


#setting title
root.title("YouTube Downloader")


#creating min and max window size, widthxheight
root.geometry("720x480") 
root.minsize(720,480)
root.maxsize(1080, 720)

#frame to hold content
content_frame = customtkinter.CTkFrame(root)
content_frame.pack(fill=customtkinter.BOTH, expand = True, padx=50, pady=50)
content_frame.pack_propagate(False)

#creating label and textentry widget for vdo url
url_label = customtkinter.CTkLabel(content_frame, text= "Enter YouTube url here")
entry_url = customtkinter.CTkEntry(content_frame, width= 400, height= 40)
url_label.pack(pady= ("10p", "5p"))
entry_url.pack(pady= ("10p", "5p"))



#to start
root.mainloop()




