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
	listint_t *eslam;
	listint_t *alaa;
	listint_t *esraa;

	alaa = *head;
	eslam = malloc(sizeof(listint_t));

	if (eslam == NULL)
		return (NULL);

	while (alaa != NULL)
	{
		if (alaa->n > number)
			break;
		esraa = alaa;
		alaa = alaa->next;
	}

	eslam->n = number;

	if (*head == NULL)
	{
		eslam->next = NULL;
		*head = eslam;
	}
	else
	{
		eslam->next = alaa;
		if (alaa == *head)
			*head = eslam;
		else
			esraa->next = eslam;
	}

	return (eslam);
}
