import xml.etree.ElementTree as ET
from .State import State

class UMLXMLBuilder:
    def __init__(self, state: State, canvas_height=600):
        self.state = state
        self.canvas_height = canvas_height
        self.root = ET.Element(
            "mxGraphModel",
            dx="1422", dy="794", grid="1", gridSize="10", guides="1",
            tooltips="1", connect="1", arrows="1", fold="1", page="1",
            pageScale="1", pageWidth="827", pageHeight="1169", math="0", shadow="0"
        )
        self.root_inner = ET.SubElement(self.root, "root")
        ET.SubElement(self.root_inner, "mxCell", id="0")
        ET.SubElement(self.root_inner, "mxCell", id="1", parent="0")
        self.id_counter = 1
        self.element_ids = {}  # map name -> mxCell id

    def _next_id(self, prefix="id"):
        self.id_counter += 1
        return f"{prefix}_{self.id_counter}"

    def _create_vertex(self, name, style, x, y, w=120, h=60, parent="1"):
        vid = self._next_id("v")
        self.element_ids[name] = vid
        cell = ET.SubElement(
            self.root_inner,
            "mxCell",
            id=vid,
            value=name,
            style=style,
            vertex="1",
            parent=parent
        )
        ET.SubElement(cell, "mxGeometry",
                      **{"x": str(x), "y": str(y), "width": str(w), "height": str(h), "as": "geometry"})
        return vid

    def build_actors(self):
        actors = self.state.get("actors", [])
        spacing = 150
        x = 50
        y = 50
        for actor in actors:
            self._create_vertex(
                actor,
                "shape=umlActor;verticalLabelPosition=bottom;verticalAlign=top;html=1;outlineConnect=0;",
                x, y, 40, 80
            )
            y += spacing

    def build_functions(self):
        funcs = self.state.get("usecases", [])
        # nếu là list of dict (cũ), flatten nó
        if funcs and isinstance(funcs[0], dict):
            flat_funcs = []
            for group in funcs:
                flat_funcs.extend(group.get("usecases", []))
            funcs = flat_funcs

        if not funcs:
            return

        spacing = 120
        x = 350
        y = 100
        for func in funcs:
            self._create_vertex(
                func,
                "ellipse;whiteSpace=wrap;html=1;",
                x, y, 140, 60
            )
            y += spacing


    def build_usecase_container(self):
        """Tạo hình chữ nhật bao quanh toàn bộ các use case"""
        funcs = self.state.get("usecases", [])
        if funcs and isinstance(funcs[0], dict):
            flat_funcs = []
            for group in funcs:
                flat_funcs.extend(group.get("usecases", []))
            funcs = flat_funcs

        if not funcs:
            return

        height = 120 * len(funcs) + 50
        width = 300
        x = 300
        y = 50

        self._create_vertex(
            "System",
            "shape=rectangle;rounded=0;dashed=0;whiteSpace=wrap;html=1;fillColor=none;strokeColor=black;",
            x, y, width, height
        )



    def build_relationships(self):
        for rel in self.state.get("relationships", []):
            source = rel.get("source") or rel.get("actor") or rel.get("function")
            target = rel.get("target") or rel.get("entity") or rel.get("function")
            rel_type = rel.get("type", "association")

            if not source or not target:
                continue

            targets = target if isinstance(target, list) else [target]

            for tgt in targets:
                if source == tgt:
                    continue
                if source not in self.element_ids or tgt not in self.element_ids:
                    continue

                style = "endArrow=none;html=1;rounded=0;"
                value = ""

                if rel_type == "association":
                    style = "endArrow=none;html=1;rounded=0;"
                elif rel_type == "include":
                    style = "endArrow=open;dashed=1;html=1;"
                    value = "«include»"
                elif rel_type == "extend":
                    style = "endArrow=open;dashed=1;html=1;"
                    value = "«extend»"
                elif rel_type == "generalization":
                    style = "endArrow=block;endFill=0;html=1;"
                elif rel_type == "dependency":
                    style = "endArrow=open;dashed=1;html=1;"

                edge_id = self._next_id("edge")
                edge = ET.SubElement(
                    self.root_inner,
                    "mxCell",
                    id=edge_id,
                    value=value,
                    style=style,
                    edge="1",
                    parent="1",
                    source=self.element_ids[source],
                    target=self.element_ids[tgt]
                )
                ET.SubElement(edge, "mxGeometry", **{"relative": "1", "as": "geometry"})

    def build_all(self):
        self.build_actors()
        self.build_usecase_container()
        self.build_functions()
        self.build_relationships()

    def to_xml_string(self):
        return ET.tostring(self.root, encoding="unicode")

    def save_xml(self, filename: str):
        tree = ET.ElementTree(self.root)
        tree.write(filename, encoding="utf-8", xml_declaration=True)
