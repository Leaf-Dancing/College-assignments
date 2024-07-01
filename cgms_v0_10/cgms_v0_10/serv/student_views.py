from fastapi import Request
from .config import app, view_page
# from .config import dblock
# from .error_view import redirect_error


@app.get("/student")
async def view_student_list(request: Request):
    return view_page(request, "student_list.html")
