from breezypythongui import EasyFrame

class MyApp(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, title="My GUI App")
        self.addLabel("Hello, World!", row=0, column=0)
        self.addButton("Click Me", row=1, column=0, command=self.sayHello)

    def sayHello(self):
        self.messageBox("Message", "You clicked the button!")

app = MyApp()
app.mainloop()