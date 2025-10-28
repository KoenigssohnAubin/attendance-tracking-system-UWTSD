class ClassroomAttendanceSystem:
    def __init__(self):
        self.students = {
            "S2337525": {"name": "Alice Johnson", "group": "CertHE"},
            "S2216535": {"name": "Bob Smith", "group": "CertHE"},
            "S2014499": {"name": "Carol Davis", "group": "CertHE"},
            "S2004186": {"name": "David Wilson", "group": "CertHE"},
            "S2221070": {"name": "Eva Brown", "group": "CertHE"},
            "S2016791": {"name": "Frank Miller", "group": "CertHE"},
            "S2337005": {"name": "Alice Johnson", "group": "CertHE"},
            "S2216035": {"name": "Baba May", "group": "CertHE"},
            "S2010099": {"name": "Carl Dav", "group": "CertHE"},
            "S2004586": {"name": "Ali Khan", "group": "CertHE"},
            "S2991070": {"name": "Eva Max", "group": "CertHE"},
            "S2016001": {"name": "Frank Kaiser", "group": "CertHE"},
            "S2337510": {"name": "Marc Boula", "group": "CertHE"},
            "S2200535": {"name": "Bobby Smith", "group": "CertHE"},
            "S2000499": {"name": "Marco Davis", "group": "Level 5"},
            "S2000186": {"name": "Davidson William", "group": "Level 5"},
            "S2001070": {"name": "Papa Brown", "group": "Level 5"},
            "S2000791": {"name": "Frank Miller", "group": "Level 5"},
            "S2007525": {"name": "Samba Johnson", "group": "Level 5"},
            "S2006535": {"name": "Bobby Smith", "group": "Level 5"},
            "S2001499": {"name": "Carolina Davis", "group": "Level 5"},
            "S2000189": {"name": "David Wilson", "group": "Level 5"},
            "S2001079": {"name": "Carol Brown", "group": "Level 5"},
            "S2000701": {"name": "Frank Miller", "group": "Level 5"},
            "S2000009": {"name": "Marco Cameroon", "group": "Level 6"},
            "S2000006": {"name": "David William", "group": "Level 6"},
            "S2000070": {"name": "Papa Camara", "group": "Level 6"},
            "S2000091": {"name": "Franky Miller", "group": "Level 6"},
            "S2000025": {"name": "Samba Papa", "group": "Level 6"},
            "S2000035": {"name": "Bobby Smith", "group": "Level 6"},
            "S2000099": {"name": "Carol Dave", "group": "Level 6"},
            "S2000019": {"name": "David Will", "group": "Level 6"},
            "S2000079": {"name": "Carol Brown", "group": "Level 6"},
            "S2000001": {"name": "Frank Midland", "group": "Level 6"},

        }
        self.attendance_records = {
            "13-10-2025": {
                "S2337525": True,  # Alice present
                "S2216535": False,  # Bob absent
                "S2014499": True,  # Carol present
                "S2004186": True,  # David present
                "S2221070": False,  # Eva absent
                "S2016791": True,  # Frank present
                "S2337005": True,  # Alice present
                "S2216035": True,  # Baba present
                "S2010099": True,  # Carl present
                "S2004586": True,  # Ali present
                "S2991070": False,  # Eva Max absent
                "S2016001": True,  # Frank present
                "S2337510": False,  # Marc absent
                "S2200535": True,  # Bobby present
                "S2000499": True,  # Marco present
                "S2000186": True,  # Davidson present
                "S2001070": True,  # Papa present
                "S2000791": False,  # Frank absent
                "S2007525": True,  # Samba present
                "S2006535": False,  # Bobby absent
                "S2001499": True,  # Carolina present
                "S2000189": False,  # David absent
                "S20001079": False,  # Carol absent
                "S2000701": True,  # Frank Miller present
                "S2000009": True,  # Marco absent
                "S2000006": True,  # David William present
                "S2000070": True,  # Papa Camara present
                "S2000091": False,  # Franky absent
                "S2000025": True,  # Samba present
                "S2000035": True,  # Bobby Smith present
                "S2000099": False,  # Carol Dave absent
                "S2000019": False,  # David Will absent
                "S2000079": False,  # Carol Brown absent
                "S2000001": False,  # Frank Midland absent
            },
            "14-10-2025": {
                "S2337525": True,  # Alice present
                "S2216535": False,  # Bob absent
                "S2014499": True,  # Carol present
                "S2004186": True,  # David present
                "S2221070": False,  # Eva absent
                "S2016791": True,  # Frank present
                "S2337005": True,  # Alice present
                "S2216035": True,  # Baba present
                "S2010099": True,  # Carl present
                "S2004586": True,  # Ali present
                "S2991070": False,  # Eva Max absent
                "S2016001": True,  # Frank present
                "S2337510": False,  # Marc absent
                "S2200535": True,  # Bobby present
                "S2000499": True,  # Marco present
                "S2000186": True,  # Davidson present
                "S2001070": True,  # Papa present
                "S2000791": False,  # Frank absent
                "S2007525": True,  # Samba present
                "S2006535": True,  # Bobby present
                "S2001499": True,  # Carolina present
                "S2000189": False,  # David absent
                "S20001079": False,  # Carol absent
                "S2000701": True,  # Frank Miller present
                "S2000009": True,  # Marco absent
                "S2000006": True,  # David William present
                "S2000070": True,  # Papa Camara present
                "S2000091": False,  # Franky absent
                "S2000025": True,  # Samba present
                "S2000035": True,  # Bobby Smith present
                "S2000099": True,  # Carol Dave present
                "S2000019": False,  # David Will absent
                "S2000079": False,  # Carol Brown absent
                "S2000001": True,  # Frank Midland present

            }
        }

        self.classroom_groups = ["CertHE", "Level 5", "Level 6"]

    def display_menu(self):
        """Display the main menu interface"""
        print("\n" + "=" * 45)
        print(" CLASSROOM ATTENDANCE SYSTEM by KOENIGSSOHN")
        print("=" * 45)

        print("Please select an option from the menu:")

        print("\n" + "*" * 45)
        print("1. Add new classroom Group")
        print("2. Add new students to Group")
        print("3. Record attendance")
        print("4. View:   'attendance records'")
        print("5. Search: 'student attendance'")
        print("6. Search: 'group attendance'")
        print("7. Delete student")
        print("8. Delete classroom group")
        print("9. EXIT SYSTEM ")
        print("\n" + "*" * 45)

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
        student_id = input("Enter student ID or Name to delete: ").strip()

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
        print("Welcome to the Classroom Attendance System by KOENIGSSOHN!")

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
                print("\nThank you for using the Classroom Attendance System by KOENIGSSOHN. Goodbye!")
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
        print("\n\nProgram interrupted by user. Thank You for using Bright Might Attendance App by "
              "KOENIGSSOHN Goodbye!")
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")
