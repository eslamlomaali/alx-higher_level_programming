#include <Python.h>
#include <object.h>
#include <listobject.h>
#include <bytesobject.h>
/**
 * print_python_bytes - Prints bytes info
 *
 * @p: Python Object
 * Return: void
 */
void print_python_bytes(PyObject *p)
{
	char *strr;
	long int cube, x, cut;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	cube = ((PyVarObject *)(p))->ob_size;
	strr = ((PyBytesObject *)p)->ob_sval;

	printf("  size: %ld\n", cube);
	printf("  trying string: %s\n", strr);

	if (cube >= 10)
		cut = 10;
	else
		cut = cube + 1;

	printf("  first %ld bytes:", cut);

	for (x = 0; x < cut; x++)
		if (strr[x] >= 0)
			printf(" %02x", strr[x]);
		else
			printf(" %02x", 256 + strr[x]);

	printf("\n");
}

/**
 * print_python_list - Prints list info
 *
 * @p: Python Object
 * Return: void
 */
void print_python_list(PyObject *p)
{
	long int cube, x;
	PyListObject *sqr;
	PyObject *opp;

	cube = ((PyVarObject *)(p))->ob_size;
	sqr = (PyListObject *)p;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", cube);
	printf("[*] Allocated = %ld\n", sqr->allocated);

	for (x = 0; x < cube; x++)
	{
		opp = ((PyListObject *)p)->ob_item[x];
		printf("Element %ld: %s\n", x, ((opp)->ob_type)->tp_name);
		if (PyBytes_Check(opp))
			print_python_bytes(opp);
	}
}
