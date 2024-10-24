import csv
from faker import Faker

# Initialize Faker object
fake = Faker()

# Define the number of records to generate
num_records = 100000


csv_file = 'students_data.csv'


with open(csv_file, mode='w', newline='') as file:
    writer = csv.writer(file)
   
    writer.writerow(['MatricNo', 'LastName', 'FirstName', 'OtherNames', 'Title', 'MaidenName', 'Gender', 'DateOfBirth', 'Email', 'Telephone', 'CreatedBy', 'CreatedAt', 'UpdatedBy', 'UpdatedAt', 'RowVersion'])

    # Loop over the number of records and insert fake data into the CSV
    for _ in range(num_records):
        matric_no = fake.unique.random_number(digits=8)
        last_name = fake.last_name()
        first_name = fake.first_name()
        other_names = fake.first_name()
        title = fake.prefix()
        maiden_name = fake.last_name()
        gender = fake.random.choice(['Male', 'Female'])
        date_of_birth = fake.date_of_birth()
        email = fake.email()
        telephone = fake.phone_number()
        created_by = fake.random_int(min=1, max=20)
        created_at = fake.date_time_this_year()
        updated_by = fake.random_int(min=1, max=20)
        updated_at = fake.date_time_between(start_date='-1y', end_date='now')
        row_version = fake.sha256()

      
        writer.writerow([matric_no, last_name, first_name, other_names, title, maiden_name, gender, date_of_birth, email, telephone, created_by, created_at, updated_by, updated_at, row_version])

print(f"Data saved to {csv_file}")
 