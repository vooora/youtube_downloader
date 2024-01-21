import customtkinter as customtkinter
import tkinter as tkinter
from tkinter import ttk 
import pytube as YouTube
import os 

def download_video():
    #url = entry_url.get()  
    url =  "https://youtu.be/0hEmxOEeVO0?si=5A_1rgGtN__ngbjS"
    resolution = resolution_var.get()

    progress_label.pack(pady= ("10p", "5p"))
    progress_bar.pack(pady= ("10p", "5p"))
    status_label.pack(pady= ("10p", "5p"))

    try:
        yt = YouTube(url)
        stream = yt.streams.filter(res=resolution).first()
        #downoad the video into a specific directory
        #os.path.join("download", title: f"{yt.title}.mp4")
        os.path.join("downloads")

        stream.download(output_path = "downloads")
        status_label.configure(text="downloaded!", fg= "fff")
        progress_label.configure(text=str(int(percentage_completed)) + '%')
        progress_label.update()
        progress_bar.set(float(percentage_completed/100))

    except Exception as e:
        status_label.configure(text=f"Error {str(e)}")
        print()

def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize()
    bytes_downloaded = total_size - bytes_remaining
    percentage_completed= bytes_downloaded/total_size * 100
    print(percentage_completed)


#creating a root window

root = tkinter.Tk()
#tkinter.set_appearance_mode("System")
#tkinter.set_default_color_theme("blue")

#setting title
root.title("YouTube Downloader")

#creating min and max window size, widthxheight
root.geometry("720x480") 
root.minsize(720,480)
root.maxsize(1080, 720)

#frame to hold content
content_frame = tkinter.Frame(master = root)
content_frame.pack(fill="both", expand = True, padx=10, pady=10)

#creating label and textentry widget for vdo url
#url_label = customtkinter.CTkLabel(content_frame, text= "Enter YouTube url here")
#entry_url = customtkinter.CTkEntry(content_frame, width= 400, height= 40)
url_label = tkinter.Label(content_frame, text= "Enter YouTube url here")
entry_url = tkinter.Text(content_frame, width=50, height=3)
url_label.pack(pady= ("10p", "5p"))
entry_url.pack(pady= ("10p", "5p"))

download_button = tkinter.Button(content_frame, text= "Download", command=download_video)
download_button.pack(pady= ("10p", "5p"))

resolutions =["720p", "360p", "240p"]
resolution_var = customtkinter.StringVar()
resolution_combobox= ttk.Combobox(content_frame, textvariable=resolution_var)
resolution_combobox.pack(pady= ("10p", "5p"))
resolution_combobox.set("720p")

progress_label = tkinter.Label(content_frame, text= "0%")

progress_bar = customtkinter.CTkProgressBar(content_frame, width= 400)
progress_bar.set(0.6)

status_label = tkinter.Label(content_frame, text= "Downloaded")
status_label.pack(pady= ("10p", "5p"))






#to start
root.mainloop()




