class steveJobs:
    def __init__(self, name="Steve Jobs"):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    def apple1(self):
        print(f"I am {self._name}") 

class steveWozniak(steveJobs):  
    def apple2(self):
        print("I am Steve too.")  

obj = steveWozniak() 
obj.apple1()  
obj.apple2()  



class gnuxLinux:  
    def __init__(self, gnuxLinuxname): 
        self._gnuxLinuxname = gnuxLinuxname

    @property
    def gnuxLinuxname(self):
        return self._gnuxLinuxname

    @gnuxLinuxname.setter
    def gnuxLinuxname(self, value):
        self._gnuxLinuxname = value

class Arch(gnuxLinux):  
    def __init__(self, Archname, gnuxLinuxname): 
        super().__init__(gnuxLinuxname)  
        self._Archname = Archname

    @property
    def Archname(self):
        return self._Archname

    @Archname.setter
    def Archname(self, value):
        self._Archname = value

class Manjaro(Arch):  
    def __init__(self, Manjaroname, Archname, gnuxLinuxname): 
        super().__init__(Archname, gnuxLinuxname)  
        self._Manjaroname = Manjaroname

    @property
    def Manjaroname(self):
        return self._Manjaroname

    @Manjaroname.setter
    def Manjaroname(self, value):
        self._Manjaroname = value
    
    def print_name(self):  
        print('gnuxLinux name :', self.gnuxLinuxname)  
        print('Arch name :', self.Archname) 
        print('Son name :', self.Manjaroname)  

s1 = Manjaro('I talk to hardware', 'Archbtw', '"archBtw"') 
print(s1.gnuxLinuxname) 
s1.print_name()  



class Linux:  
    def __init__(self, kernel_name="Linux"):
        self._kernel_name = kernel_name

    @property
    def kernel_name(self):
        return self._kernel_name

    @kernel_name.setter
    def kernel_name(self, value):
        self._kernel_name = value

    def Linus(self): 
        print("This function is the kernel.") 

class Debian(Linux): 
    def __init__(self, debian_name="Debian", kernel_name="Linux"):
        super().__init__(kernel_name)
        self._debian_name = debian_name

    @property
    def debian_name(self):
        return self._debian_name

    @debian_name.setter
    def debian_name(self, value):
        self._debian_name = value

    def ianMurdock(self):  
        print("I am the boring child.") 

class Fedora(Linux): 
    def __init__(self, fedora_name="Fedora", kernel_name="Linux"):
        super().__init__(kernel_name)
        self._fedora_name = fedora_name

    @property
    def fedora_name(self):
        return self._fedora_name

    @fedora_name.setter
    def fedora_name(self, value):
        self._fedora_name = value

    def Redhat(self):
        print("I am the enterprise child.") 

object1 = Debian()  
object2 = Fedora() 
object1.Linus()  
object1.ianMurdock()  
object2.Linus()  
object2.Redhat()  