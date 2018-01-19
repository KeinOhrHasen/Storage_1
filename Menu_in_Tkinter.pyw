#Menu in restaurant "Yurii's Restauration"
from tkinter import *

class Application(Frame):
    '''My favourite class'''
    def __init__(self, master):
        '''initialization'''
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()


    def create_widgets(self):
        '''Menu frame with dishes, prices and add offers '''
        #Menu
        Label(self, text = "\tMenu by \'Yurii's Restauration\'"
              ).grid(row = 0, column = 0, columnspan = 3, sticky  = W)
        
        #Enter Name
        Label(self, text = "Enter your Second name"
              ).grid(row = 1, column = 0, sticky  = W)
        self.enter_name = Entry(self)
        self.enter_name.grid(row = 1, column = 1, sticky  = W)
        
        #meal 1
        Label(self, text = "Fry potato with beautiful salt"
              ).grid(row = 2, column = 0, sticky  = W)
        self.price1 = BooleanVar()
        Checkbutton(self,
                    text = '50',
                    variable = self.price1,
                    command = self.update_text
                    ).grid(row = 2, column = 1, sticky  = W)
        
        #meal 2
        Label(self, text = "Barbecue"
              ).grid(row = 3, column = 0, sticky  = W)
        self.price2 = BooleanVar()
        Checkbutton(self,
                    text = '80',
                    variable = self.price2,
                    command = self.update_text
                    ).grid(row = 3, column = 1, sticky  = W)
        
        #meal 3
        Label(self, text = "Bavarian sausages"
                    ).grid(row = 4, column = 0, sticky  = W)
        self.price3 = BooleanVar()
        Checkbutton(self,
                    text = '125',
                    variable = self.price3,
                    command = self.update_text
                    ).grid(row = 4, column = 1, sticky  = W)
        
        #your order
        self.order = Text(self, width = 30, height = 4, wrap = WORD)
        self.order.grid(row = 7, column = 0, sticky  = W)

        #Add
        Label(self,
              text = "Add offering"
              ).grid(row = 5, column = 1, sticky  = W)

        #offers

        self.offer = StringVar()
        self.offer.set(None)
        Radiobutton(self,
                    text = 'Live music',
                    variable = self.offer,
                    value = "live music",
                    command = self.update_text
                    ).grid(row = 6, column = 0, sticky  = W)

        Radiobutton(self,
                    text = 'Hgirls',
                    variable = self.offer,
                    value = 'Hgirls',
                    command = self.update_text
                    ).grid(row = 6, column = 1, sticky  = W)              
        
        Radiobutton(self,
                    text = 'Hboys',
                    variable = self.offer,
                    value = 'Hboys',
                    command = self.update_text
                    ).grid(row = 6, column = 2, sticky  = W)        

        # summ
        self.summary = Text(self, width = 15, height = 1, wrap = WORD)
        self.summary.grid(row = 7, column = 1, sticky  = W)

    def update_text(self):
        '''view result'''
        contents = self.enter_name.get()
        tell = 'Mr(s) ' + str(contents) + ' you choose: ' 
        Sum = 'Sum is : '
        summ  = 30
        if self.price1.get():
            tell += 'Fry potato with beautiful salt, '
            summ += 50
        if self.price2.get():
            tell += 'Barbecue, '
            summ += 80
        if self.price3.get():
            tell += 'Bavarian sausages, '
            summ += 125

        add = self.offer.get()
        tell += add
        if add == 'Hboys' or add == 'Hgirls' or add == 'live music':
            summ += 500
        self.summary.delete(0.0, END)
        self.summary.insert(0.0, Sum + str(summ))        
        self.order.delete(0.0, END)
        self.order.insert(0.0, tell)

root = Tk()
root.title('MENU')
root.geometry('500x300')
app = Application(root)
root.mainloop()
            
