from customtkinter import CTk, set_appearance_mode

class window(CTk):
    def __init__(self, geo="250x250", mode="System", title="Infinite craft hack") -> None:
        super().__init__()
        self.geometry(geo)
        set_appearance_mode(mode)
        self.title(title)

    def change_geo(self, new_geo):
        self.geometry(new_geo)


    


        

        

