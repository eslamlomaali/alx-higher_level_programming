#include "lists.h"

/**
 * insert_node - Write a function in C that inserts a
 * number into a sorted singly linked list.
 * @head: A pointer
 * @number: The number
 * Return: Return: the address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *nn = *head, *nnn;

	nnn = malloc(sizeof(listint_t));
	if (nnn == NULL)
		return (NULL);
	nnn->n = number;

	if (nn == NULL || nn->n >= number)
	{
		nnn->next = nn;
		*head = nnn;
		return (nnn);
	}

	while (nn && nn->next && nn->next->n < number)
		nn = nn->next;

	nnn->next = nn->next;
	nn->next = nnn;

	return (nnn);
}
