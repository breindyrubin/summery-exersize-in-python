class Father(object):
    father_name = ''
    father_age = None

    def __init__(self, father_name, father_age):
        self.father_name = father_name
        self.father_age = father_age

    def get_father_name(self):
        return self.father_name

    def get_father_age(self):
        return self.father_age

    def set_father_age(self, age):
        self.father_age = age

    def set_father_name(self, name):
        self.father_name = name


class Mother(object):
    mother_name = ''
    mother_age = None

    def __init__(self, mother_name, mother_age):
        self.mother_name = mother_name
        self.mother_age = mother_age

    def get_mother_name(self):
        return self.mother_name

    def get_mother_age(self):
        return self.mother_age

    def set_mother_age(self, age):
        self.mother_age = age

    def set_mother_name(self, name):
        self.mother_name = name


class Child(Father, Mother):
    child_name = ''
    child_age = None
    father: Father
    mother: Mother

    def __init__(self, child_name, child_age, father, mother):
        self.child_name = child_name
        self.child_age = child_age
        for k,v in father.items():
            self.set_father(k,v)
        for k,v in mother.items():
            self.set_mother(k,v)

    def get_child_name(self):
        return self.child_name

    def get_child_age(self):
        return self.child_age

    def set_child_age(self, age):
        self.child_age = age

    def set_child_name(self, name):
        self.child_name = name

    def set_father(self, name, age):
        super(Child, self).set_father_name(name)
        super(Child, self).set_father_age(age)

    def set_mother(self, name, age):
        super(Child, self).set_mother_name(name)
        super(Child, self).set_mother_age(age)

    def set_parents(self, father_details, mother_details):
        self.set_father(father_details.name, father_details.age)
        self.set_mother(mother_details.name, mother_details.age)


class Family(Child):
    parents = {}
    children = {}
    last_name = ''

    def __init__(self, parents, children, last_name=''):
        self.parents = parents
        for k, v in children.items():
            self.add_child(k, v)
        self.last_name = last_name

    def add_child(self, child_name, child_age):
        c = Child(child_name, child_age, self.parents['father'], self.parents['mother'])
        self.children[child_name]=child_age

    def get_children(self):
        return self.children

    def get_child(self, i):
        return self.children[i]

    def get_parents_names(self):
        return self.parents['father'], self.parents['mother']


def main():
    father_name = input('enter fathers name: ')
    father_age = input('enter fathers age: ')
    mother_name = input('enter mothers name: ')
    mother_age = input('enter mothers age: ')
    last_name = input('enter last name(optional): ')
    num_of_children = int(input('enter number of children: '))

    count = 1
    children = {}
    while count <= num_of_children:
        child_name = input('enter child name: ')
        child_age = input('enter child age: ')
        children[child_name] = child_age
        count = count + 1

    father_details = {'name': father_name, 'age': father_age}
    mother_details = {'name': mother_name, 'age': mother_age}
    parents = {'father': father_details, 'mother': mother_details}

    f = Family(parents, children, last_name)

    print('what a beautiful family!')
    parents_info=f.get_parents_names()
    print(f'father: {parents_info[0]}, mother: {parents_info[1]}')
    print('children: ',f.get_children())


if __name__ == '__main__':
    main()
