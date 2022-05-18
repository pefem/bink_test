# functions handling question sections.
import json
import run_command
from questions import * # not a very good practice but used beacuse i have full control over questions module



class QuestionSections:

    def __init__(self) -> None:
    
        self.rows_obj = question_one()
        self.rows =  list(self.rows_obj)
        self.lease_years = question_two(self.rows)
        self.tenant_mast_data = question_three(self.rows)
        self.startdate_range = list(question_four(self.rows))

    
    # returns sorted list by "current rent" in ascending order
    def q1_section_a(self):

        self.rows.sort(key=lambda row:float(row["Current Rent"]))
        return self.rows
    

    # outputs the first five elements of the sorted list
    def q1_section_b(self, rows):
    
        for item in rows[0:5]:
            print(item)
    
    # outputs all data where lease years = 25
    def q2_section_a(self):

        print(self.lease_years)
    

    # outputs the total rent for data where lease years = 25
    def q2_section_b(self):
        
        total = 0

        for row_rent in self.lease_years:
            total += float(row_rent["Current Rent"])
        
        print(f"total_rent: {total}")


    # output in json format
    def q3_section_a(self):
        
        print(json.dumps(self.tenant_mast_data, indent=4))


    # output with formatted dates
    def q4_section_a(self):

        for item in self.startdate_range:

            changed_format = datetime.strftime(item["Lease Start Date"], "%d/%m/%Y")
            item["Lease Start Date"] = changed_format

            print(item)
            print("")
        




def main():

    command = input("Enter run command> ").lower()

    if command == run_command.password:
        question_sec = QuestionSections()
        all_rows = question_sec.q1_section_a()

        print("Question One B.....")
        question_sec.q1_section_b(all_rows)
        print("")
        print("__________________________")

        print("Question Two A.....")
        question_sec.q2_section_a()
        print("")
        print("__________________________")

        print("Question Two B.....")
        question_sec.q2_section_b()
        print("")
        print("__________________________")

        print("Question Three A.....")
        question_sec.q3_section_a()
        print("")
        print("__________________________")

        print("Question Four A.....")
        question_sec.q4_section_a()
        print("")
        print("__________________________")
    else:
        print("incorrect run command")




if __name__ == "__main__":
    main()



    
























# a = q1_section_a()
# q1_section_b(a)



