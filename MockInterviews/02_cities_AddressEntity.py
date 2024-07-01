"""
Given an initial AddressEntity that represents a country, find and return a list with all streets that have a population bigger than 50 people.

class AddressEntity {
    boolean isCountry();
	boolean isCity();
	boolean isNeighborhood();
	boolean isStreet();
	String getName();
	int getPopulation();
	List<AddressEntity> getChildren();
}

- Brazil
    - Rua 2
	- Belo Horizonte
		- Savassi
			- Rua 1
			- Rua 2
			- Rua 3
	- São Paulo
		- Itaim
			- Rua 1
			- Rua 2
			- Rua 5
	- Nanuque
		- Centro
			- Rua 1 
			- Rua 2
		- Feirinha
			- Rua 5
			- Avenida Brazil
			
input: AddressEntity -> Brazil, 50
       AddressEntity -> Brazil, startsWith(Avenida)
output: [AddressEntity(Rua1), AddressEntity(Rua2)]

"""

class PopulationBiggerThanCondition:
    int threshold
    
    def apply(address: AdressEntity):
        return address.getPopulation > threshold

class NameStartsWithCondition:
    str prefix
    
    def apply(address: AdressEntity):
        return address.getName().startsWith(prefix)

class orCondition:
    condition1, condition2
    
    def apply(address: AdressEntity):
        return condition1.apply(address) or condition2.apply(address)

class andCondition:
    condition1, condition2
    
    def apply(address: AdressEntity):
        return condition1.apply(address) and condition2.apply(address)

class Solution:
    def get_streets(self, address: AdressEntity, condition):
        result = []
        
        if address.isStreet():
            if condition.apply(address):
                result.append(address)
        else:
            for add in address.getChildren():
                new_streets = get_streets(add, condition)
                result = result + new_streets
        
        return result
        
Solution().get_streets(address, andCondition(PopulationBiggerThanCondition(50), NameStartsWithCondition("Avenida")))
Solution().get_streets(address, NameStartsWithCondition("Avenida"))
        
        
        
# -> Marketplace -> isEnabled
# -> UseCase -> isEnabled
# -> optIN -> isOptedIn
# ...

# filtros = []