# Contact Tracing Program
This is an application that analyses a small dataset to determine how a virus is spreading based on contact tracing dataset 
to determine how a virus is spreading based on contact tracing data.

Below is a set of instructions that led to the creation of this program.

## Running the contact tracing program
There are two ways to run the program from the terminal depending on whether you want to provide the data file 
name on the command line or whether you want the user to be prompted for the file name:
### Entering a file name on the command line
On Windows, run the program in the terminal, specifying the data file name:
python contact.py DataSet0.txt

or on macos type:
python3 contact.py DataSet0.txt

The meaning of the terms on this line is:
1. python or python3 - The python interpreter. On macos this will be python3
and on Windows, this will be py or python.
2. contact.py - The name of the python program.
3. DataSet0.txt - Name of the data file.

### Prompting the user for a file name
To prompt the user for a file name, simply run the program in your editor (IDE) as you would normally.

## Getting Started
This contact tracing data is one-directional, 
meaning sick people who have tested positive for a fictitious zombie disease have reported the people with whom
they have had contact. We don’t have data for the reverse direction where a well person had contact with a sick 
individual. In order to work with the contact tracing data, you will need to load a data file storing contact tracing data
and create appropriate data structures such as a dictionary or a list. These data structures can be used to identify the 
relationship between the individuals in the data. 
The program will then print the information returned using print() commands in main().

### Data files
It is assumed that the data in the files given is correct. The data is stored in CSV (comma separated 
value) files. Each file ends with the .txt extension. Open the files in Visual Studio Code or in a text 
editor to see the contents.
Each line in the file will be of the form < SickPerson1 >, < Contact1 >, < Contact2 >, ..., < Contactn > 
< SickPerson1 >, < Contactn > are placeholders for specific people.  

Each line will always begin with exactly one person, followed by one or more other people. For example, lines in the 
file could be Jonathan, Alice, Bob or Carol, Alice
The names may include a mixture of upper and lowercase letters and may also include spaces. The end of a name is 
indicated by comma separator. In order to make the files easier to work with you can assume that there will not be 
any spaces immediately before or after any of the commas (only within the start and end of a name).

## 1. Check the file exists
Take a look at the following code in main():

// 1. Check that the file exists
 if not file_exists(filename):  
 print("File does not exist, ending program.")  
 sys.exit()

The python code sys.exit() will cause the program to terminate if the file cannot be opened and read. You should not 
change the code in main().
The function file_exists() takes the file name given as a parameter, and checks that the file exists. The first task 
is to complete function file_exists(). The function file_exists()must return True if the file exists and False if 
it does not. Hint: use the function isfile() from the python library os.path. 

## 2. Create a dictionary
Take a look at the following code in main():

// 2. Create contacts dictionary from the file contents  
contacts_dic = parse_file(filename)

Complete the function parse_file(). This function takes a file name as a parameter, reads the file line by line and 
creates a dictionary with the name of the sick person as the key and a list of contacts as the value. The function will 
return the dictionary. If a ValueError exception is generated when processing a line of the file, the program should 
print the message:  
"Error found in file, continuing."  
The program should continue if there is an error of this type and attempt to read the next line of the file. If there 
are no valid lines in the file then the function should return an empty dictionary. Ensure that the file is closed.

## 3. Print contact records
Take a look at the following code in main():

// Section 4. Print contact records  
// Add your code here

Print the names of the sick people with the list of people that they had contact with. For example, if the data 
file contains the line:  
Jonathan, Alice, Bob, Charles  
Your output should be:  
Jonathan had contact with Alice, Bob and Charles  

Check the format of the output expected for the files given. The output expected for each data file can be found 
in the corresponding file name with the word “out” in the name. For example: the output for DataSet1.txt is given in 
DataSet1-out.txt.   
Note that commas appear after all the contacts except the last two items where the word “and” must be used. You 
have been provided with module format_list.py which contains the function format_list(). Use the function 
format_list() to print the list as shown in the output.

The output expected for DataSet1.txt is:  
Contact Records:  
 Alice had contact with Bob, Carol, Darryl, Ettienne Fourth, Forbert Findlesworth II and Gordie  
 Bob had contact with Lammle  
 Carol had contact with Lammle  
 Darryl had contact with Lammle  
 Ettienne Fourth had contact with Lammle  
 Forbert Findlesworth II had contact with Job and Molly  
 Gordie had contact with Kirk  
 Hanes had contact with Bob, Carol, Ettienne Fourth and Forbert Findlesworth II  
 Illersley had contact with Darryl, Ettienne Fourth, Forbert Findlesworth II, Gordie, Job and Kirk  
 Job had contact with Lammle  
 Kirk had contact with Job  
 Molly had contact with Job and Kirk  

 ## 4. Identify possible patients zero
The input files consist of contact tracing records where we know everyone tested positive before constructing their 
contact record list, then we can track back the path of the likely infection to what we will call patient zero(s). One way 
to think about patient zero(s) is that they are people that are sick who do not appear in anyone else’s contact list. 
The program should list the patient zero(s) for the input data.   
The output for DataSet1.txt should be:  
Patient Zero(s): Bob, Farley and Larry  
Complete function find_patients_zero(). Do not change the function signature, this means that the 
parameters and the return type of function find_patients_zero() must remain the same. Add code to main()
to print the results. Use the function format_list() to print the list as shown in the sample output.

