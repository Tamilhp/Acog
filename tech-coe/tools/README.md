# Tools for the COE's

These are the tools we are going to use to build the COE website. Here are the programs:

1. Tool to pull the information together:
   1. It generates the following:
      1. One JSON file for all the projects, that contains metadata along with the information from README.md
      2. One folder for project with
         1. the same information as above
         2. README.md in the same page
         3. docs folder
   2. Now, 11ty does the following
      1. Front page -- just static page from this folder.
      2. All the projects, from the JSON file.
      3. List of all the projects in a separate file.
      4. The menu will have:
         1. Projects -- all the company projects
         2. best practices
         3. blogs
         4. people
         5. open tasks
         6. gists
   3. Generate the website with the info.

