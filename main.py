import requests
import customtkinter
from PIL import ImageTk, Image

customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("dark-blue")
app = customtkinter.CTk()
app.title("Unit Converter")
app.geometry("1250x625")


def api():

    url = "https://measurement-unit-converter.p.rapidapi.com/length"

    # Get the values from entry widgets
    value = entry.get()
    from_unit = drop_down.get()
    to_unit = drop_down2.get()

    # Validate if the value is numeric
    try:
        float(value)  # Try converting the value to a float
    except ValueError:
        l3.configure(text="Error: Please enter a valid number")
        return  # Exit the function if the value is not numeric

    querystring = {"value": value, "from": from_unit, "to": to_unit}
    # Change To your own API key. If you can do please read the documentation given.
    headers = {
        "X-RapidAPI-Key": "<YOUR API KEY>",
        "X-RapidAPI-Host": "<YOUR API HOST>"
    }

    response = requests.get(url, headers=headers, params=querystring)
    data = response.json()

    # Assuming the API response has a key "result" containing the conversion result
    if "result" in data:
        l3.configure(text=data["result"])  # Update the text of the label with the conversion result
    else:
        l3.configure(text="Error: Conversion failed")


bg = ImageTk.PhotoImage(Image.open(r"C:\Users\utsav\OneDrive\Desktop\Python Projects\Unit-Converter\Background.jpg"))
lable = customtkinter.CTkLabel(app, image=bg)
lable.pack()

frame = customtkinter.CTkFrame(app, width=400, height=400, corner_radius=15, bg_color="#000000")
frame.place(relx=0.5, rely=0.5, anchor="center")

entry = customtkinter.CTkEntry(app, placeholder_text="Enter your number.", fg_color="black", corner_radius=15,
                               height=50, width=150, bg_color="#212121")
entry.place(relx=0.5, rely=0.4, anchor="center")
#
# entry2 = customtkinter.CTkEntry(app, placeholder_text="Enter your unit.", fg_color="black", corner_radius=15,
#                                 height=50, width=150, bg_color="#212121")
# entry2.place(relx=0.57, rely=0.4, anchor="center")

l2 = customtkinter.CTkLabel(app, text="Unit Converter", font=('Century Gothic', 30), bg_color="#212121")
l2.place(relx=0.5, rely=0.25, anchor="n")

l3 = customtkinter.CTkLabel(app, text="", bg_color="#212121")
l3.place(relx=0.5, rely=0.7, anchor="center")
mesurments = ["nm",
              "μm",
              "mm",
              "cm",
              "m",
              "km",
              "in",
              "yd",
              "ft-us",
              "ft",
              "fathom",
              "mi",
              "nMi"]
drop_down = customtkinter.CTkComboBox(app, values=mesurments, bg_color="#212121")
drop_down.place(relx=0.43, rely=0.5, anchor="center")

drop_down2 = customtkinter.CTkComboBox(app, values=mesurments, bg_color="#212121")
drop_down2.place(relx=0.58, rely=0.5, anchor="center")

button = customtkinter.CTkButton(app, text="Convert", bg_color="#212121", corner_radius=15, command=api)
button.place(relx=0.5, rely=0.6, anchor="center")
app.mainloop()
