# White paper
Introduction: The transition from SQL Server Authentication (SSA) to OAuth for our S360 item required changes in our legacy tabular models. These models used SQL queries in import tables, which are now required to be changed to M queries to implement OAuth authentication. This white paper discusses the challenges faced during this migration and presents a Python script as a solution to automate the conversion process.
Background: Tabular models are structured as BIM files containing various elements like data sources, measures, relationships, dimensions, queries, and roles in a nested JSON format. Converting the SQL queries to M queries manually within this nested JSON structure is laborious and prone to errors.
Solution: To address this issue, we developed a Python script that utilizes JSON libraries to parse the BIM files and employs an intelligent iterator to locate and modify legacy SQL queries to M queries automatically. The script operates in two phases: Phase-1 creates M queries for all tables, and Phase-2 replaces old elements with new M query elements while eliminating unnecessary ones. The result is a BIM file compliant with OAuth authentication.
Benefits: Using our Python script eliminates the need for manual intervention, significantly reducing the chances of errors. The script has been successfully employed to migrate all our legacy tabular models, ensuring its reliability and effectiveness. In a large model with 64 tables, the manual migration process would take approximately 7 days and with 7 such models it can go up to 20-30 days. However, with our script, this task can be completed in a matter of seconds, resulting in a considerable reduction in time and effort.
Conclusion: Our customized Python script proved to be a valuable solution for our migration needs. Furthermore, it can be further refined to cater to more generic use cases. This script holds the potential to serve as a migration tool for other customers, both internal and external, providing them with a seamless transition from SQL Server Authentication to OAuth for their tabular models. As we continue to enhance its capabilities, the script can offer immense value to the product team and our broader user base.


# how to use
Give the bim file path in the script and the datasourceName
if you are using multiple data sources run the script 1 by one for each of them.
the script will do a in-place modification of the Bim file which will be M compatible

# Please note
In some cases wherever we have unicode characters in the query the script might add a extra space like "S E L E C T * F R O M <>" in such cases you can just copy that part in a notepad and do a find replace of whitespace.

# Open and parse the Bim file
file = <Bim FIle Path>
datasourceName = <Give your datasource Name which will be used in the Let - in expression>
