from tkinter import *
import customtkinter
import openai
import os
import pickle

#first

root=customtkinter.CTk()
root.title("ChatGPT Asistans")
root.geometry('600x490')
root.iconbitmap('gptıcon.ico')

#theme
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme('dark-blue')
#function 
def speak():
    if chat_entry.get():
        filename="api_key"
        try:
            if os.path.isfile(filename):
                input_file=open(filename,'rb')
                api_password=pickle.load(input_file)

                openai.api_key=api_password
                openai.Model.list()

                answer=openai.Completion.create(
                    model="text-davinci-003",
                    prompt=chat_entry.get(),
                    temperature=0.5,
                    max_tokens=1000,
                    top_p=1.0,
                    frequency_penalty=0.0,
                    presence_penalty=0.0
                )
                my_text.insert(END,(answer["choices"][0]["text"]).strip())
                my_text.insert(END,"\n\n")

            else:
                input_file=open(filename,'wb')
                input_file.close()
                my_text.insert(END,"API key not found\nhttps://platform.openai.com/account/api-keys")
        except Exception as e:
            my_text.insert(END,f"\n\n An error occurred{e}")
    else:
            my_text.insert(END,"\n\n Please write your question")

    
def clear():
    my_text.delete(1.0,END)
    chat_entry.delete(0,END)

    
def key():
    filename="api_key."
    try:
        if os.path.isfile(filename):
            input_file=open(filename,'rb')
            api_password=pickle.load(input_file)
            api_entry.insert(END,api_password)

        else:
            input_file=open(filename,'wb')
            input_file.close()
    except Exception as e:
        my_text.insert(END,f"\n\n An error occurred{e}")

    root.geometry("600x600")
    api_frame.pack(pady=10)
    
def save_key():

    filename="api_key"
    try:
        output_file=open(filename,'wb')
        pickle.dump(api_entry.get(),output_file)
        api_entry.delete(0,END)
        api_frame.pack_forget()
    except Exception as e:
        my_text.insert(END,f"\n\n An error occurred{e}")
    root.geometry("600x490")
    

#text frame
text_frame=customtkinter.CTkFrame(root)
text_frame.pack(pady=20)
my_text=Text(text_frame,bg="#343638",width=65,bd=1,relief="flat",wrap=WORD,selectbackground="#660099")
my_text.grid(row=0,column=0)

#scrollbar
text_scroll=customtkinter.CTkScrollbar(text_frame,command=my_text.yview)
text_scroll.grid(row=0,column=1,sticky="ns")
my_text.configure(yscrollcommand=text_scroll.set)

#entry
chat_entry=customtkinter.CTkEntry(root,placeholder_text="What would you like to ask Chat GPT?",width=535,height=50,border_width=1)
chat_entry.pack(pady=10)

#button frame
button_frame=customtkinter.CTkFrame(root,fg_color="#343638")
button_frame.pack(pady=10)

submit_button=customtkinter.CTkButton(button_frame,text="Ask to Chat GPT",command=speak,fg_color="#660099",hover_color="#808080")
submit_button.grid(row=0,column=0,padx=20,)

clear_button=customtkinter.CTkButton(button_frame,text="Clear Answers",command=clear,fg_color="#660099",hover_color="#808080")
clear_button.grid(row=0,column=1,padx=20)

api_button=customtkinter.CTkButton(button_frame,text="Update Api key",command=key,fg_color="#660099",hover_color="#808080")
api_button.grid(row=0,column=2,padx=20)

#Api key frame
api_frame=customtkinter.CTkFrame(root,border_width=1)
api_frame.pack(pady=10)

api_entry=customtkinter.CTkEntry(api_frame,placeholder_text="Enter new api key",width=350,height=50,border_width=1)
api_entry.grid(row=0,column=0,padx=20,pady=20)

api_save_button=customtkinter.CTkButton(api_frame,text="Save key",command=save_key,fg_color="#660099",hover_color="#808080")
api_save_button.grid(row=0,column=1,padx=10)
root.mainloop()