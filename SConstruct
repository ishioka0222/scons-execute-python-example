import os
env = Environment(ENV={'PATH': os.environ['PATH']})

env.Command(
    target="output.txt",
    source=None,
    action="python script.py --out $TARGET"
)
