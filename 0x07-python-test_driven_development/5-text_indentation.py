#!/usr/bin/python3
"""function that prints 2 new lines after  characters"""


def text_indentation(text):
    """Function that prints 2 new lines after  characters"""

    if not isinstance(text, str):
        raise TypeError("text must be a string")
    st = text[:]
    for i in ".?:":
        list_of_text = st.split(i)
        st = ""
        for j in list_of_text:
            j = j.strip("")
            st = j + i if st == "" else st + "\n\n" + j + i

    print(st[:-3], end="")
