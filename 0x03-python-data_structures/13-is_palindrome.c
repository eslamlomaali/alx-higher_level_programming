#include "lists.h"

/**
 * reverse - reverses a linked list
 * @head: pointer
 * Return: pointer
 */
void reverse(listint_t **head)
{
	listint_t *old = NULL;
	listint_t *pre = *head;
	listint_t *fut = NULL;

	while (pre)
	{
		fut = pre->fut;
		pre->fut = old;
		old = pre;
		pre = fut;
	}

	*head = old;
}

/**
 * is_palindrome - Write a function in C that checks if 
 * a singly linked list is a palindrome.
 * @head: double pointer
 *
 * Return: 1 if it is, 0 if not
 */
int is_palindrome(listint_t **head)
{
	listint_t *s = *head, *f = *head, *t = *head, *d = NULL;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	while (1)
	{
		f = f->next->next;
		if (!f)
		{
			d = s->next;
			break;
		}
		if (!f->next)
		{
			d = s->next->next;
			break;
		}
		s = s->next;
	}

	reverse(&d);

	while (d && t)
	{
		if (t->n == d->n)
		{
			d = d->next;
			t = t->next;
		}
		else
			return (0);
	}

	if (!d)
		return (1);

	return (0);
}
