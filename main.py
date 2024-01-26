class ToDoList:
        def __init__(self):
                self.tasks = []
        
        def AddTask(self, task):
                self.tasks.append(task)
                print(self.tasks)
        def RemoveTask(self, task):
                if task in self.tasks:
                        self.tasks.remove(task)
                else:
                        print(f'{task} is in List')
        def DisplayList(self,):
                if self.tasks !=0:
                        for i in self.tasks:
                                print(f'{i}')                                
def main():
        ToDo = ToDoList()
        while 1:
                print(f'1]SHow List\n2]Add Task to List\n3]Remove Task from List\n4]Exit To-Do List')
                Choise = int(input('Choose 1 option from above: '))
                
                if Choise == 1:
                        ToDo.DisplayList()
                elif Choise == 2:
                        task = input("Add to List: ")
                        ToDo.AddTask(task)
                elif Choise == 3:
                        task = input("Remove from list: ")
                        ToDo.RemoveTask(task)
                elif Choise == 4:
                        exit()
                else:
                        print("Choose Write option from above")
main()
 