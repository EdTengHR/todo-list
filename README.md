## Instructions for building and running the app
To build, run docker-compose build --pull
To run, use docker-compose up

## Database Schema
The todo database is simple, and is a list of items, each having the following schema:
```
{
    "id": (int) A unique identifier for the current todo item,
    "todo": (string) The description of the todo item,
    "marked": (boolean) A boolean describing if the todo item has been marked as complete
}
```

## Endpoints

### Listing all todos
To list all todos in the list, open Command Prompt, and run:
``` curl "http://localhost:5000/list" ```

### Adding a todo item
To add an item to the todo list, run:
``` curl "http://localhost:5000/add?id=1&todo=todo+item+here" ```
* Where the id is the unique identifier of the todo item, and the todo query parameter describes the todo item

### Marking a todo item as complete
To mark an item as complete, run:
``` curl "http://localhost:5000/mark-complete?id=1" ```
* After running, the todo item with the corresponding identifier in 'id' will have its marked parameter become true

### Deleting a todo item
To delete an item, run:
``` curl "http://localhost:5000/delete?id=1" ```
* The todo item with the identifier of 1 will be deleted from the list