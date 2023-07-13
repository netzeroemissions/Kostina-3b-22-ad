class Housework:
    def __init__(self, file_name):
        self.file_name = file_name
        self.tasks = self.upload()

    def add_task(self, task):
        self.tasks.append(task)
        self.save()
    def del_task(self, task):
        self.tasks.remove(task)
        self.save()
    def show_task(self):
        print('Список задач: ')
        for task in self.tasks:
            print(task)
    def save(self):
        with open(self.file_name, 'w') as file:
            file.write('\n'.join(self.tasks))
    def upload(self):
        with open(self.file_name, 'r') as file:
            return file.read().splitlines()

housework = Housework('housework.txt')
housework.show_task()

housework.add_task('помыть посуду')
housework.add_task('помыть полы')
housework.add_task('приготовить ужин')
housework.add_task('приготовить обед')
housework.show_task()

housework.del_task('помыть посуду')
housework.show_task()