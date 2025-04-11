import sys
from page_generation import copy_static
from page_generation import generate_pages_recursive


def main():
    basepath = sys.argv[1] if len(sys.argv) > 1 else "/"
    
    static_dir = "static"
    output_dir = "docs"

    copy_static(static_dir, output_dir)
   
    generate_pages_recursive(
        dir_path_content="content", 
        template_path="template.html",
        dest_dir_path=output_dir,
        basepath=basepath,
    )
    
if __name__ == "__main__":    
    main()