from random import choice, sample
from itertools import combinations
from math import ceil


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
        # !!!! IMPLEMENT ME

        # Add users
        first_names = ["Liam", "Noah", "William", "James", "Oliver", "Benjamin", "Elijah", 
            "Lucas", "Mason", "Logan", "Emma", "Olivia", "Ava", "Isabella", "Sophia", 
            "Charlotte", "Mia", "Amelia", "Harper", "Evelyn"]
        last_names = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", 
            "Davis", "Rodriguez", "Martinez", "Hernandez", "Lopez", "Gonzalez", "Wilson", 
            "Anderson", "Thomas", "Taylor", "Moore", "Jackson", "Martin"]

        for i in range(num_users):
            self.add_user(f'{choice(first_names)} {choice(last_names)}')

        # Create friendships
        new_friendships = sample(list(combinations(range(1, self.last_id+1), r=2)), k=ceil((avg_friendships*num_users)/2))
        for item in new_friendships:
            self.add_friendship(item[0], item[1])

    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME
        friend_stack = [(friend, [user_id, friend]) for friend in self.friendships[user_id]]

        while friend_stack:
            friend_id, path = friend_stack.pop(0)

            if friend_id is not user_id and friend_id not in visited:
                visited[friend_id] = path

                for secondary_friend in self.friendships[friend_id]:
                    if secondary_friend is not user_id and secondary_friend not in visited:
                        friend_stack.append( (secondary_friend, path + [secondary_friend]) )

        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(10, 2)
    print(sg.friendships)
    connections = sg.get_all_social_paths(1)
    print(connections)
