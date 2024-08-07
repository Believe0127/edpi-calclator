import customtkinter as CTk

def main():
    def edpicalc():
        result_ent.configure(state="normal")
        result_ent.delete(0, CTk.END)
        result_ent.insert(0, str(int(dpi_ent.get()) * float(sens_ent.get())))
        result_ent.configure(state="readonly")

    CTk.set_appearance_mode("dark")
    CTk.set_default_color_theme("dark-blue")
    app = CTk.CTk()
    app.title("edpi計算機")
    app.geometry("250x300+820+300")
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
