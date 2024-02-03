bl_info = {
    "name": "Emission Material Lamps",
    "blender": (4, 0, 0),
    "category": "Object",
}

if "bpy" in locals():
    import importlib
    if "emission_material_lamps" in locals():
        importlib.reload(emission_material_lamps)

else:
    from . import emission_material_lamps

def register():
    emission_material_lamps.register()

def unregister():
    emission_material_lamps.unregister()

if __name__ == "__main__":
    register()
