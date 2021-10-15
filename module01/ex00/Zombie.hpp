#ifndef ZOMBIE_HPP
#define ZOMBIE_HPP

#include <string>
#include <iostream>
#include <unistd.h>

class Zombie
{
	private:
		std::string _name;

		Zombie();

	public:
		Zombie(std::string name);
		~Zombie();
		
		void announce(void) const;
};

#endif
