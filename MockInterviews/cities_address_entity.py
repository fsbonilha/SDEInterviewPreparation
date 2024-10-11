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

def pop_bigger_than_50(address: AddressEntity):
    result = []

    def dfs(address: AddressEntity):
        if address.isStreet() and address.getPopulation() > 50:
            result.append(address)
            return

        for child in address.getChildren():
            dfs(child)
    return result
