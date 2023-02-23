class details:
    def __init__(self,id,name,sal):
        self.id=id
        self.name=name
        self.sal=sal
    def show(self):
        print("Name",self.name)
        print("id",self.id)
        print("sal",self.sal)

class Updatedetails(details):
    def __init__(self,id,name,sal,cert,awards):
        super().__init__(id,name,sal)
        self.cert=cert
        self.awards=awards
    def show111(self):
        super().show()
        print("Certification",self.cert)
        print("awards",self.awards)

obj=Updatedetails(101,'virat',100000,'A+','Padmashri')
obj.show111()