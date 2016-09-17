import sys
import textwrap

names = sorted(sys.modules.keys())
names_text = ",".join(names)

print textwrap.fill(names_text)

print "\n"

for name in sys.builtin_module_names:
    print name