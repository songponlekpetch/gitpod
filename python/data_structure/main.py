from general_tree.tree_node import TreeNode

organnization = {
    "nilupul": {"name": "Nilupul", "position": "CEO"},
    "chinmay": {"name": "Chinmay", "position": "CTO"},
    "vishwa": {"name": "Vishwa", "position": "Infrastructure Head"},
    "dhaval": {"name": "Dhaval", "position": "Cloud Manager"},
    "abhijit": {"name": "Abhijit", "position": "App Manager"},
    "aamir": {"name": "Aamir", "position": "Application Head"},
    "gels": {"name": "Gels", "position": "HR Head"},
    "peter": {"name": "Peter", "position": "Recruitment Manager"},
    "waqas": {"name": "Waqas", "position": "Policy Manager"},
}

def main():
    root = TreeNode(organnization["nilupul"])

    chinmay = TreeNode(organnization["chinmay"])
    chinmay.add_child(TreeNode(organnization["vishwa"]))
    chinmay.add_child(TreeNode(organnization["dhaval"]))
    chinmay.add_child(TreeNode(organnization["abhijit"]))
    chinmay.add_child(TreeNode(organnization["aamir"]))
    
    gels = TreeNode(organnization["gels"])
    gels.add_child(TreeNode(organnization["peter"]))
    gels.add_child(TreeNode(organnization["waqas"]))
    
    root.add_child(chinmay)
    root.add_child(gels)

    root.print_data_by()

if __name__ == "__main__":
    main()
