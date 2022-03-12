#!/usr/bin/env python3


class Spell:

    def __init__(self, incantation, name):
        self.name = name
        self.incantation = incantation

    def __str__(self):
        return self.name + ' ' + self.incantation + '\n' + self.get_description()

    def get_description(self):
        """
        return: a discription of the spell
        """
        return 'No description'

    def execute(self):
        """
        return: None
        prints self.incantation
        """
        print(f'{self.incantation}\n')


class Accio(Spell):

    def __init__(self):
        Spell.__init__(self, 'Accio', 'Summoning Charm')

    def __str__(self):
        return f'Summoning Charm Accio\n{self.get_description()}'

    def get_description(self):
        """
        return: a discription of the spell
        """
        return 'This charm summons an object to the caster, ' \
               'potentially over a significant distance.'


class Confundo(Spell):

    def __init__(self):
        Spell.__init__(self, 'Confundo', 'Confundus Charm')

    def get_description(self):
        """
        return: a discription of the spell
        """
        return 'Causes the victim to become confused and befuddled.'


def study_spell(spell):
    print(f'{spell}\n')


exemplar = Accio()
exemplar.execute()
study_spell(exemplar)
study_spell(Confundo())
