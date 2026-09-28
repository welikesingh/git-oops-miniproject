# Class Diagram

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
                    │           ├──────────────┤
                    └──────────►│ course_id   │
                                │ course_name │
                                │ mentor      │
                                └──────┬───────┘
                                       │
                                ┌──────▼────────┐
                                │  Enrollment   │
                                ├───────────────┤
                                │ student      │
                                │ course       │
                                │ status       │
                                └───────────────┘


# Git development plan

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


git init
git branch -M main

git checkout -b feature-user
# implement User, Student, Mentor
git add .
git commit -m "Add User Student and Mentor classes"
git push -u origin feature-user
