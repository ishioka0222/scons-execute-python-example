import os
env = Environment(ENV=os.environ.copy())

env.Command(
    target="output.txt",
    source=None,
    action="python script.py --out $TARGET"
)
