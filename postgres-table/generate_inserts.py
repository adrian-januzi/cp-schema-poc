import random
import names
import faker

# Initialize a Faker generator
fake = faker.Faker()

def generate_insert_query(id):
    query = f"""
    INSERT INTO Person (id, addressid, firstname, email, phone, age, gender, updated_at)
    VALUES ({id}, {random.randint(100, 999)}, '{names.get_first_name()}', '{fake.email()}', '{fake.phone_number()}', {random.randint(18, 99)}, '{random.choice(['Male', 'Female'])}', {fake.date_time().timestamp()}000);
    """
    return query

def main():
    num_queries = int(input("Enter the number of INSERT queries to generate: "))

    with open('insert_queries.sql', 'w') as file:
        for id in range(1, num_queries + 1):
            file.write(generate_insert_query(id))

if __name__ == "__main__":
    main()
