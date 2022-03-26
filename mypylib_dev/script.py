import mypylib

print(
  mypylib.somemethods.minus(1),  # somemethods.py
  mypylib.p2(1),                 # someothermethods.py
)

print(
  mypylib.package.div(4),
  mypylib.package.packagesublevel.subdiv(4),
)
