import random

class Family:
    def __init__(self, last_name):
        self.last_name = last_name
        # example list of members
        self._members = []
        
   # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return random.randint(0, 99999999) 

    def add_member(self, member):
        new_member=member
        new_member["id"]=self._generateId()
        while True:
            print(new_member)
            if not any(member["id"] == new_member["id"] for member in self._members):
                break
            new_member["id"]=self._generateId()
        self._members.append(member)
        
        ## you have to implement this method
        ## append the member to the list of _members

    def delete_member(self, id):
        self._members=list(filter(lambda member : member["id"] != id,self._members))
        pass
        ## you have to implement this method
        ## loop the list and delete the member with the given id

    def update_member(self, id, member):
        ## you have to implement this method
        ## loop the list and replace the member with the given id
        for existing_member in self._members:
            if existing_member["id"]==id:
                member["id"]=id
                existing_member=member
    
    def get_member(self, id):
        for existing_member in self._members:
            if existing_member["id"]==id:
                return existing_member
        ## you have to implement this method
        ## loop all the members and return the one with the given id

    def get_all_members(self):
        return self._members