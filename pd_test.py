#For searching price in the list
import re

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
#Sum
        if(self.action_v == "Sum"):
            self.action_sum()



    def action_add(self):
        text = input("What product you want to add?(Please follow instruction *Food - Price*): ")
        
        with open(self.file , "a+") as file:
            # file.write("\n")
            file.write(text + "\n")
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

    def action_sum(self):
        sum = 0
        with open(self.file , "r") as file:
            for line in file.readlines():
                result = line[:-1].split("-")
                sum += int(result[-1])
                
            # for line in lines:
            #     print(line)
            #     if(line == " "):
            #         continue
            #     sum += int((re.search("- (.*)\n" , line)).group(1))

        print(f"Overall sum of the products in your list is : {sum}")        


#What actions can be done: Add to file, Make changes in list, Delete from list, Sum of the products.
file_name = input("Please enter name of the file: ")
action_1 = input("What action you want to perform? \nAdd , Change, Delete, Overall sum - ")
test = PythonTest(file_name , action_1)
#test.action(action)