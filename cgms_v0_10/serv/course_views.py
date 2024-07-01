from fastapi import Request
from .config import app, view_page
# from .config import dblock
# from .error_view import redirect_error


@app.get("/course")
async def view_student_list(request: Request):
    return view_page(request, "course_list.html")
