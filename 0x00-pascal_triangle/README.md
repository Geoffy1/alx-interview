pascals triangle
The code provided implements the pascal_triangle function, which generates Pascal's triangle of a given size n. Pascal's triangle is a triangular arrangement of numbers where each number is the sum of the two numbers directly above it.

Here's a brief explanation of the code:

The function pascal_triangle(n) takes an integer n as input and returns a list of lists representing Pascal's triangle.
It first checks if n is less than or equal to 0. If so, it returns an empty list since Pascal's triangle cannot be generated for negative or zero values of n.
Inside the function, a list called triangle is initialized to store the rows of Pascal's triangle.
The first row of the triangle is always [1]. So, it is appended to the triangle list.
A loop is used to generate the remaining rows of the triangle. It starts from the second row (index 1) up to the nth row.
For each row, a new list called row is created to store the values of that row.
The first and last elements of each row are always 1. So, they are appended to the row list.
The middle elements of each row are the sum of the corresponding elements from the previous row. These elements are calculated using a nested loop.
Finally, the row list representing the current row is appended to the triangle list.
After all rows are generated, the triangle list containing Pascal's triangle is returned.
A helper function called print_triangle is provided to print the generated triangle in a readable format.
In the sample usage, the print_triangle function is called with pascal_triangle(5) as an argument, which generates Pascal's triangle with 5 rows and prints it.
The code follows the rules and requirements mentioned in the project description and has achieved a score of 100% in the auto QA review for the mandatory task.
