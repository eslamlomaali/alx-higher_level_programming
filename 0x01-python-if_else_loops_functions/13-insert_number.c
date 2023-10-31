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
	listint_t *n1;
	listint_t *n3;
	listint_t *n2;

	n3 = *head;
	n1 = malloc(sizeof(listint_t));

	if (n1 == NULL)
		return (NULL);

	while (n3 != NULL)
	{
		if (n3->n > number)
			break;
		n2 = n3;
		n3 = n3->next;
	}

	n1->n = number;

	if (*head == NULL)
	{
		n1->next = NULL;
		*head = n1;
	}
	else
	{
		n1->next = n3;
		if (n3 == *head)
			*head = n1;
		else
			n2->next = n1;
	}

	return (n1);
}
