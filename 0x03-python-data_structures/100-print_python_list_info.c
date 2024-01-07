#include <Python.h>
#include <stdio.h>

void print_python_list_info(PyObject *p)
{
	Py_ssize_t size, k;
	PyObject *element;

	size = PyList_Size(p);

	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

	for (k = 0; k < size; k++)
	{
		element = PyList_GetItem(p, k);
		printf("Element %ld: %s\n", k, Py_TYPE(element)->tp_name);
	}
}
