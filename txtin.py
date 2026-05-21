import tkinter as tk

global rets 

rets=""


class myapps:
    def __init__(self,root:tk.Tk,title:str,backgrounds:str,foregrounds:str):
        self.root=root
        self.root.title(title)
        self.root.configure(background=backgrounds)
        self.text=tk.Text(background=backgrounds,foreground=foregrounds)
        self.text.pack(padx=10,pady=10)
        self.button=tk.Button(background=backgrounds,foreground=foregrounds,text="ok",command=self.oks)
        self.button.pack(padx=10,pady=10)
    def oks(self):
          global rets
          a=self.text.get("1.0",tk.END)
          rets=a
          self.root.quit()



def inputs(title:str="input texts",backgrounds:str="black",foregrounds:str="white"):
           root=tk.Tk()
           apps=myapps(root,title,backgrounds,foregrounds)
           root.mainloop()
           return rets
