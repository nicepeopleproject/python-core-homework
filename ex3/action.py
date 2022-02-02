class BaseAction:
    def __init__(self, name):
        self.name = name
        self.resultMap = {'PaperScissors': False, 'PaperRock': True, 'ScissorsPaper': True,
                          'ScissorsRock': False, 'RockPaper': False, 'RockScissors': True}

    def __repr__(self):
        return self.name

    def __lt__(self, other):
        return not self.resultMap[self.name + other.name]

    def __gt__(self, other):
        return self.resultMap[self.name + other.name]

    def __eq__(self, other):
        return self.name == other.name

    def __hash__(self):
        return hash(self.name)


class NothingAction(BaseAction):
    def __init__(self):
        super().__init__('Nothing')


class RockAction(BaseAction):
    def __init__(self):
        super().__init__('Rock')


class PaperAction(BaseAction):
    def __init__(self):
        super().__init__('Paper')


class ScissorsAction(BaseAction):
    def __init__(self):
        super().__init__('Scissors')

