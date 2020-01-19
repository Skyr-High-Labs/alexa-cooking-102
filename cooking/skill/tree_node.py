import scheduler
import constants

class TreeNode:
        def __init__(self, duration, childcount, children, annoying, description , dropoff = 0.1):
            self.todo = childcount
            self.children = children
            self.annoying = annoying
            self.duration = duration if annoying else -1
            self.restars = 0
            self.description = description
            self.dropoff = dropoff
            self.parents = []
            self.children_ready = {key: False for child in children}

        def set_parent(self, parent):
            self.parents.append(parent)

        def get_description(self):
            return self.description

        def start(self, time_now):
            if self.annoying:
                scheduler.add_timer(time_now+self.duration, self)

        def restart(self, time_now):
            self.restars += 1
            scheduler.add_timer([time_now+max(self.duration*(self.dropoff**self.restars), constants.minduration)])

        def complete_self(self):
            for parent in self.parents:
                parent.complete_child(self)

        def complete_child(self, child):
            self.children_ready[child] = True
            self.todo-=1
            if self.todo == 0:
                scheduler.activate_node(this)
