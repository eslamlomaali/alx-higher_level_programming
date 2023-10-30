#include "lists.h"

/**
 * check_cycle - Write a function in C that checks if a
 * singly linked list has a cycle in it.
 * @list: linked list
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *prev = list;
	listint_t *new = list;

	if (!list)
		return (0);

	while (prev && new && new->next)
	{
		prev = prev->next;
		new = new->next->next;
		if (prev == new)
			return (1);
	}

	return (0);
}
