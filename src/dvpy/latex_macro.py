
def latex_macro(variable, value):
  assert(variable.isalpha())
  return '\\newcommand{\\%s}{%s}'%(variable, value)
