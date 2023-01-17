# convert_obj_to_map.py

import os

class Vertex:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

class Face:
    def __init__(self):
        self.vertices = []
    def __str__(self, num):
        return "v {0} {1} {2} t 0 0 8 8".format(self.vertices[num].z, self.vertices[num].x, self.vertices[num].y)

class Model:
    def __init__(self):
        self.vertices = []
        self.faces = []

class Main:
    def __init__(self):
        # Define input and output directories
        self.obj_input_dir = "input"
        self.map_output_dir = "output"

        # Get list of obj files in input directory
        self.obj_files = [f for f in os.listdir(self.obj_input_dir) if f.endswith(".obj")]

    def convert(self):
        for obj_file in self.obj_files:
            print("Processing file: ", obj_file)
            model = Model()
            self.read_obj_file(obj_file, model)
            self.write_map_file(obj_file, model)
            print("Completed. New file:", obj_file.replace(".obj", ".map"))

    def read_obj_file(self, obj_file, model):
        with open(os.path.join(self.obj_input_dir, obj_file), "r") as obj_file:
            for line in obj_file:

                # Check if line is a vertex
                if line.startswith("v "):
                    x, y, z = map(float, line.split()[1:])

                    # Convert to inches from cm
                    x /= 2.54
                    y /= 2.54
                    z /= 2.54

                    model.vertices.append(Vertex(x, y, z))
                
                # Check if line is a face
                elif line.startswith("f "):
                    face = Face()
                    for vertex_str in line.split()[1:]:
                        vertex_index = vertex_str.split("/")[0] 
                        vertex_index = int(vertex_index) - 1 
                        vertex = model.vertices[vertex_index]
                        face.vertices.append(vertex)
                    model.faces.append(face)

    def write_map_file(self, obj_file, model):
        with open(os.path.join(self.map_output_dir, obj_file.replace(".obj", ".map")), "w") as map_file:

            # Write header            
            map_file.write("iwmap 4\n"
                            "\"000_Global\" flags  active\n"
                            "\"The Map\" flags\n"
                            "// entity 0\n"
                            "{\n"
                            "    \"classname\" \"worldspawn\"\n")

            # Write faces as brushes
            index = 0
            for face in model.faces:
                map_file.write(f"    // brush {index}\n"
                                "    {\n"
                                "        mesh\n"
                                "        {\n"
                                "            toolFlags splitGeo;\n"
                                "            caulk\n"
                                "            lightmap_gray\n"
                                "            smoothing smoothing_hard\n"
                                "            2 2 0 8\n"
                                "            (\n"
                                f"                {face.__str__(2)}\n"
                                f"                {face.__str__(1)}\n"
                                "            )\n"
                                "            (\n"
                                f"                {face.__str__(0)}\n"
                                f"                {face.__str__(1)}\n"
                                "            )\n"
                                "        }\n"
                                "    }\n")
                index += 1

            # Write footer
            map_file.write("}\n")

if __name__ == "__main__":
    Main().convert()
