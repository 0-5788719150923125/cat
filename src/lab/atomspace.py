from opencog.atomspace import AtomSpace, types
from opencog.execute import execute_atom

# import opencog.logger
# import opencog.scheme_wrapper
from opencog.utilities import set_default_atomspace, initialize_opencog
from opencog.type_constructors import *


if __name__ == "__main__":
    atomspace = AtomSpace()
    set_default_atomspace(atomspace)
    initialize_opencog(atomspace)

    atom = ConceptNode("My first python created node")
    atom.tv = TruthValue(0.75, 0.1)

    print(atom.long_string())
    print(atom.atomspace)

    link = SimilarityLink(
        ConceptNode("I can refer to this atom now"), ConceptNode("this one too")
    )

    print(link)
    print(link.atomspace)

    my_nodes = atomspace.get_atoms_by_type(types.ConceptNode)

    print(my_nodes)
    print(my_nodes[0].type_name)

    cat = atomspace.add_node(types.ConceptNode, "Cat")
    man = atomspace.add_node(types.ConceptNode, "Man")
    animal = atomspace.add_node(types.ConceptNode, "Animal")

    atomspace.add_link(types.InheritanceLink, [man, animal])

    color = ConceptNode("Color")
    c1 = ConceptNode("Blue")
    color_link = InheritanceLink(c1, color)

    InheritanceLink(ConceptNode("Red"), color)
    InheritanceLink(ConceptNode("Green"), color)
    InheritanceLink(ConceptNode("Blue"), color)

    # Create a pattern to look for color nodes
    varlink = TypedVariableLink(VariableNode("$xcol"), TypeNode("ConceptNode"))
    pattern = InheritanceLink(VariableNode("$xcol"), color)
    colornodes = GetLink(varlink, pattern)

    output = execute_atom(atomspace, colornodes)
    print(output)
