#include "lists.h"
#include <stdlib.h>

/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: pointer to head of list
 * @number: number to insert
 * Return: address of new node or NULL if failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node, *current_node;

	if (!head)
		return (NULL);

	new_node = malloc(sizeof(listint_t));
	if (!new_node)
		return (NULL);

	new_node->n = number;

	if (!*head)
	{
		new_node->next = NULL;
		*head = new_node;
		return (new_node);
	}

	current_node = *head;
	if (current_node->n > number)
	{
		new_node->next = current_node;
		*head = new_node;
		return (new_node);
	}

	while (current_node->next)
	{
		if (current_node->next->n > number)
		{
			new_node->next = current_node->next;
			current_node->next = new_node;
			return (new_node);
		}
		current_node = current_node->next;
	}

	new_node->next = NULL;
	current_node->next = new_node;
	return (new_node);
}
