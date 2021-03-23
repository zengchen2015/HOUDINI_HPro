import hou

def edge(node_relative_path):
    node = hou.pwd()
    input_node = node.node(node_relative_path)
    geo = input_node.geometry()
    final_list = []

    if geo:
        edge_group_tuple = geo.edgeGroups()

        for edge_group in edge_group_tuple:
            edge_group_name = edge_group.name()
            final_list.append(edge_group_name)
            final_list.append(edge_group_name)

    return final_list

def prim(node_relative_path):
    node = hou.pwd()
    input_node = node.node(node_relative_path)
    geo = input_node.geometry()
    final_list = []

    if geo:
        prim_group_tuple = geo.primGroups()

        for prim_group in prim_group_tuple:
            prim_group_name = prim_group.name()
            final_list.append(prim_group_name)
            final_list.append(prim_group_name)

    return final_list


def point(node_relative_path):
    node = hou.pwd()
    input_node = node.node(node_relative_path)
    geo = input_node.geometry()
    final_list = []

    if geo:
        point_group_tuple = geo.pointGroups()

        for point_group in point_group_tuple:
            point_group_name = point_group.name()
            final_list.append(point_group_name)
            final_list.append(point_group_name)

    return final_list
