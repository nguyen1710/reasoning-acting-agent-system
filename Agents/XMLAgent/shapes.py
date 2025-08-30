
def actor_style() -> str:
    return (
        "shape=umlActor;"
        "verticalLabelPosition=bottom;"
        "verticalAlign=top;"
        "html=1;"
        "outlineConnect=0;"
    )

def usecase_style() -> str:
    return "ellipse;whiteSpace=wrap;html=1;"

def system_container_style() -> str:
    return (
        "shape=rectangle;"
        "rounded=0;"
        "dashed=0;"
        "whiteSpace=wrap;"
        "html=1;"
        "fillColor=none;"
        "strokeColor=black;"
    )

def edge_style(rel_type: str) -> tuple[str, str]:
    """
    Trả về (style, nhãn) cho từng loại quan hệ trong UML.
    """
    if rel_type == "association":
        return "endArrow=none;html=1;rounded=0;", ""
    elif rel_type == "include":
        return "endArrow=open;dashed=1;html=1;", "«include»"
    elif rel_type == "extend":
        return "endArrow=open;dashed=1;html=1;", "«extend»"
    elif rel_type == "generalization":
        return "endArrow=block;endFill=0;html=1;", ""
    elif rel_type == "dependency":
        return "endArrow=open;dashed=1;html=1;", ""
    return "endArrow=none;html=1;rounded=0;", ""
