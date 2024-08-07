import customtkinter as CTk

def main():
    def edpicalc():
        result_ent.configure(state="normal")
        result_ent.delete(0, CTk.END)
        result_ent.insert(0, str(int(dpi_ent.get()) * float(sens_ent.get())))
        result_ent.configure(state="readonly")
    
    data = '''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'''

    CTk.set_appearance_mode("dark")
    CTk.set_default_color_theme("dark-blue")
    app = CTk.CTk()
    app.title("edpi計算機")
    app.geometry("250x300+820+300")
    app.iconbitmap(data)
    app.resizable(height=False, width=False)

    dpi_lbl = CTk.CTkLabel(master=app, text="dpi: ", font=("Meiryo UI", 23))
    dpi_lbl.place(x=20, y=40)
    dpi_ent = CTk.CTkEntry(master=app, width=160, height=35, corner_radius=3, placeholder_text="800", font=("Meiryo UI", 18), border_color="#e3e3e3")
    dpi_ent.place(x=70, y=40)

    sens_lbl = CTk.CTkLabel(master=app, text="感度: ", font=("Meiryo UI", 23))
    sens_lbl.place(x=10, y=100)
    sens_ent = CTk.CTkEntry(master=app, width=160, height=35, corner_radius=3, placeholder_text="1.2", font=("Meiryo UI", 18), border_color="#e3e3e3")
    sens_ent.place(x=70, y=100)

    result_lbl = CTk.CTkLabel(master=app, text="edpi: ", font=("Meiryo UI", 23))
    result_lbl.place(x=10, y=160)
    result_ent = CTk.CTkEntry(master=app, width=160, height=35, corner_radius=3, state="readonly", font=("Meiryo UI", 18), border_color="#e3e3e3")
    result_ent.place(x=70, y=160)

    send_btn = CTk.CTkButton(master=app, text="計算", height=35, width=80, font=("Meiryo UI", 18), corner_radius=2.5, fg_color="#343434", text_color="lightgreen", hover_color="#454545", command=edpicalc)
    send_btn.place(x=80, y=220)
    
    made_by_kinoko = CTk.CTkLabel(master=app, text="Author: kinoko", font=("Meiryo UI", 13))
    made_by_kinoko.place(x=145, y=267)

    app.mainloop()

if __name__ == "__main__":
    main()