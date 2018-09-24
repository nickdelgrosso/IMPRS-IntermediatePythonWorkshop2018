import inspect
import random

"""All Q classes contain class variables that are executed and inspected in the game, guaranteeing that the code runs
and that all answers are correct.  Important is that both Q.a and Q.b exist--they are hardcoded to be the
compared variables!"""

class Q1:
    a = [1, 2, 3]
    b = a


class Q2:
    a = 50.23
    b = 50.23


class Q3:
    a = [1, 2, 3]
    b = a[0]


class Q4:
    a = [1, 2, 3]
    b = a
    b[0] = 10

class Q5:
    a = 1
    b = 2

class Q6:
    a = 'hello'
    b = 'goodbye'

class Q7:
    a = (1, 2)
    b = a
    a = a + (3, 4)

class Q8:
    a = ['yes', 'no']
    b = a
    a.append('maybe')

class Q9:
    a = ['yes', 'no']
    b = a
    b.append('perhaps')

class Q10:
    a = 51.2
    b = a
    a += 10

class Q11:
    a = 3
    b = 4
    b = a

class Q12:
    a = {'ctrl': 1, 'exp': 2}
    b = a
    b['exp'] = 4

class Q13:
    a = {'ctrl': 1, 'exp': 2}
    b = a
    b['new'] = 4

class Q14:
    a = {'ctrl': 1, 'exp': 2}
    b = a
    a.update([('exp', 4)])

class Q15:
    a = {'ctrl': 1, 'exp': 2}
    b = a
    b.pop('ctrl')

class Q16:
    a = ['dog', 'rat', 'cat']
    b = a[:]

class Q17:
    a = {'ctrl': 1, 'exp': 2}
    b = a['ctrl']

class Q18:
    a = {'ctrl': 1, 'exp': 2}
    b = a['ctrl']
    a = a['ctrl']

class Q19:
    a = ['dog', 'rat', 'cat']
    b = list(a)

class Q20:
    a = ['dog', 'rat', 'cat']
    b = ['dog', 'rat', 'cat']

class Q22:
    a = ('dog', 'rat', 'cat')
    b = a

class Q23:
    a = ('dog', 'rat', 'cat')
    b = ('dog', 'rat', 'cat')
    a += ('fish', 'mouse')

class Q24:
    a = 1022
    b = a
    a += 1

class Q25:
    a = 1022
    b = a
    b += 1

class Q26:
    c = ['red', 'blue', 'green']
    a = c[0]
    b = c[0]

class Q27:
    c = ['red', 'blue', 'green']
    a = c[0]
    c.append('yellow')
    b = c[0]

class Q28:
    c = ('red', 'blue', 'green')
    a = c[1]
    c += ('yellow', 'orange')
    b = c[1]

class Q29:
    a = ['red', 'blue', 'green']
    b = a
    a = a.append('yellow')

class Q30:
    a = {0: 1, 2: 3, 4: 5}
    b = a
    b[2] = 200

class Q31:
    a = {0: 1, 2: 3, 4: 5}
    b = {0: 1, 2: 3, 4: 5}

class Q32:
    a = 3 if True else 1
    b = a

class Q33:
    a = [1, 2, 3]
    c = [5, 6, a, 7]
    b = c[-1]

class Q34:
    a = [1, 2, 3]
    c = [5, 6, a, 7]
    b = c[2]

class Q35:
    a = [1, 2, 3]
    c = [5, 6, a, 7]
    b = c[-2]

class Q36:
    a = 3
    b = 40 if False else a

class Q37:
    a = 3
    b = 40 if [False, False] else a

class Q38:
    a = 3
    b = 40 if 6 > 3 else a

class Q39:
    a = 3
    b = a if -1 else 40

class Q40:
    a = 3
    b = a if False else 40

class Q41:
    a = 3
    b = a if a else -a

class Q42:
    a = 3
    b = a if [a, a] else True

class Q43:
    a = 3
    b = a if a else -a

class Q44:
    c = list(range(6))
    a = c[-2]
    b = c[4]

class Q45:
    c = list(range(6))
    a = c[-2]
    b = c[2]

class Q46:
    c = list(range(6))
    a = c[:3][1]
    b = c[1]

class Q47:
    c = list(range(9))
    a = c[4:]
    b = c[-5:]

class Q48:
    c = 10
    a = [c]
    b = [c]

class Q49:
    a = [5, 6, 7]
    b = a[:]


questions = [var for name, var in sorted(locals().items()) if 'Q' in name[0] and name[1].isdigit()]


class Question:

    @classmethod
    def from_number(cls, value):
        return cls(questions[value])

    @classmethod
    def get_random(cls):
        return cls(random.choice(questions))

    def __init__(self, Q):
        self.Q = Q
        self.answered = False

    def __str__(self):
        lines = inspect.getsourcelines(self.Q)[0][1:]
        lines.append('-----------------\na is b')
        text = ''.join([line.lstrip() for line in lines])
        return text

    @property
    def correct_answer(self):
        return self.Q.a is self.Q.b
