class PythonTest:
    def __init__(self , filename , action) -> None:
        self.file = filename
        self.action_v = action
        self.action(action)

#Here we will ask user to say what action they want to do and call 
    def action(self , action):
#        self.action_v = action
#Add
        if(self.action_v == "Add"):
            self.action_add()
#Change
        if(self.action_v == "Change"):
            self.action_change()
#Delete
        if(self.action_v == "Delete"):
            self.action_delete()
        

    def action_add(self):
        text = input("What product you want to add?(Please follow instruction Food - Price")
        
        with open(self.file , "a+") as file:
            file.write("\n")
            file.write(text)
        file.close()

    def action_change(self):
        text = input("Which food you want to change?")
        change = input("Change to what price?")

        info = []
        with open(self.file , "r") as file:
            for line in file:
                info.append(line.strip())
            for i in range(len(info)):
                if (text in info[i]):
                    info[i] = text + " - " + change

        with open(self.file , "w") as file:
            for i in range(len(info)):
                file.write(info[i] + "\n")

    def action_delete(self):
        text = input("Which food you want to remove?")
        with open(self.file , "r") as file:
            lines = file.readlines()
        
        with open(self.file , "w") as file:
            for line in lines:
                if text not in line:
                    file.write(line)

    
            
                


#What actions can be done: Add to file, Make changes in list, Delete from list, Overall sum.
action_1 = input("What action you want to perform? \nAdd , Change, Delete, Overall sum - ")
test = PythonTest("filename.csv" , action_1)
#test.action(action)