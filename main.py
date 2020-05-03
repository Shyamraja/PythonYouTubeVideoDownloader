from pytube import *
import tkinter as tk
from tkinter.filedialog import *
from tkinter.messagebox import *
from threading import *

# total size of container
file_size = 0


# updating download percentage...
def progress(stream=None, chunk=None, file_handle=None, remaining=None):
    # shows percentage of downloaded portion of file
    file_downloaded = (file_size - remaining)
    percentage = (file_downloaded / file_size) * 100
    dBtn.config(text="{:00.0f} % downloaded".format(percentage))


def start_download():
    global file_size
    try:
        url = urlField.get()
        print(url)
        # Changing button text as needed
        dBtn.config(text="Please wait...")
        dBtn.config(state=DISABLED)
        save_video_to = askdirectory()
        print(save_video_to)
        if save_video_to is None:
            return
        # creating object as youtube object with url
        ob = YouTube(url, on_progress_callback=progress)
        # strms = ob.streams.all()
        # for s in strms:
        # print(s)
        # I choose to print only first streams out of all
        stream = ob.streams.first()
        # print(stream)
        # Below informations are for video inforamtions
        # print(stream.filesize)
        # print(stream.title)
        # print(ob.description)
        stream.download(save_video_to)
        print("done...")
        dBtn.config(text="Start Download")
        dBtn.config(state=NORMAL)
        showinfo("Download Finished", "Successfully Downloaded")

    except Exception as e:
        print(e)
        print("error !!")


main = Tk()
main.title("YouTube Downloader")
main.iconbitmap('icon.ico')
main.geometry("300x400")
file = PhotoImage(file='youtube.png')
headingIcon = Label(main, image=file)
headingIcon.pack(side=TOP)
urlField = Entry(main, font=("verdana", 18), justify=CENTER)
urlField.pack(side=TOP, fill=X, padx=10)
# download button
dBtn = Button(main, text="start download", font=("verdana", 18), relief='ridge', command=start_download())
dBtn.pack(side=TOP, pady=10)
main.mainloop()
