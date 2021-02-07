Description:

Write an algorithm to determine if a given relation R is reflexive, symmetric, anti-symmetric, and transitive.
Your code should meet the following requirements, standards and tasks.
• Read the relations in the text file ”input.txt”.
• Let R be a relation on a set A where ∃a, b ∈ A,(a, b) ∈ R. Each relation R is represented with the lines
in the file:
1. The first line says how many relations in R.
2. The second line gives the elements of the set A.
3. The following lines give each relation in R.
• After determining each relation in input.txt whether it is reflexive, symmetric, anti-symmetric and transitive with your algorithm, write its result to the file which is called ”output.txt” with the following
format.
• output.txt:
1. Start a new line with ”n” which indicates a new relation.
2. The set of R
3. Reflexive: Yes or No, explain the reason if No (e.g. ”(a, a) is not found”).
4. Symmetric: Yes or No, explain the reason if No (e.g. ”(b, a) is not found whereas (a, b) is found.”)
5. Antisymmetric: Yes or No, explain the reason if No (e.g. ”(b, a) and (a, b) are found.”)
6. Transitive: Yes or No, explain the reason if No (e.g. ”(a, c) is not found whereas (a, b) and (b, c)
are found.”)
• An example of the output format is given in ”exampleoutput.txt”. The file has the result of the first
relation in ”input.txt”.
• When explaining why a property does not exist in the relation, one reason is enough to explain if there
are more. For example, in ”exampleoutput.txt”, the relation is not symmetric because (b, a) and (e, a)
are not found. Detecting one of them is enough to explain the reason.
• Bonus (20 points): If you can explain why a property exists in the relation, it brings you bonus of 20
points.
• Your code is responsible to provide exception and error handling. The input file may be given with a
wrong information, then your code must be prepared to detect them. For instance, ”The element b of the
relation (1, b) is not found in the set A = {1, 2, 3, 4}.”.
