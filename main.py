from pytube import YouTube
from tkinter import *
from tkinter.filedialog import *
from tkinter.messagebox import *

file_size = 0

def startDownload():
    global file_size
    try:
        url = urlField.get()
        print(url)
        # Changing button text
        dBtn.config(text="Please wait...")
        dBtn.config(state=DISABLED)
        save_video_to = askdirectory()
        print(save_video_to)
        if save_video_to is None:
            return
        # url = "https://youtu.be/OXi4T58PwdM"
        # save_video_to = "C:\\Users\\shyam\\Videos"
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
main.geometry("500*600")
file = PhotoImage(file='youtube.png')
headingIcon = Label(main, image=file)
headingIcon.pack(side=TOP)
urlField = Entry(main, font=("verdana", 18), justify=CENTER)
urlField.pack(side=TOP, fill=X, padx=10)
# download button
dBtn = Button(main, text="start download", command=startDownload())
dBtn.pack(side=TOP, pady=10)
main.mainloop()
