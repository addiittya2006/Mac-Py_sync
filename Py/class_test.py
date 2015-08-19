#!/usr/local/bin/python3

#class Definiton
class Potato:
    def __init__(self, form="raw"):  #Constructor for the Class
        self.form=form
    
    def getForm(self):
        return self.form
    
    
def main():
    print("Potato form:")
    print(Potato().getForm(), end=' -> ')
    print(Potato("fries").getForm(), end=' -> ')
    print(Potato("chips").getForm())
    
if __name__ == '__main__':main()