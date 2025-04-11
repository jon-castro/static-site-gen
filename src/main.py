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
    generate_page(
        from_path="content/blog/glorfindel/index.md",
        template_path="template.html",
        dest_path="public/blog/glorfindel/index.html",
    )    
    generate_page(
        from_path="content/blog/majesty/index.md",
        template_path="template.html",
        dest_path="public/blog/majesty/index.html",
    )    
    generate_page(
        from_path="content/blog/tom/index.md",
        template_path="template.html",
        dest_path="public/blog/tom/index.html",
    )    
    generate_page(
        from_path="content/contact/index.md",
        template_path="template.html",
        dest_path="public/contact/index.html",
    )    
    
    
if __name__ == "__main__":    
    main()