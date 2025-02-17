#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>

int more_or_less(int a, int b)
{
    int	result;

    result = 0;
    if (!a || !b)
	{
		write(1, "Necesita numeros\n", 17);
		return (result);
	}
	result = (a + b);
	return (result);
}

int multipl(int a, int b)
{
	int	result = 0;
	if (!a || !b)
	{
		write(1, "Necesito números\n", 18);
		return (result);
	}
	result = a * b;
	return (result);
}
