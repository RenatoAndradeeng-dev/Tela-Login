import customtkinter as ctk
from tkinter import*
import database 
from tkinter import messagebox

janela = ctk.CTk()


class application():

    def __init__(self):
        self.janela= janela
        self.tema()
        self.tela()
        self.tela_login()
        janela.mainloop()
        
    def tema(self):
        ctk.set_appearance_mode('dark')
        ctk.set_default_color_theme('dark-blue')


    def tela(self): 
    
        self.janela.geometry('700x400')
        self.janela.title('Sistema de login')
        self.janela.iconbitmap('ico.ico')
        self.janela.resizable(False, False)

    
    def tela_login(self):
    #importando a imagem
        img = PhotoImage(file='Logo5.png')
        label_img = ctk.CTkLabel(master=janela, image=img, text=None).place(x=85, y=85)
        
        
    #frame
        login_frame = ctk.CTkFrame(master=janela, width=350, height=396)
        login_frame.pack(side=RIGHT)

    #widgets dentro da frame da tela de login
        label = ctk.CTkLabel(master=login_frame, text='Sistema de Login', font=('Roboto', 
        20)).place(x=25, y=5)
      
        username_entry = ctk.CTkEntry(master=login_frame, placeholder_text='Nome do usuario', width=300
        ,font=('Roboto', 14)).place(x=25, y=105)

        username_label = ctk.CTkLabel(master=login_frame, text='nome do usuario é obrigatorio'
        ,text_color='green', font=('Roboto', 10)).place(x=25, y=135)

       
        passoword_entry = ctk.CTkEntry(master=login_frame, placeholder_text='Senha do usuario'
        ,width=300, font=('Roboto', 14), show='*').place(x=25, y=175)

        passoword_label = ctk.CTkLabel(master=login_frame, text='senha do usuario é obrigatorio'
        ,text_color='green', font=('Roboto', 10)).place(x=25, y=205) 


        checkBox = ctk.CTkCheckBox(master=login_frame, text='Lembrar senha').place(x=25, y=233)

        def login():
            
            msg = messagebox.showinfo(title='Estado de Login', message='Parabens! Login feito com sucesso.')
            pass
        login_button = ctk.CTkButton(master=login_frame, text='LOGIN', width=300, command=login).place(x=25, y=285)
        
        cadastrar_span = ctk.CTkLabel(master=login_frame, text="Não tenho conta").place(x=25, y=325)
        
        def tela_cadastrar():
            #removendo o frame de login
            login_frame.pack_forget()
            #Criando a tela de cadastro de usuarios
            cds_frame = ctk.CTkFrame(master=janela, width=350, height=396)
            cds_frame.pack(side=RIGHT)
            
            label = ctk.CTkLabel(master=cds_frame, text='Cadastre-se a baixo', font=('Roboto', 
            20)).place(x=25, y=5)
            
            
            span = ctk.CTkLabel(master=cds_frame, text='Por favor preencha todos os campos com dados corretos.', 
            font=('Roboto', 12), text_color='gray').place(x=25, y=65)

            username_entry = ctk.CTkEntry(master=cds_frame, placeholder_text='Nome do usuario', width=300,
            font=('Roboto', 14)).place(x=25, y=105)
            
            email_entry = ctk.CTkEntry(master=cds_frame, placeholder_text='E-mail do usuario', width=300,
            font=('Roboto', 14)).place(x=25, y=145)
            
            passoword_entry = ctk.CTkEntry(master=cds_frame, placeholder_text='Senha do usuario', width=300,
            font=('Roboto', 14),show='*').place(x=25, y=185)
            
            Cpassoword_entry = ctk.CTkEntry(master=cds_frame, placeholder_text='Confirmar senha', width=300,
            font=('Roboto', 14),show='*').place(x=25, y=265)
            
            checkBox = ctk.CTkCheckBox(master=cds_frame, text='Aceito todos os termos e Politicas.').place(x=25, y=233)
            
            def back():
                #Removendo o frame de cadastro 
                cds_frame.pack_forget()
                
                #Devolvendo frame de login
                login_frame.pack(side=RIGHT)
                
            
            back_button = ctk.CTkButton(master=cds_frame, text='VOLTAR', width=145, fg_color='gray',
            hover_color='#202020', command=back).place(x=25, y=300)
            
            def save_user():
                msg = messagebox.showinfo(title='Estado do Cadastro', message='Parabens! Usuario cadastrado com sucesso.')
            
            save_button = ctk.CTkButton(master=cds_frame, text='CADASTRAR', width=145, fg_color='green', 
            hover_color='#014B05', command=save_user).place(x=180, y=300)
            
            
        cadastrar_button = ctk.CTkButton(master=login_frame, text='CADASTRE-SE', width=150,
        fg_color='green', hover_color='#2D9334',command=tela_cadastrar).place(x=175, y=325)

            
        

application()