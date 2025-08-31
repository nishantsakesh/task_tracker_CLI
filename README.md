🚀 My Task Tracker CLI 🚀
Hello, developers! 👋

This is a simple, yet incredibly useful, Command-Line Interface (CLI) task tracker app. You can easily manage your daily tasks, just like you would in a notebook. But in this case, all your tasks are stored safely in a JSON file.

It's built without any external libraries, using only native Python and filesystem modules. So, let's see how it works!

🧐 Features: What's in It?
This little app has some big, useful features, such as:

Add a Task: Add new tasks. Just write the description, and you're good to go!

Update or Delete: If you need to change a task or it's no longer necessary, you can modify or remove it by its ID.

Change Status: You can mark any task as in-progress or done.

View Lists: See all your tasks at once, or filter them by status (like todo, in-progress, or done).

🛠️ How to Use It?
Running this project is incredibly easy. First, you must have Python 3 installed.

1. Project Setup
First, download or clone this code and navigate to the project directory in your terminal:

cd task-tracker-cli-project


2. Run the Commands
Now you can run the script using task-cli.py (or whatever you named it). All the commands will run in this way:

To Add a Task:

python task_cli.py add "Buy groceries for the week"
# Output: Task added successfully (ID: 1)



To View All Tasks:

python task_cli.py list



To View Tasks by Status:

python task_cli.py list in-progress
# Or
python task_cli.py list done



To Update a Task:

python task_cli.py update 1 "Buy groceries and cook dinner"
# Output: Task 1 updated successfully.



To Mark a Task as in-progress:

python task_cli.py mark-in-progress 1
# Output: Task 1 marked as in-progress successfully.



To Mark a Task as done:

python task_cli.py mark-done 1
# Output: Task 1 marked as done successfully.



To Delete a Task:

python task_cli.py delete 1
# Output: Task 1 deleted successfully.



📝 Task Properties: The Inside Scoop
Every task is a JSON object with the following properties:

id: A unique number that identifies each task.

description: A short description of the task.

status: The current state of the task - todo, in-progress, or done.

createdAt: When the task was created.

updatedAt: When the task was last changed.


project link : https://github.com/nishantsakesh/task_tracker_CLI
project url : https://roadmap.sh/projects/task-tracker