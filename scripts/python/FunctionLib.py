import hou
import AttributeName as an

def findPointAttrType(node_relative_path, attr_name):
    attr_type = "none"
    point_attrs = an.point(node_relative_path)

    if attr_name in point_attrs:
        if attr_name in an.pointFloat(node_relative_path):
            attr_type = "f"
        elif attr_name in an.pointInt(node_relative_path):
            attr_type = "i"
        elif attr_name in an.pointString(node_relative_path):
            attr_type = "s"
        elif attr_name in an.pointVector2(node_relative_path):
            attr_type = "u"
        elif attr_name in an.pointVector(node_relative_path):
            attr_type = "v"
        elif attr_name in an.pointVector4(node_relative_path):
            attr_type = "p"

    return attr_type

def findPrimAttrType(node_relative_path, attr_name):
    attr_type = "none"
    prim_attrs = an.prim(node_relative_path)

    if attr_name in prim_attrs:
        if attr_name in an.primFloat(node_relative_path):
            attr_type = "f"
        elif attr_name in an.primInt(node_relative_path):
            attr_type = "i"
        elif attr_name in an.primString(node_relative_path):
            attr_type = "s"
        elif attr_name in an.primVector2(node_relative_path):
            attr_type = "u"
        elif attr_name in an.primVector(node_relative_path):
            attr_type = "v"

    return attr_type