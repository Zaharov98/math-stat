library(DiagrammeR)

# grViz("
#      graph mygraph {
#      a -- b -- c;
#      b -- d;
#      }
#    ")
# grViz("
#       digraph mygraph {
#       a -> b -> c;
#       b -> d;
#       }
#     ")
# grViz("
#       digraph mygraph {
#       a [label='Foo'];
#       b [shape= box];
#       a -> b -> c [color=blue];
#       b -> d [style=dotted];
#       }
#     ")
grViz("
      digraph xpath {
      html -> head -> title;
      html -> body;
      body -> {h1 'p' 'p[@class=abastract]' 'div[@class=abstact]' div}
      'div[@class=abstact]' -> {'p[1]' 'p[2]' 'p[@id=date]'}
      }
      ")
