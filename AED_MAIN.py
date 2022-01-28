
from pickle import FALSE
from re import S
import tkinter as tk



class AED_Main():
    

    def __init__(self):
        f = open("Logged.txt","r",encoding="Utf-8")
        for l in f:
            LoggedInfo = l.split(";")
            if LoggedInfo[2] != "TRUE":
                exit()
      
        
        #File Path Pre feito serve pra teste apenas // URGENTE MUDAR !!!
        self.Universidade="ESMAD"
        self.curso="1"
        self.data_folder = "InfoCursos\\"+self.Universidade+"\\"
        self.file_to_open = self.data_folder + self.curso +".txt"

        #Opening Files
        self.f = open(self.file_to_open,encoding="utf-8")
        self.Textos=[]
        
        

        for l in self.f:
            a = l.split(";")
            self.Textos.append(a)
        print(self.f.read())
        self.f.close()
        print(self.Textos)
        
        # Variaveis uteis !!! Em que texto Vamos --> i || Ntextos --> verifica numero de textos 
        
        self.i=2
        self.Ntextos=len(self.Textos)-1

        self.root = tk.Tk()

        #Get the current screen width and height
        self.screen_width = self.root.winfo_screenwidth()
        self.screen_height = self.root.winfo_screenheight()

        #Text Box com nome do curso
        self.NomeCurso = tk.Text(self.root ,height=10, width=30)
        self.NomeCurso.insert(tk.END, self.Textos[self.i][0])
        self.NomeCurso.pack()


        #Text Box com Titulos
        self.Titulo = tk.Text(self.root ,height=1, width=30)
        self.Titulo.insert(tk.END, self.Textos[self.i][1])
        self.Titulo.pack()


        #Text Box com texto
        self.Texto = tk.Text(self.root ,height=10, width=30)
        self.Texto.insert(tk.END, self.Textos[self.i][2])
        self.Texto.pack()

        #frame para os butoes
        self.FrameButtons = tk.Frame(self.root)

    
        #butao -1 
        self.ButaoMudartextoesquerda = tk.Button(self.FrameButtons, text='<-')
        self.ButaoMudartextoesquerda.bind('<Button-1>',self.Esquerda)

        
        #confirmar mudança
        self.ButaoEnviartexto = tk.Button(self.FrameButtons, text='Change')
        self.ButaoEnviartexto.bind('<Button-1>',self.Change)

            
        #butao +1 
        self.ButaoMudartextodireta = tk.Button(self.FrameButtons, text='->',)
        self.ButaoMudartextodireta.bind('<Button-1>',self.Direita)

        #orientação butoes
        self.ButaoMudartextoesquerda.pack(side=tk.LEFT)
        self.ButaoEnviartexto.pack(side=tk.LEFT)
        self.ButaoMudartextodireta.pack(side=tk.LEFT)

        self.FrameButtons.pack()

        self.root.mainloop()

    def Esquerda(self,a):
        

        if( self.i > 2):
            self.i-=1

            self.NomeCurso.delete("1.0","end")
            self.NomeCurso.insert(tk.END, self.Textos[self.i][0])
            #Titulo
            self.Titulo.delete("1.0","end")
            self.Titulo.insert(tk.END, self.Textos[self.i][1])
            #Texto
            self.Texto.delete("1.0","end")
            self.Texto.insert(tk.END, self.Textos[self.i][2])

            print(self.i)
        return


    def Direita(self,a):
        

        if( self.i < self.Ntextos):
            self.i+=1
            
            self.NomeCurso.delete("1.0","end")
            self.NomeCurso.insert(tk.END, self.Textos[self.i][0])
            #Titulo
            self.Titulo.delete("1.0","end")
            self.Titulo.insert(tk.END, self.Textos[self.i][1])
            #Texto
            self.Texto.delete("1.0","end")
            self.Texto.insert(tk.END, self.Textos[self.i][2])

            print(self.i)

        return
                
    def Change(self,a):

        
        print("Change")

        #Mudar Texto
        self.Textos[self.i][0]=self.NomeCurso.get("1.0","end"+"-1c")
        self.Textos[self.i][1]=self.Titulo.get("1.0","end"+"-1c")
        self.Textos[self.i][2]=self.Texto.get("1.0","end"+"-1c")

        
        #

        self.f = open(self.file_to_open,"w",encoding="Utf-8")
        l=0
        while l != len(self.Textos)-1:
           self.f.write(self.Textos[l][0] + ";" +self.Textos[l][1] + ";" + self.Textos[l][2] + "\n")
           l+=1
        self.f.close()





AED_Main()