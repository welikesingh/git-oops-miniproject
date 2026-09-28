# Class Diagram

```

                    ┌──────────────────┐
                    │   User (ABC)     │
                    ├──────────────────┤
                    │ name             │
                    │ email            │
                    │ user_id          │
                    ├──────────────────┤
                    │ display_info()   │
                    │ validate_email() │ ← staticmethod
                    │ create_user()    │ ← classmethod
                    └────────┬─────────┘
                             │
                    ┌────────┴─────────┐
                    │                  │
             ┌──────▼──────┐    ┌──────▼──────┐
             │   Student   │    │   Mentor    │
             ├─────────────┤    ├─────────────┤
             │ course list │    │ expertise   │
             │ enroll()    │    │ add_course()│
             └──────┬──────┘    └──────┬──────┘
                    │                  │
                    │                  │
                    │           ┌──────▼──────┐
                    │           │    Course   │
                    │           ├─────────────┤
                    └──────────►│ course_id   │
                                │ course_name │
                                │ mentor      │
                                └──────┬──────┘
                                       │
                                ┌──────▼────────┐
                                │  Enrollment   │
                                ├───────────────┤
                                │ student       │
                                │ course        │
                                │ status        │
                                └───────────────┘

```


# Git development plan

```
main
 │
 ├── feature-user
 │      └── User / Student / Mentor
 │
 ├── feature-course
 │      └── Course functionality
 │
 ├── feature-enrollment
 │      └── Enrollment functionality
 │
 └── feature-readme
        └── Documentation
```


git init
git branch -M main

git checkout -b feature-user

# implement User, Student, Mentor
# run    python -m src.main

git add .
git commit -m "Add User Student and Mentor classes"
git push -u origin feature-user



## Description
The name __init__ shows up in two different places.The __init__.py file: marks a folder as a package

Encapsulation:class controls how its internal data is modified.
Encapsulation: We don't directly expose the email. access it through getter

Every child class provide its own implementation of display_role()
obj.display_role() return different values. same method name behaves differently depending on the object.
We also override: display_info() in both child classes.
