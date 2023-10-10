#ifndef PYTHON_H
#define PYTHON_H

#include <stdio.h>



#include <assert.h>               // assert()
#include <inttypes.h>             // uintptr_t
#include <limits.h>               // INT_MAX
#include <math.h>                 // HUGE_VAL
#include <stdarg.h>
typedef struct _object {
    _PyObject_HEAD_EXTRA
    Py_ssize_t ob_refcnt;
    struct _typeobject *ob_type;
} PyObject;

#endif 
