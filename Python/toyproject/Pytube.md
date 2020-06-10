#### Pytube를 이용한 mp3다운로드


```
PyCharm, Anaconda 환경에서 실행시 

Error 발생
urllib.error.URLError: <urlopen error unknown url type: https>


Solution
From anaconda3\Library\bin copy below files and paste them in anaconda3/DLLs
-   libcrypto-1_1-x64.dll
-   libssl-1_1-x64.dll 

실행파일 만들기
  1) pip install pyinstaller
  ---- 기본형 (이렇게 하면 exe파일이 다른 폴더에서는 실행안됨)
  2) pyinstaller toy_pytube.py
  3) dist폴더에 생성된 exe파일 실행
  ---- one-file bundled executable
  2-1) pyinstaller -F -n toy_pybube_v2 toy_pytube.py   // -F: onefile   -n: NAME
  
  
  

```
```python
from pytube import YouTube
#from subprocess import run
#from moviepy.editor import AudioFileClip    # pyinstaller 수행시 에러발생해서 아래로 변경
from moviepy.audio.io.AudioFileClip import AudioFileClip
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import glob
import os


class PopFrame(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)

        self.master = master
        self.master.title("Music Download")
        self.pack(fill=BOTH, expand=True)

        frame1 = Frame(self)
        frame1.pack(fill=X)
        lbl_url = Label(frame1, text="Youtube URL:", width=20)
        lbl_url.pack(side=LEFT, padx=10, pady=10)

        entry_value = StringVar(self)
        entry_url = Entry(frame1, textvariable=entry_value)
        entry_url.pack(fill=X, padx=10, expand=True)

        frame2= Frame(self)
        frame2.pack(fill=X)
        lbl_result = Label(frame2, text="ready......", width=300)
        lbl_result.pack(side=LEFT, padx=10, pady=10)
        entry_url.bind('<Key>', lambda event, obj=lbl_result: self.result_init(event, obj))

        frame3 = Frame(self)
        frame3.pack(fill=X)
        btn_close = Button(frame3, text="Close", command=lambda:self.button_close())
        btn_close.pack(side=RIGHT, padx=10, pady=10)
        btn_save = Button(frame3, text="Save", command=lambda:button_pressed('save', entry_value, lbl_result))
        btn_save.pack(side=RIGHT, padx=10, pady=10)

    def result_init(self, event, obj):
       # print("Single Click, Button" + event.type)
        obj.configure(text="ready......")

    def button_close(self):
        self.master.destroy()


def button_pressed(value, entry_value, lbl_result):
    if not (entry_value.get() == '') and (entry_value.get().startswith('http://') or entry_value.get().startswith('https://')):
        down_file(entry_value, lbl_result)
    else:
        messagebox.showerror("Error", "please, http://  or  https://")


def down_file(entry_value, lbl_result):
    yt = YouTube(entry_value.get())
    ytfilter = yt.streams.filter(only_audio=True, subtype='mp4')
    print(ytfilter)

    ytfilter.first().download()
    print("download success!")

    files = glob.glob("*.mp4")
    tmpdir = os.getcwd() + "\\"

    for x in files:
        if os.path.isfile(tmpdir + x):
            filename = os.path.splitext(x)
            sourceFile = tmpdir + filename[0] + ".mp4"
            targetFile = tmpdir + filename[0] + ".mp3"
            print(sourceFile)
            print(targetFile)

            # run(["mplayer", "-novideo", "-nocorrect-pts", "-ao", "pcm:waveheader", sourceFile], shell=True)  # mplayer error
            # run(["lame", "-v", "audiodump.wav", targetFile], shell=True) #lame error
            # os.remove("audiodump.wav")

            audioclip = AudioFileClip(sourceFile)
            audioclip.write_audiofile(targetFile)
            audioclip.close()

            if os.path.isfile(targetFile):
                lbl_result.configure(text="download success! - " + filename[0] + ".mp3")
                entry_value.set('')

            if os.path.isfile(sourceFile):
                os.remove(sourceFile)


def main():
    root = Tk()
    root.geometry("700x150+100+100")
    app = PopFrame(root)
    root.mainloop()


if __name__ == '__main__':
    main()

```
