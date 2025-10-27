class ClassroomAttendanceSystem:
    def __init__(self):
        self.students = {}
        self.attendance_records = {}
        self.classroom_groups = []

    def display_menu(self):
        """Display the main menu interface"""
        print("\n" + "=" * 40)
        print("    CLASSROOM ATTENDANCE SYSTEM")
        print("=" * 40)
        print("1. Add New Classroom Group")
        print("2. Add Student to Group")
        print("3. Record Attendance")
        print("4. View Attendance by Date")
        print("5. Search Student Attendance")
        print("6. Search Group Attendance")
        print("7. Delete Student")
        print("8. Delete Classroom Group")
        print("9. Exit System")
        print("=" * 40)

    def add_classroom_group(self):
        """Add a new classroom group to the system"""
        group_name = input("Enter new classroom group name: ").strip()

        if not group_name:
            print("Error: Group name cannot be empty!")
            return

        if group_name in self.classroom_groups:
            print(f"Error: Group '{group_name}' already exists!")
        else:
            self.classroom_groups.append(group_name)
            print(f"Success: Group '{group_name}' added!")

    def add_student_to_group(self):
        """Add a new student to an existing classroom group"""
        if not self.classroom_groups:
            print("Error: No groups available. Please add a group first.")
            return

        print("\nAvailable groups:", ", ".join(self.classroom_groups))
        selected_group = input("Enter group name: ").strip()

        if selected_group not in self.classroom_groups:
            print("Error: Group not found!")
            return

        student_id = input("Enter student ID: ").strip()
        student_name = input("Enter student name: ").strip()

        if not student_id or not student_name:
            print("Error: Student ID and name cannot be empty!")
            return

        if student_id in self.students:
            print("Error: Student ID already exists!")
        else:
            self.students[student_id] = {
                "name": student_name,
                "group": selected_group
            }
            print(f"Success: Student '{student_name}' added to group '{selected_group}'!")

    def validate_date(self, date_str):
        """Basic date validation (DD-MM-YYYY format)"""
        if len(date_str) != 10 or date_str[2] != '-' or date_str[5] != '-':
            return False

        day, month, year = date_str.split('-')
        return day.isdigit() and month.isdigit() and year.isdigit()

    def record_attendance(self):
        """Record attendance for a specific date and group"""
        date = input("Enter date (DD-MM-YYYY): ").strip()

        if not self.validate_date(date):
            print("Error: Invalid date format! Use DD-MM-YYYY.")
            return

        if not self.classroom_groups:
            print("Error: No groups available. Please add a group first.")
            return

        print("\nAvailable groups:", ", ".join(self.classroom_groups))
        selected_group = input("Enter group name: ").strip()

        if selected_group not in self.classroom_groups:
            print("Error: Group not found!")
            return

        # Initialize attendance record for date if not exists
        if date not in self.attendance_records:
            self.attendance_records[date] = {}

        # Get students in the selected group
        students_in_group = {
            sid: info for sid, info in self.students.items()
            if info["group"] == selected_group
        }

        if not students_in_group:
            print("No students found in this group!")
            return

        print(f"\nRecording attendance for {selected_group} on {date}:")
        print("-" * 40)

        count = 0
        for student_id, student_info in students_in_group.items():
            while True:
                status = input(f"Is {student_info['name']} present? (Y/N): ").strip().upper()
                if status in ['Y', 'N']:
                    self.attendance_records[date][student_id] = (status == 'Y')
                    count += 1
                    break
                else:
                    print("Please enter 'Y' for Yes or 'N' for No.")

        print(f"\nSuccess: Attendance recorded for {count} students!")

    def view_attendance_by_date(self):
        """View attendance records for a specific date"""
        date = input("Enter date to view (DD-MM-YYYY): ").strip()

        if date not in self.attendance_records:
            print(f"No attendance records found for {date}")
            return

        print(f"\nAttendance for {date}:")
        print("-" * 40)

        found_records = False
        for student_id, present_status in self.attendance_records[date].items():
            if student_id in self.students:
                status_text = "Present" if present_status else "Absent"
                print(f"{self.students[student_id]['name']}: {status_text}")
                found_records = True

        if not found_records:
            print("No valid student records found for this date.")

    def search_student_attendance(self):
        """Search for attendance history of a specific student"""
        search_term = input("Enter student ID or name: ").strip()

        if not search_term:
            print("Error: Search term cannot be empty!")
            return

        print(f"\nAttendance history for '{search_term}':")
        print("-" * 40)

        found = False
        for date, daily_records in self.attendance_records.items():
            for student_id, present_status in daily_records.items():
                if student_id in self.students:
                    student_name = self.students[student_id]["name"]
                    if student_id == search_term or student_name.lower() == search_term.lower():
                        status_text = "Present" if present_status else "Absent"
                        print(f"{date}: {status_text}")
                        found = True

        if not found:
            print("No attendance records found for this student.")

    def search_group_attendance(self):
        """Generate attendance report for a specific group"""
        if not self.classroom_groups:
            print("Error: No groups available.")
            return

        print("\nAvailable groups:", ", ".join(self.classroom_groups))
        selected_group = input("Enter group name: ").strip()

        if selected_group not in self.classroom_groups:
            print("Error: Group not found!")
            return

        print(f"\nAttendance summary for '{selected_group}':")
        print("=" * 50)

        found_records = False
        for date, daily_records in self.attendance_records.items():
            present_count = 0
            total_count = 0

            for student_id, present_status in daily_records.items():
                if student_id in self.students and self.students[student_id]["group"] == selected_group:
                    total_count += 1
                    if present_status:
                        present_count += 1

            if total_count > 0:
                percentage = (present_count / total_count) * 100
                print(f"Date: {date}")
                print(f"Attendance: {present_count}/{total_count} ({percentage:.1f}%)")
                print("-" * 30)
                found_records = True

        if not found_records:
            print("No attendance records found for this group.")

    def delete_student(self):
        """Delete a student and their attendance records"""
        student_id = input("Enter student ID to delete: ").strip()

        if student_id not in self.students:
            print("Error: Student not found!")
            return

        student_name = self.students[student_id]["name"]
        group_name = self.students[student_id]["group"]

        # Remove student from students dictionary
        del self.students[student_id]

        # Remove student from all attendance records
        for date in list(self.attendance_records.keys()):
            if student_id in self.attendance_records[date]:
                del self.attendance_records[date][student_id]

            # Remove date entry if no records left
            if not self.attendance_records[date]:
                del self.attendance_records[date]

        print(f"Success: Student '{student_name}' deleted from group '{group_name}'!")

    def delete_classroom_group(self):
        """Delete a classroom group and all associated data"""
        if not self.classroom_groups:
            print("Error: No groups available.")
            return

        print("\nAvailable groups:", ", ".join(self.classroom_groups))
        group_to_delete = input("Enter group name to delete: ").strip()

        if group_to_delete not in self.classroom_groups:
            print("Error: Group not found!")
            return

        # Remove group from classroom_groups list
        self.classroom_groups.remove(group_to_delete)

        # Find and remove students belonging to this group
        students_to_remove = []
        for student_id, student_info in self.students.items():
            if student_info["group"] == group_to_delete:
                students_to_remove.append(student_id)

        # Remove students belonging to this group
        for student_id in students_to_remove:
            del self.students[student_id]

        # Remove attendance records for students in this group
        for date in list(self.attendance_records.keys()):
            for student_id in students_to_remove:
                if student_id in self.attendance_records[date]:
                    del self.attendance_records[date][student_id]

            # Remove date entry if no records left
            if not self.attendance_records[date]:
                del self.attendance_records[date]

        print(f"Success: Group '{group_to_delete}' and all associated data deleted!")

    def run(self):
        """Main program loop"""
        print("Welcome to the Classroom Attendance System!")

        while True:
            self.display_menu()
            user_choice = input("Enter your choice (1-9): ").strip()

            if user_choice == "1":
                self.add_classroom_group()
            elif user_choice == "2":
                self.add_student_to_group()
            elif user_choice == "3":
                self.record_attendance()
            elif user_choice == "4":
                self.view_attendance_by_date()
            elif user_choice == "5":
                self.search_student_attendance()
            elif user_choice == "6":
                self.search_group_attendance()
            elif user_choice == "7":
                self.delete_student()
            elif user_choice == "8":
                self.delete_classroom_group()
            elif user_choice == "9":
                print("\nThank you for using the Classroom Attendance System. Goodbye!")
                break
            else:
                print("Invalid choice! Please enter a number between 1-9.")

            input("\nPress Enter to continue...")


# Main program execution
if __name__ == "__main__":
    try:
        system = ClassroomAttendanceSystem()
        system.run()
    except KeyboardInterrupt:
        print("\n\nProgram interrupted by user. Goodbye!")
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")
