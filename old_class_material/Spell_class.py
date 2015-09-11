class Spell(object):
    def __init__(self, incantation, name):
        self.name = name
        self.incantation = incantation
        
    def __str__(self):
        return self.name + ' ' + self.incantation + '\n' + self.getDescription()
        
    def getDescription(self):
        return 'No description'
        # return 'This charm summons an object to the caster, potentially over a significant distance.'
        
    def execute(self):
        print self.incantation
        
class Accio(Spell):
    def __init__(self):
        Spell.__init__(self, 'Accio', 'Summoning Charm')
        
class Confundo(Spell):
    def __init__(self):
        Spell.__init__(self, 'Confundo', 'Confundus Charm')
        
    def getDescription(self):
        return 'Causes the vitim to become confused and befuddled'
        
def studySpell(spell):
    print spell
        
spell = Accio() 
spell.execute() # Accio
studySpell(spell) # Accio \n
studySpell(Confundo()) #Confundo, COndundus Charme
