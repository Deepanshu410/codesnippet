From Into: 

NumPy = Numerical Python. Widely used in fields that involve heavy data processing, such as data science, engineering, ai, ml.

Eg. \[1,2,3] \* 2 = \[1,2,3,1,2,3] -> Python list , np.array(\[1,2,3]) \* 2 = \[2,4,6] -> NumPy list

NumPy gives you the speed and the specialized tools you need to handle large scale numerical operations efficiently. 
Instead of dealing with words or slow lists, it takes massive grids of numbers and **does complex math** on all of them instantly.


Python topics needed: variables, data types, lists, loops, functions, indexing



###### **From Multi-Dimensional Arrays:** 

\- np.array('A') # **0d array**

\- np.array(\['A', 'B', 'C']) **# 1d array or vector**

\- np.array(\[\['A', 'B', 'C'], 

&#x20;                  \['D', 'E', 'F'], 

&#x20;                  \['G', 'H', 'I']]) **# 2d array or matrix**

\- np.array(\[\[\['A', 'B', 'C'], \['D', 'E', 'F'], \['G', 'H', 'I']],

&#x20;                  \[\['J', 'K', 'L'], \['M', 'N', 'O'], \['P', 'Q', 'R']],

&#x20;                  \[\['S', 'T', 'U'], \['V', 'W', 'X'], \['Y', 'Z', '\_']]]) # **3d array or tensor**

\- each of these lists, they **need a consistent number of elements with each other**

\- print(array1.ndim) # returns the **number of array dimensions** as an integer

\- print(array4.shape) # return a tuple of integers. It shows, **depth, the number of rows, and the number of coloumns**

\- print(array4\[0,0,0]) # in numpy, we have to access  chain indexing through something called, **mutli-dimensional indexing.**



###### **From Slicing:**

array\[start: end: step], **subscript operator**, end is exclusive and step is NOT exclusive

\- array\[::2] # **row selection**

\- array\[:, ::] # **column selection, array\[row, column]**



###### **From Arithmetic:**

\- Scalar (a linear algebra term, meaning a **single value**) arithmetic

\- Vertorized (linear algebra term, is a **single dimension**) math functions: with this we can **apply a function to an entire array without** writing a **loop**

\- Element-wise arithmetic; each operation is applied **element by element between two arrays**.

\- **Comparison** operators; using this we can create boolean arrays, filter data, and use element-wise comparisons.



###### **From Broadcasting:**

Broadcasting allows NumPy to perform operations on arrays with different shapes by virtually expanding dimensions so they match the larger arrays shape.

Rules: The dimensions have the same size. OR, one of the dimensions has a size of 1. 

\- # **conditions, either;**

print(array1.shape) # **(1,4)**

print(array2.shape) # **(4,1)**

\#OR, this

print(array3.shape) # **(4,4)**

print(array4.shape) # **(4,1)**



###### **From Aggregate Functions:** 

Aggregate function summarize data and typically return a single value.

\- np.**sum**, np.**mean**, np.**std**, np.**var** - **square root of std**, np.**min**, np.**argmin** - position of min, np.**argmax** - position of max, np.sum(array, axis=0) apply **to all column**, np.sum(array, axis=1) apply **to all rows**



###### **From Filtering:**

Filtering refers to the process of selecting elements from an array that match a given condition. 

\- use **'\&' instead of 'and'** because numpy uses C style arrays

\- boolean functions would flaten the list, break the 2d into 0d array. **To preserve the original shape**:

\- adults2 = **np.where**(ages>= 18, ages, 0) # **where(condition, argument(which is array), fill(replacing the filtered out values with))**

