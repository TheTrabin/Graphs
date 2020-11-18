import random
import math
from util import Queue

class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}

        # Add users
        for i in range(num_users):
            self.add_user(f"User {i}")

        # Create friendships
        # generate all the possible friendships and put them in a list
        possible_friendships = []
        for user_id in self.users:
            for friend_id in range(user_id +1, self.last_id +1):
                possible_friendships.append((user_id, friend_id))
        # shuffle that list
        random.shuffle(possible_friendships)
        # create friendships using add friendship from the first N elements in that list
        for i in range(math.floor(num_users * avg_friendships / 2)):
            friendship = possible_friendships[i]
            self.add_friendship(friendship[0], friendship[1])

    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.


        Plan:
        Queue or Stack? Deque?
        Would have to traverse the main information
        Find connected edges from target user
        log all connected edges
        Take new user information
        log all new connected edges in the tree.

        Initialize Plan:

        Make a stack and a path.
        Initial user is the main entry in the stack.
        Pop users into the path.
        move down the list in the search.
        append found users that match criteria.


        """
        visited = {}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME
        line = Queue()
        line.enqueue(user_id)
        stack = [[user_id]]

        while len(stack) > 0:
            path = stack.pop(0)
            currNode = path[-1]

            if currNode not in visited:
                visited[currNode] = path

                for user in self.friendships[currNode]:
                    nPath = list(path)
                    nPath.append(user)
                    stack.append(nPath)

        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(10, 2)
    print(f"friendships:")
    print(sg.friendships)
    connections = sg.get_all_social_paths(1)
    print(f"Social pathings:")
    print(connections)
    print(f"100/10")
    sg.populate_graph(100,10)
    connections2 = sg.get_all_social_paths(1)
    print(f"friendships:{sg.friendships}")
    print(f"connections: {connections2}")
    sg.populate_graph(1000,5)
    connections3 = sg.get_all_social_paths(1)
    print(f"friendships:{sg.friendships}")
    print(f"connections: {connections3}")