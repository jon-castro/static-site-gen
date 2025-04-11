from page_generation import copy_static
from page_generation import generate_page, generate_pages_recursive


def main():
    static_dir = "static"
    public_dir = "public"

    copy_static(static_dir, public_dir)
   
    generate_pages_recursive(
        dir_path_content="content", 
        template_path="template.html",
        dest_dir_path="public",
    )
    
if __name__ == "__main__":    
    main()