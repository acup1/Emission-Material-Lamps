import bpy

class OBJECT_PT_EmissionMaterial(bpy.types.Panel):
    bl_label = "Emission Material Lamps"
    bl_idname = "PT_EmissionMaterialLamps"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Lamps'

    def draw(self, context):
        layout = self.layout
        layout.operator("object.add_emission_material", text="Add Emission Material")

def add_emission_material():
    obj = bpy.context.active_object

    material = bpy.data.materials.new(name="EmissionMaterial")

    if obj.data.materials:
        obj.data.materials[0] = material
    else:
        obj.data.materials.append(material)

    material.use_nodes = True
    nodes = material.node_tree.nodes
    emission_node = nodes.new(type='ShaderNodeEmission')
    output_node = nodes.get("Material Output")

    material.node_tree.links.new(emission_node.outputs["Emission"], output_node.inputs["Surface"])

    emission_node.inputs["Color"].default_value = (1.0, 1.0, 1.0, 1.0)
    emission_node.inputs["Strength"].default_value = 10.0

    obj.visible_camera = False
    obj.visible_shadow = False

class OBJECT_OT_AddEmissionMaterial(bpy.types.Operator):
    bl_label = "Create lamp"
    bl_idname = "object.add_emission_material"

    def execute(self, context):
        add_emission_material()
        return {'FINISHED'}

def register():
    bpy.utils.register_class(OBJECT_PT_EmissionMaterial)
    bpy.utils.register_class(OBJECT_OT_AddEmissionMaterial)

def unregister():
    bpy.utils.unregister_class(OBJECT_PT_EmissionMaterial)
    bpy.utils.unregister_class(OBJECT_OT_AddEmissionMaterial)

if __name__ == "__main__":
    register()
