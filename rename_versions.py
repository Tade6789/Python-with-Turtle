import os
import shutil

for filename in os.listdir('.'): 
    if filename.endswith('.py') and not filename.startswith('v'):
        for i in range(1, 13):  # v1 to v12
            new_name = f"v{i}_{filename}"
            if not os.path.exists(new_name):
                shutil.copy(filename, new_name)
                print(f"Created {new_name}")
