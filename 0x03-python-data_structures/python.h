#ifndef PYTHON_H
#define PYTHON_H


typedef struct _object {
    _PyObject_HEAD_EXTRA
    Py_ssize_t ob_refcnt;
    struct _typeobject *ob_type;
} PyObject;

#endif 
