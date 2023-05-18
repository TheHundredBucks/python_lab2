"""
This program describes the DNS domain names represented in classes.
The parent class contains the data regarding the registered part name and the domain's
registration period. It is natural that the parent class has these values as any domain have them.
.com domains are belong to the class of Generic Top Leve Domains (as well as .net, .biz, .education and so on).
.uk domains are considered as a Country Code domain names for United Kingdom
"""

class Domain:
    def __init__(self, registered_part, registration_period):
        self.registered_part = registered_part
        self.registration_period = registration_period

    def __repr__(self):
        return f'{self.__class__.__name__}()'
    
    def add_years(self):
        self.registration_period += 1
        
    def registry_info(self):
        print(f"This TLD is operated by {self.Registry}\n")
        
class CountryCodeTld(Domain):
    pass

class GenericTld(Domain):
    pass
    
class DotCom(GenericTld):

    Registry = "Verisign Inc."
    
    def __init__(self, registered_part, registration_period):
        super().__init__(registered_part, registration_period)
        print(f'{registered_part}.com')
        
    def __repr__(self):
        return f'{self.__class__.__name__}()'
    
    def info(self):
        return print(f"""
    The domain {self.registered_part}.com 
    is registered for {self.registration_period} years\n""")

class DotUk(CountryCodeTld):

    Registry = "Nominet Ltd."
    
    def __init__(self, legaltype, registered_part, registration_period):
        super().__init__(registered_part, registration_period)
        self.legaltype = legaltype
        print(f'{registered_part}.uk')
        
    def __repr__(self):
        return f'{self.__class__.__name__}()'

    def info(self):
        return print(f"""
    The domain {self.registered_part}.uk 
    is registered for {self.registration_period} years 
    with a legal type of 
        {self.legaltype}\n""")

def main():
    myuk = DotUk("UK Individual", "myuk", 5)
    bestdomain = DotCom("bestdomain", 3)

    myuk.info()
    myuk.registry_info()
    print("Let`s add one more year:")
    myuk.add_years()
    myuk.info()

    bestdomain.info()
    bestdomain.registry_info()