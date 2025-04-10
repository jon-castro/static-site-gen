from page_generation import copy_static
from page_generation import generate_page


def main():
    static_dir = "static"
    public_dir = "public"

    copy_static(static_dir, public_dir)
    
    generate_page(
        from_path="content/index.md",
        template_path="template.html",
        dest_path="public/index.html",
    )    
    
    
if __name__ == "__main__":    
    main()