## 5. Identify potential zombies
A potential zombie is any person that might be infected (because they have been in contact with a sick individual) but 
who has not yet been conclusively determined to be sick. Remember that a sick person occurs as a first entry in each 
contact record in the data file so a potential zombie will occur in the list of a sick person, but not occur as a sick person
themselves. The output from your program should display all of the potential zombies with an appropriate heading. 
There should be no duplicates in this list.  
The output for DataSet1.txt should be:  
Potential Zombies: Philip and Sarai  
Complete function find_potential_zombies(). Do not change the function signature, this means that the 
parameters and the return type of function find_potential_zombies()must remain the same. Add code to 
main() to print the results. Use the function format_list() to print the list as shown in the output.

## 6. Identify people who are neither patients zero(s) nor potential zombies
The people that are neither patient zero(s) nor potential zombies are all of the individuals that occur in the data file 
but were not printed in Section 5: Identify possible patients zero or Section 6: Identify potential zombies. You must 
complete function find_not_zombie_nor_zero(). You can use the lists returned by the functions created for 
the previous two sections as arguments to function find_not_zombie_nor_zero(). The function should 
construct a list of names that only includes individuals who were not potential zombies and were not patient zero(s)
and return this list. Do not change the function signature of , find_not_zombie_nor_zero(). This means that 
the parameters and the return type of function find_not_zombie_nor_zero()must remain the same. 
Add code to main() to print the results. Use the function format_list() to print the list.   
The output for DataSet1.txt should be:  
Neither Patient Zero or Potential Zombie: Carol, Leanne, Mark, Paul, Will and Zach  

## 7. Identify the most viral people
The most viral people are the people who likely infected the greatest number of other people in the data set 
because they had the longest list of contacts. You must identify the most viral people by completing function
find_most_viral(). Do not change the function signature, this means that the parameters and the return type of 
function find_most_viral()must remain the same. Add code to main() to print the results. Use the function 
format_list() to print the list as shown in the output.  
The output for DataSet1.txt should be:  
Most Viral People: Bob  
DataSet1.txt has only one most viral person but other data sets may have several most viral individuals, all of whom 
infected the same amount of people. When that situation occurs, your program should display all of the most viral 
people.

## 8. Identify the most contacted person
The most contacted person is the member of the data set who has possibly been infected by (been in contact with) 
the most sick members of the data set. You must identify the most viral people by completing function
find_most_contacted(). Do not change the function signature, this means that the parameters and the return 
type of function find_most_contacted()must remain the same. Remember, there should be no duplicates in 
this list returned from the function. Add code to main() to print the results. Use the function format_list() to 
print the list as shown in the output.  
The output for DataSet1.txt should be:  
Most Contacted: Leanne and Mark  

## 9. Find the maximum distance from a potential zombie
The maximum distance from a potential zombie is the longest contact tracing path downwards in the data set from a 
sick person to a potential zombie. Using this definition, all potential zombies (people that are not yet confirmed to be 
sick) have maximum distance 0. Any person that only has contact with potential zombies has maximum distance 1. All other 
people in the data set have a maximum distance which is one more than the maximum distance of the person they’ve had 
contact with who has the largest maximum distance value.  
You can determine the maximum distances of all the people in the contact tracing data using the following algorithm:  

set the max distances of all people, including potential zombies, to 0  
set changed to true   
while something has changed   
set changed to false   
for each person, p1, in the dataset  
for each person, p2, that p1 had contact with  
if the max dist of p1 <= max dist of p2   
set the max dist of p1 to the max dist of p2 + 1  
set changed to true  

Implement the algorithm by completing function find_maximum_distance_from_zombie(). Do not change 
the function signature, this means that the parameters and the return type of function
find_maximum_distance_from_zombie() must remain the same. Add code to main() to print the results.   
The output for DataSet1.txt should be:  
Heights:  
 Bob: 4  
 Larry: 4  
 Carol: 3  
 Farley: 3  
 Will: 3  
 Mark: 2  
 Paul: 2  
 Leanne: 1  
 Zach: 1  
 Philip: 0  
 Sarai: 0  
Note: your output may not appear in the same order, this is acceptable.  

## 10. Identify the spreader zombies, regular zombies, and zombie predators.  
A spreader zombie is sick person that only has had contact with potential zombies. Display the spreader zombies 
under an appropriate heading. If there aren’t any spreader zombies then you should display the heading, 
followed by “(None)”. In DataSet1.txt, you will see that Leanne has had contact with Sarai and Zach has had contact 
with Philip. Both Sarai and Philip are both potential zombies and this means that Leanne and Zach are spreader 
zombies.   
A regular zombie is a sick person that has had contact with both potential zombies and people who are already sick. 
Display the regular zombies under an appropriate heading. If there aren’t any regular zombies then you should display 
the heading, followed by “(None)”. In DataSet1.txt, we can see that a regular zombie cannot be a spreader zombie so 
that excludes Leanne and Zach. Mark has had contact with both Philip and Zach; Philip is a potential zombie and Zach 
is a sick person so Mark is a regular zombie.   
A zombie predator is a person that only has contact with people who are sick. Display the zombie predators under an 
appropriate heading. If there aren’t any zombie predators then you should display the heading, followed by “(None)”.
In DataSet1.txt, zombie predators are Bob, Carol, Farley, Larry, Paul and Will have only had contact with sick people. 
They have not had contact with potential zombies.   
The output for spreader, regular, and predator zombies for DataSet1.txt are:    
 Spreader Zombies: Leanne and Zach  
 Regular Zombies: Mark  
 Zombie Predators: Bob, Carol, Farley, Larry, Paul and Will  




















