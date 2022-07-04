import random
from game.shared.point import Point

class Elements:
    """contains the set of all objects on the screen

    Attributes:
       _objects: this a list of the objects { key: group_name, value: a list of objetos }
                 the objects can be, player, gem and rock
    """

    def __init__(self):
        """Constructs ."""
        self._objects = {}
        
    def add_object(self, group, object):
        """Adds an object to the given group.
        
        Args:
            group (string): The name of the group.
            object (ObjectInBoard): The actor to add.
        """
        if not group in self._objects.keys():
            self._objects[group] = []
            
        if not object in self._objects[group]:
            self._objects[group].append(object)

    def get_objects(self, group):
        """Gets the objects in the given group.
        
        Args:
            group (string): The name of the group.

        Returns:
            List: The objects in the group.
        """
        results = []
        if group in self._objects.keys():
            results = self._objects[group].copy()
        return results
    
    def get_all_objects(self):
        """Gets all of the objects in the dictionary of the elements.
        
        Returns:
            List: All of the objets in the elements.
        """
        results = []
        for group in self._objects:
            results.extend(self._objects[group])
        return results

    def get_first_object(self, group):
        """Gets the first object in the given group.
        
        Args:
            group (string): The name of the group.
            
        Returns:
            List: The first object in the group.
        """
        result = None
        if group in self._objects.keys():
            result = self._objects[group][0]
        return result

    def remove_object(self, group, object):
        """Removes an object from the given group.
        
        Args:
            group (string): The name of the group.
            object (ObjectInBoard): The object to remove.
        """
        if group in self._objects:
            self._objects[group].remove(object)
    
    def change_positions(self, group):
        
        if group in self._objects.keys():
            list_objects = self._objects[group]
            for i in range (len(list_objects)): 
                    x = random.randint(1, 60 - 1)
                    y = random.randint(1, 40 - 1)
                    position = Point(x, y)
                    position = position.scale(60)
                    self._objects[group][i].set_position(position)
                
