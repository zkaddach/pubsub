# Improvements 

Here are some possible improvements for the project:
- Generate documentation using tools like Sphinx.
- Make it more resilient : 
    - Cache actions when either topics, publishers or subscribers are down
    - Class attributes are shared by child objects, we should check that it is okay
    - Manage better errors such as topics that doesn't exist yet
- Add tests in respect of the FIRST method (there are actually very few tests implemented just as examples)
- Make this messaging system a library 
  
