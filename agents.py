def planner_agent(topic):
    return f"""
Day 1: Learn basics of {topic}

Day 2: Practice problems on {topic}

Day 3: Revise and take a mock test
"""


def quiz_agent(topic):
    return f"""
1. What is {topic}?

A) Option A
B) Option B
C) Option C
D) Option D
"""


def motivation_agent():
    return "Keep learning every day. Small progress becomes big success!"
def quiz_agent(topic):
    return f"""
1. What is {topic}?

A) Option A
B) Option B
C) Option C
D) Option D

2. Why is {topic} important?

A) Learning
B) Practice
C) Development
D) All of the above

3. Which field uses {topic}?

A) AI
B) Web Development
C) Data Science
D) All of the above
"""