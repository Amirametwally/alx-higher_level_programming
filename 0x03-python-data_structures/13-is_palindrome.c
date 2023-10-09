#include "lists.h"

/**
 * reverse_list - Reverses a linked list
 * @head: Double pointer to the head
 * Return: Pointer to the new head
 */
listint_t *reverse_list(listint_t **head)
{
	listint_t *prev = NULL;
	listint_t *current = *head;
	listint_t *next = NULL;

	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}

	*head = prev;
	return (*head);
}

/**
 * compare_lists - Compares two linked lists
 * @list1: first Pointer
 * @list2: second Pointer
 *
 * Return: 1, 0
 */
int compare_lists(listint_t *list1, listint_t *list2)
{
	while (list1 != NULL && list2 != NULL)
	{
		if (list1->n != list2->n)
			return (0);

		list1 = list1->next;
		list2 = list2->next;
	}

	return (list1 == NULL && list2 == NULL);
}

/**
 * is_palindrome - Checks if a linked list is a palindrome
 * @head: Double pointer to the head
 *
 * Return: 1 , 0
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow = *head;
	listint_t *fast = *head;
	listint_t *previous_slow = *head;
	listint_t *middle = NULL;
	listint_t *second_half = NULL;
	int palindrome = 1;

	if (*head == NULL || (*head)->next == NULL)
		return (palindrome);

	while (fast != NULL && fast->next != NULL)
	{
		fast = fast->next->next;
		previous_slow = slow;
		slow = slow->next;
	}

	if (fast != NULL)
	{
		middle = slow;
		slow = slow->next;
	}
	second_half = slow;
	previous_slow->next = NULL;

	reverse_list(&second_half);

	palindrome = compare_lists(*head, second_half);

	reverse_list(&second_half);

	if (middle != NULL)
	{
		previous_slow->next = middle;
		middle->next = second_half;
	}
	else
		previous_slow->next = second_half;
	return (palindrome);
}
