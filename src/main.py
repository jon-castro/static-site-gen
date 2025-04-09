import os
import shutil


def copy_directory(source, destination):
    for item in os.listdir(source):
        source_path = os.path.join(source, item)
        destination_path = os.path.join(destination, item)
        
        if os.path.isdir(source_path):
            if not os.path.exists(destination_path):
                os.mkdir(destination_path)
            copy_directory(source_path, destination_path)
        elif os.path.isfile(source_path):
            shutil.copy(source_path, destination_path)
            
def copy_static(source, destination):
    if os.path.exists(destination):
        shutil.rmtree(destination)
    os.mkdir(destination)
    copy_directory(source, destination)

def main():
    # print(TextNode('This is some anchor text', TextType.LINK, 'https://www.boot.dev'))
    static_dir = "static"
    public_dir = "public"

    print(f"Copying static files from {static_dir} to {public_dir}...")
    copy_static(static_dir, public_dir)
    print(f"Static files copied successfully!")
    
if __name__ == "__main__":    
    main()