class programmers():
    worknCom = 'microsoft'
    def __init__(self,programmer1Name,language, experience):
        self.programmer1Name = programmer1Name
        self.language  = language
        self.experience = experience
    
    def __str__(self):
        return f"programmer's name {self.programmer1Name}\nprogrammer language is {self.language}\nexperience of programmer is {self.experience}\n"
    
    def __init__(self,programmer2Name,language2,experience2):
        self.programmer2Name = programmer2Name
        self.language2 = language2
        self.experience2 =  experience2
    
    def __str__(self):
        return f"programmer's name {self.programmer2Name}\nprogrammer language is {self.language2}\nexperience of programmer is {self.experience2}\n"
    
p = programmers('dj',"python",3)
p2 = programmers('djop',"java",'none')
print(p)
print(p2)