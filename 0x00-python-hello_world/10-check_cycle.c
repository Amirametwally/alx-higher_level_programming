#include "lists.h"

/**
 * check_cycle - function in C that checks if a singly
 * linked list has a cycle in it.
 * @list: struct
 *
 * Return: 1 or 0
 */

int check_cycle(listint_t *list)
{
	listint_t *fast = list;
	listint_t *slow = list;

	if (!list)
		return (0);

	while (fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;

		if (slow == fast)
			return (1);
	}

	return (0);
}
