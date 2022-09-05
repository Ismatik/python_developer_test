class PythonTest:
    def __init__(self , filename) -> None:
        self.file = filename

#Here we will ask user to say what action they want to do and call 
    def action(self , action):
        self.action = action

        if(self.action == "Add"):
            self.action_add()

    def action_add(self):
        text = input("What product you want to add?(Please follow instruction Food - Price")
        with open(self.file , "a+") as file:
            file.write("\n")
            file.write(text)



#What actions can be done: Add to file, Make changes in list, Delete from list, Overall sum.
action = "Add"
test = PythonTest("filename.csv")
test.action(action)