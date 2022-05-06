from cgitb import text
from doctest import master
from turtle import width
import chromedriver_autoinstaller
from selenium import webdriver
import tkinter
import customtkinter
from tkfontawesome import icon_to_image 
import webbrowser
import requests
from bs4 import BeautifulSoup
from tkinter import messagebox
import shutil

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"

class App(customtkinter.CTk):
  ncopies = 3
  defaultNameFile= 'proxies'
  def __init__(self):
    super().__init__()
    # Iconos
    github = icon_to_image("github", fill="black", scale_to_width=20)  
    # Configurar ventana principal
    self.title("Proxy Scrapper v1.0")
    self.geometry("450x300")
    self.resizable(False, False)
    self.protocol("WM_DELETE_WINDOW", self.on_closing)
    self.grid_columnconfigure(0, weight=1)
    self.grid_rowconfigure(0, weight=0)
    self.grid_rowconfigure(1, weight=1)

    # Frame de arriba
    self.frame_up = customtkinter.CTkFrame(master=self, width=440)
    self.frame_up.grid(row=0, column=0, padx=10, pady=10, sticky="nswe")
    self.frame_up.rowconfigure(0, minsize=80)

    self.file_name_label = customtkinter.CTkLabel(master=self.frame_up,text="Enter file name: ")
    self.file_name_label.grid(row=0, column=0)
    self.file_name_input = customtkinter.CTkEntry(master=self.frame_up, placeholder_text="File name")
    self.file_name_input.grid(row=0, column=1, columnspan=2, pady=20, padx=20, sticky="we")
    self.file_name_input.insert('end',str(self.defaultNameFile))

    # Slider para las copias
    self.slider_1 = customtkinter.CTkSlider(master=self.frame_up, from_=0, to=4, number_of_steps=4, command=self.update_copies)
    self.slider_1.grid(row=2, column=0, columnspan=3, pady=10, padx=50, sticky="we")
    self.label_slider = customtkinter.CTkLabel(master=self.frame_up,text='Copies: {numberCopies}'.format(numberCopies= self.slider_1.get()).split('.')[0])
    self.label_slider.grid(row=1, column=1, pady=10, padx=10)

    # Labels vacias para recolocar
    self.label_1 = customtkinter.CTkLabel(master=self.frame_up,text="")
    self.label_1.grid(row=3, column=0, pady=10, padx=10)
    self.label_2 = customtkinter.CTkLabel(master=self.frame_up,text="")
    self.label_2.grid(row=3, column=2, pady=10, padx=10)

    # Boton para descargar los proxies
    self.proxy_button = customtkinter.CTkButton(master=self.frame_up,text="Get Proxies",fg_color=("gray75", "gray30"), command=lambda:self.get_proxies(), compound = 'left')
    self.proxy_button.grid(row=3, column=1, pady=10, padx=20, sticky="w", rowspan=2)

    # Frame inferior donde esta el boton de github
    self.frame_bottom = customtkinter.CTkFrame(master=self)
    self.frame_bottom.grid(row=1, column=0,padx=10, pady=10, sticky="we")
    self.frame_bottom.grid_columnconfigure(0, weight=1)

    #Boton de github
    self.github_button = customtkinter.CTkButton(master=self.frame_bottom,text="Github",fg_color=("gray75", "gray30"), command=lambda:self.open_github(), image = github, compound = 'left')
    self.github_button.grid(row=0, column=0, pady=10, padx=20, sticky="we")

  def update_copies(self,val):
    # Funcion para actualizar las copias
    self.ncopies = str(self.slider_1.get()).split('.')[0]
    self.label_slider.config(text='Copies: {numberCopies}'.format(numberCopies= val).split('.')[0])

  def open_github(self):
      webbrowser.open('https://www.github.com/vicnx', new=0, autoraise=True)

  def get_proxies(self):
      with open('{name}.txt'.format(name=self.file_name_input.get()), 'bw') as f:
        # First webpage API method
        url1 = 'https://www.proxy-list.download/api/v1/get?type=http'
        r1 = requests.get(url1)
        f.write(r1.text.encode())

        # Another webpage (bs method)
        url2 = 'https://free-proxy-list.net'
        r2 = requests.get(url2)
        bs = BeautifulSoup(r2.text, 'lxml')
        table = bs.find('tbody')
        rows = table.find_all('tr')
        for row in rows:
          proxy = row.contents[0].text + ':'+ row.contents[1].text + '\n'
          f.write(proxy.encode())

      with open('{name}.txt'.format(name=self.file_name_input.get()), 'r+') as fileRead:

        x = len(fileRead.readlines())
        # Copias de archivos
        if int(self.ncopies) > 1:
          for i in range(int(self.ncopies)):
            shutil.copyfile('{name}.txt'.format(name=self.file_name_input.get()), '{name}.txt'.format(name=self.file_name_input.get()+str(i+1)))

        #mensaje de OK
        messagebox.showinfo(message='Saved {x} proxies.'.format(x=x), title="Information")

  # def check_proxies(self):
  #           # line = 'http://' + ip + ':' + port
  #         # proxies = { 'http': line, 'https': line }
  #         # try:
  #         #   testIP = requests.get('https://httpbin.org/ip', proxies = proxies, timeout = 3)
  #         #   print(testIP.text)
  #         #   resIP = testIP.json()['origin']
  #         #   origin = resIP.split(',')
            
  #         #   if origin[0] == ip:
  #         #       print('  Proxy ok! Appending proxy to proxyList...')
  #         #       proxyList.append(line)
  #         #       count += 1
  #         #       if count == 5:
  #         #           break
  #         # except:    
  #         #   print('Bad proxy')

  def start(self):
        self.mainloop()

  def on_closing(self, event=0):
        self.destroy()


if __name__ == "__main__":
    app = App()
    app.start()