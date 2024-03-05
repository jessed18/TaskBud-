#This code defines a "Task" box where we can store a task's name, priority, and estimated time 
#The '_init_' function sets up the box with these compartments, filling them with the given information when a new task is created 
class Task:
    def __init__(self, name, priority, estimated_time):
        self.name = name
        self.priority = priority
        self.estimated_time = estimated_time

#takes a list of tasks as input and creates a schedule for doing them 
def generate_schedule(tasks):
    #sorts the taks based on two criteria: priority and estimated time
    #'key' parameter specifies how to sort the tasks 
    sorted_tasks = sorted(tasks, key=lambda x: (x.priority, x.estimated_time), reverse=True)
    #initalizes an empty list called 'schedule' to hole the tasks that fit into the day's schedule 
    schedule = []
    #sets the starting time of schedule to 0
    current_time = 0
    #loops goes through each tasks in the sorted list of tasks 
    for task in sorted_tasks:
        #checks if there's time in the day to do the current task
        #adds the estimated time of the task to the current time and compares it with 24
        if current_time + task.estimated_time <= 24:  # Assuming a 24-hour schedule
            schedule.append((task.name, current_time, current_time + task.estimated_time))
            #updates the current time by adding the estimated time of task that was just scheduled 
            current_time += task.estimated_time          
    #returns schedule of tasks to do 
    return schedule

#line starts a function called 'get_user_input'
def get_user_input():
    #line creates an empty list called 'tasks'
    tasks = []
    #this line starts a loop that continues forver 
    while True:
        #line asks the user for a task name 
        name = input("Enter task name (or 'done' to finish): ")
        #if the user types 'done' it stops the loop 
        if name.lower() == 'done':
            break
        #line asks the user for the task's priroity 
        priority = int(input("Enter priority level (1-10): "))
        #line asks the user for the estimated time to complete the task 
        estimated_time = float(input("Enter estimated time (hours): "))
        #adds the task to the list of tasks 
        tasks.append(Task(name, priority, estimated_time))
    #it gives back the list of tasks to whoever called the function 
    return tasks

#checks if the script is run directly 
if __name__ == "__main__":
    #gets tasks from the user 
    tasks = get_user_input()
    #makes a schedule for the tasks 
    schedule = generate_schedule(tasks)
    #prints a message about the schedule 
    print("\nGenerated Schedule:")
    #goes through each task in the schedule 
    for i, task in enumerate(schedule, 1):
        #prints details of each task 
        print(f"{i}. Task: {task[0]}, Start Time: {task[1]}:00, End Time: {task[2]}:00")
