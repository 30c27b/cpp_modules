#include "ClapTrap.hpp"
#include "ScavTrap.hpp"

int main(void)
{
	std::cout << " == Testing ClapTrap ==" << std::endl;

	{
		ClapTrap steve("Steve");
		steve.attack("Joe");
		steve.takeDamage(9);
		steve.takeDamage(2);
		steve.beRepaired(6);
		steve.beRepaired(1);

		ClapTrap steve2;
		steve2 = steve;
		steve2.attack("Joe2");
		steve2.takeDamage(1);

		ClapTrap steve3(steve2);
		steve2.attack("Joe3");
		steve3.takeDamage(3);
	}


	std::cout << " == Testing ScavTrap ==" << std::endl;

	{
		ScavTrap tom("Tom");

		tom.attack("Tony");
		tom.takeDamage(4);
		tom.takeDamage(9);
		tom.beRepaired(50);
		tom.guardGate();
	}
	return 0;
}
