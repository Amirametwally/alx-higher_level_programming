#include <stdio.h>
#include <Python.h>
/**
 * print_python_list_info - prints  basic of Python lists
 * @p: pointer to PyObject
 *
 * Return: void
 */
void print_python_list_info(PyObject *p)
{
	Py_ssize_t l_size, l_allocated, j;
	PyObject *item;

	l_size = Pylist_Size(p);
	l_allocated = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %zd\n", l_size);
	printf("[*] Allocated = %zd\n", l_allocated);

	for (j = 0; j < l_size; j++)
	{
		printf("Element %zd: ", j);

		item = PyList_GetItem(p, j);
		printf("%s\n", Py_TYPE(item)->tp_name);
	}
}
